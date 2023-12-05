import os

import util_validate
import util_date

prompt_token = " >"

def input_with_format_date(question, default):
    question += f" [format = yyyy-mm-dd] [default is {default}]" + prompt_token
    while True:
        answer = input(question).strip() or default
        if util_date.is_valid_date_yyyy_mm_dd(answer):
            return answer
   
def boolToYorN(value):
   if value:
      return "Y"
   return "N"

def input_list(question, default):
    items = []
    question += f" [default is {default}]" + prompt_token
    is_valid = False
    while not is_valid:
        answer = input(question).strip()
        if len(answer) > 0:
            items.append(answer)
        elif len(items) > 0:
            is_valid = True
        elif len(default) > 0:
            items = default
            is_valid = True
    return items

def input_required__dir_path(question, default):
    question += f" [default is {default}]" + prompt_token
    while True:
        answer = input(question).strip() or default
        if len(answer) > 0:
            if (not os.path.isdir(answer)):
                print(f" ! ERROR: That directory does not exist")
            else:
                return answer

def input_with_format_y_or_n(question, default):
    question += f" [Y or N] [default is {boolToYorN(default)}]" + prompt_token
    while True:
        answer = input(question).strip()
        if len(answer) == 0 and default is not None:
           return default
        if answer == "Y":
           return True
        if answer == "N":
           return False

def input_with_format_git_filter_repo_size(question, default):
    question += f"[Values are like 256K or 1M or 1G][Default = {default}]" + prompt_token
    while True:
        answer = input(question).strip()
        if len(answer) == 0:
           return default
        if util_validate.is_valid_blob_size(answer):
            return answer

def input_optional(question, default):
    question += f"[Default = {default}]"
    answer = input(question).strip() or default
    return answer
