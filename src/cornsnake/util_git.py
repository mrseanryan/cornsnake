import os

from . import config
from . import util_date
from . import util_file
from . import util_list
from . import util_print
from . import util_log
from . import util_proc

COMMIT_PARTS_SEPARTOR="_||_"

logger = util_log.getLogger(__name__)

def _parse_result(result):
    parts = result.split(COMMIT_PARTS_SEPARTOR)
    parts_cleaned = []
    for part in parts:
        parts_cleaned.append(part.replace('"', ''))
    return parts_cleaned

def get_current_branch(local_repo_location):
    return execute_command('rev-parse', ['--abbrev-ref', 'HEAD'], local_repo_location).strip()

def get_last_commit_id(path_to_repo_dir, file_only = None):
    # git log -n 1 --pretty=format:"%H_|\_%ad_|\_%s" --date=short BUILD.plz
    git_args = ['log', '-n', '1', f'--pretty=format:"%H{COMMIT_PARTS_SEPARTOR}%ad{COMMIT_PARTS_SEPARTOR}%s"', '--date=short']
    if file_only is not None:
        git_args += [file_only]
    result = util_proc.run_process_and_get_output(config.PATH_TO_GIT, git_args, path_to_repo_dir)
    if config.IS_VERBOSE:
        print("  " + result)
    parsed = _parse_result(result)
    commit = parsed[0]
    return commit

def execute_command(command, git_args, working_dir):
    git_args_with_command = [command] + git_args
    return util_proc.run_process_and_get_output(config.PATH_TO_GIT, git_args_with_command, working_dir)

# execute git command with too many parameters - so we chunk
def execute_command_in_chunks(command, git_args, git_extra_args_to_chunk, working_dir):
    CHUNK_SIZE = 20
    chunks = util_list.chunk(git_extra_args_to_chunk, CHUNK_SIZE)
    for chunk in chunks:
        execute_command(command, git_args + chunk, working_dir)

def fetch_notes(working_dir):
    execute_command('fetch', ['origin', 'refs/notes/*:refs/notes/*', '--force'], working_dir)

def checkout_branch(branch, path_to_repo_dir):
    result = execute_command('checkout', [branch], path_to_repo_dir)
    return result

def checkout_at_start_of_date(local_repo_location, branch, start_date):
    # git rev-list -n 1 --first-parent --before="2023-12-22 00:00" main
    last_commit = execute_command('rev-list', ['-n', '1', '--first-parent', f'--before="{start_date} 00:00"', branch], local_repo_location)
    last_commit = last_commit.strip()
    if last_commit:
        checkout_branch(last_commit, local_repo_location, True)
        return True
    return False

def checkout_head(local_repo_location, branch):
    checkout_branch(branch, local_repo_location)

def check_has_no_changes(path_to_local_repo):
    # should return empty, if no changes
    result = execute_command('status', ['--porcelain'], path_to_local_repo)
    if len(result) > 0:
        message = f"Local repository at {path_to_local_repo} has changes. Please ensure the local repository is clean and has no outstanding changes."
        raise RuntimeError(message)

def _prepare_local_clone(path_to_repo_dir, temp_git_fixer_dir, is_mirror):
    local_clone_dir = os.path.join(temp_git_fixer_dir, "lm") # lm = local_mirror (keeping path short)
    util_file.ensure_dir_exists(local_clone_dir)
    args = [path_to_repo_dir]
    if is_mirror:
        args = ['--mirror'] + args
    execute_command('clone', args, local_clone_dir)

    local_repo_name = util_file.get_last_part_of_path(path_to_repo_dir)
    if is_mirror:
        local_repo_name += ".git"
    else:
        if local_repo_name.endswith(".git"):
            local_repo_name = local_repo_name[:-4]
    return os.path.join(local_clone_dir, local_repo_name)

def prepare_local_full_clone(path_to_repo_dir, temp_git_fixer_dir):
    return _prepare_local_clone(path_to_repo_dir, temp_git_fixer_dir, False)

def prepare_local_mirror_clone(path_to_repo_dir, temp_git_fixer_dir):
    return _prepare_local_clone(path_to_repo_dir, temp_git_fixer_dir, True)

def gc_expire_reflog(repo_dir):
    # Expires the reflog, which helps a following 'gc prune' to remove more garbage
    execute_command('reflog', ['expire', '--expire=now', '--all'], repo_dir)

def gc_prune_aggressive(mirror_clone_dir):
    result = execute_command('gc', ['--prune=now', '--aggressive'], mirror_clone_dir)
    return result

def gc_prune_now(repo_dir):
    execute_command('gc', ['--prune=now'], repo_dir)

def gc_prune_safe(repo_dir):
    execute_command('gc', [], repo_dir)

def remove_origin_and_remote_branches(repo_dir):
    execute_command('remote', ['remove', 'origin'], repo_dir)

def remove_tag(repo_dir, tag):
    execute_command('tag', ['-d', tag], repo_dir)

