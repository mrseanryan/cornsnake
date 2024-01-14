import os

from . import config
from . import util_file
from . import util_list
from . import util_proc

COMMIT_PARTS_SEPARTOR="_||_"

def _parse_result(result):
    parts = result.split(COMMIT_PARTS_SEPARTOR)
    parts_cleaned = []
    for part in parts:
        parts_cleaned.append(part.replace('"', ''))
    return parts_cleaned

def get_last_commit_id(path_to_repo_dir, file_only = None):
    # git log -n 1 --pretty=format:"%h_|\_%ad_|\_%s" --date=short BUILD.plz
    git_args = ['log', '-n', '1', f'--pretty=format:"%h{COMMIT_PARTS_SEPARTOR}%ad{COMMIT_PARTS_SEPARTOR}%s"', '--date=short']
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

def checkout_branch(branch, path_to_repo_dir):
    result = execute_command('checkout', [branch], path_to_repo_dir)
    return result

def check_has_no_changes(path_to_local_repo):
    # should return empty, if no changes
    result = execute_command('status', ['--porcelain'], path_to_local_repo)
    if len(result) > 0:
        message = f"Local repository at {path_to_local_repo} has changes. Please ensure the local repository is clean and has no outstanding changes."
        raise SystemExit(message)

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

def get_config(key, path_to_local_repo):
    result = execute_command('config', ['--get', key], path_to_local_repo)
    return result

def delete_branches_except(branches_to_keep, path_to_local_repo):
    branches = get_all_origin_branches(path_to_local_repo)
    branches_to_delete = util_list.except_for(branches, branches_to_keep)

    execute_command_in_chunks('push', ['-d', 'origin'], branches_to_delete, path_to_local_repo)
