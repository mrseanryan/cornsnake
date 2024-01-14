import os

from . import config
from . import util_color
from . import util_validate
from . import util_date

prompt_token = " >"

QUESTION_COLOR = util_color.bcolors.OKCYAN

def input_custom(question, default):
    if isinstance(default, str):
        default = default.strip()
    if not config.IS_INTERACTIVE:
        print(question + str(default))
        return default
    return input(question).strip() or default

def input_with_format_date(question, default):
    question = util_color.colorize(question, QUESTION_COLOR) + f" [format = yyyy-mm-dd] [default is {default}]" + prompt_token
    while True:
        answer = input_custom(question, default)
        if util_date.is_valid_date_yyyy_mm_dd(answer):
            return answer
   
def boolToYorN(value):
   if value:
      return "Y"
   return "N"

def input_list_of_branches(question, default):
    if not config.IS_INTERACTIVE:
        return default
    items = []
    question = util_color.colorize(question, QUESTION_COLOR) + f" [default is {default}]" + prompt_token
    is_valid = False
    while not is_valid:
        answer = input_custom(question, "")
        if len(answer) > 0:
            error = util_validate.check_is_branch_name_or_empty(answer, 'branch name')
            if error:
                print(error)
            else:
                items.append(answer)
        elif len(items) > 0:
            is_valid = True
        elif len(default) > 0:
            items = default
            is_valid = True
    return items

def input_branch_name_required(question, default):
    question = util_color.colorize(question, QUESTION_COLOR) + f"[Default = {default}]"
    while True:
        answer = input_custom(question, default)
        if answer and len(answer) > 0:
            error = util_validate.check_is_branch_name_or_empty(answer, 'branch name')
            if error:
                print(error)
            else:
                return answer

def input_required__dir_path(question, default):
    question = util_color.colorize(question, QUESTION_COLOR) + f" [default is {default}]" + prompt_token
    while True:
        answer = input_custom(question, default)
        if len(answer) > 0:
            if (not os.path.isdir(answer)):
                print(f" ! ERROR: That directory does not exist")
            else:
                return answer

def input_with_format_y_or_n(question, default):
    question = util_color.colorize(question, QUESTION_COLOR) + f" [Y or N] [default is {boolToYorN(default)}]" + prompt_token
    while True:
        answer = input_custom(question, default)
        if not config.IS_INTERACTIVE:
            return answer
        if len(answer) == 0 and default is not None:
           return default
        if answer == "Y":
           return True
        if answer == "N":
           return False

def input_with_format_git_filter_repo_size(question, default):
    question = util_color.colorize(question, QUESTION_COLOR) + f"[Values are like 256K or 1M or 1G][Default = {default}]" + prompt_token
    while True:
        answer = input_custom(question, default)
        if len(answer) == 0:
           return default
        if util_validate.is_valid_blob_size(answer):
            return answer

def input_optional(question, default):
    question = util_color.colorize(question, QUESTION_COLOR) + f"[Default = {default}]"
    answer = input_custom(question, default)
    return answer