def get_commits_after_date(repo_dir, branches, start_date):
    commits = []
    for branch in branches:
        checkout_branch(branch, repo_dir)

        # git log --pretty=format:"%H" --after="2023-01-31"
        day_before_cutoff = util_date.add_day_to_date(start_date, -1)
        result = execute_command('log', ['--pretty=format:"%H"', f'--after="{day_before_cutoff}"'], repo_dir)
        commits += result.split('\n')
    cleaned_commits = []
    for commit in commits:
        cleaned = commit.replace('"', '').strip()
        cleaned_commits.append(cleaned)
    return cleaned_commits

def get_git_text_editor_or_none(local_repo_location):
    path_to_text_editor = get_config('core.editor', local_repo_location)
    if path_to_text_editor is None or len(path_to_text_editor) == 0:
        return (None, None)
    error_message = f"Cannot parse default git text editor ('core.editor' = '{path_to_text_editor}')"
    # Unfortunately, value can be like '"program" command'. To be able to execute 'program', we need to split that out:
    program = path_to_text_editor
    args = []
    try:
        if '"' in path_to_text_editor:
            if path_to_text_editor.count('"') == 2:
                parts = path_to_text_editor.split('"')  # '"path to exe" cmd' -> ['', 'path to exe', ' cmd']
                parts = util_list.strip_strings(parts)
                program = parts[1]
                args = parts[2:]
    except Exception as e:
        util_log.log_exception(e)
        # Intentionally NOT passing exception onwards
    if os.path.exists(program):
        return (program, args)
    util_print.print_custom(error_message)
    return (None, None)

def get_all_tags(path_to_local_repo):
    tags = []
    result = execute_command('tag', [], path_to_local_repo)
    raw_tags = result.split('\n')
    for raw_tag in raw_tags:
        raw_tag = raw_tag.strip()
        if raw_tag:
            tags.append(raw_tag)
    return tags

def delete_all_tags(path_to_local_repo):
    tags = get_all_tags(path_to_local_repo)
    execute_command_in_chunks('push', ['--delete', 'origin', '--quiet'], tags, path_to_local_repo)

def get_all_origin_branches(path_to_local_repo):
    branches = []
    result = execute_command('branch', ['-r'], path_to_local_repo)
    raw_branches = result.split('\n')
    for raw_branch in raw_branches:
        if 'origin' not in raw_branch:
            continue
        if '->' in raw_branch:
            continue
        raw_branch = raw_branch.strip()
        raw_branch = raw_branch.removeprefix('origin/')
        if raw_branch:
            branches.append(raw_branch)
    return branches

def delete_branches_except(branches_to_keep, path_to_local_repo):
    # original bash:
    #   git branch -r | grep -Eo 'origin/.*' | grep -v 'origin/main$' | sed 's/origin\///' | xargs git push origin -v --delete
    # OR this one seems more reliable:
    #   git branch -r | grep -Eo 'origin/.*' | grep -v 'origin/main$' | sed 's/origin\///' | xargs git push -d origin
    branches = get_all_origin_branches(path_to_local_repo)
    branches_to_delete = util_list.except_for(branches, branches_to_keep)

    execute_command_in_chunks('push', ['-d', 'origin'], branches_to_delete, path_to_local_repo)

def get_config(key, path_to_local_repo):
    result = ""
    try:
        result = execute_command('config', ['--get', key], path_to_local_repo, False)
    except RuntimeError as re:
        # If the config key is missing, then git returns exit code 1 and empty stderr
        if len(re.args) == 2 and re.args[1] == 1:
            if config.IS_VERBOSE:
                util_print.print_custom(f"[ok] git config has no value for setting '{key}'")
            return ""
        raise
    return result

def log_git_config(path_to_local_repo):
    # Log interesting config settings that can cause issues, especially with text files:
    interesting_settings = [
        'i18n.filesencoding',
        'core.ignorecase',  # Probably best set to false.
        'core.autocrlf',  # Caused encoding exception on validation (which we handle now). Probably best set to false - line-endings.
        'diff.astextplain.textconv'
        ]

    logger.info('git config - text related settings')
    for setting in interesting_settings:
        value = get_config(setting, path_to_local_repo)
        if len(value) > 0:
            logger.info(f'  {setting}={value}')
        else:
            logger.info(f'  {setting} is not set [ok]')

settings_best_set_to_false = [
    'core.ignorecase',  # Probably best set to false.
    'core.autocrlf',  # Caused encoding exception on validation (which we handle now). Probably best set to false - line-endings.
]

def is_git_ignored(directory, filename):
    try:
        execute_command('check-ignore', [filename], directory, False)
    except RuntimeError as re:
        if len(re.args) == 2:
            exit_code = re.args[1]
            if exit_code == 0:
                # 0 - One or more of the provided paths is ignored.
                return True
            elif exit_code == 1:
                # 1 - None of the provided paths are ignored.
                return False
            # 128 - A fatal error was encountered.
            # any other exit code
            raise
    # 0 - One or more of the provided paths is ignored.
    return True
