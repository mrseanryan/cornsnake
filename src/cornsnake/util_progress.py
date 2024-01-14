import sys

import config_system

previous_percent = 0
def progress(count, total):
    global previous_percent

    percent = round(100.0 * count / float(total), 1)

    if config_system.MINIMIZE_PROGRESS_BAR_OUTPUT:
        if percent < previous_percent:
            # reset:
            previous_percent = percent
        else:
            if percent - previous_percent < 10:
                return
    previous_percent = percent

    _update_progress(percent)

def _update_progress(percent):
    bar_len = 60
    filled_len = int(round(bar_len * percent / float(100)))

    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    fmt = '[%s] %s%s ...' % (bar, percent, '%')
    print('\b' * len(fmt), end='')  # clears the line
    sys.stdout.write(fmt)
    sys.stdout.flush()

def complete():
    _update_progress(100)
    print("")  # ensure a new line
