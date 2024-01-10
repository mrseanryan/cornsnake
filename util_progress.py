import sys

import config

previous_percent = 0
def progress(count, total, status='', bar_len=60):
    global previous_percent
    filled_len = int(round(bar_len * count / float(total)))

    percent = round(100.0 * count / float(total), 1)

    if config.MINIMIZE_PROGRESS_BAR_OUTPUT:
        if percent < previous_percent:
            # reset:
            previous_percent = percent
        else:
            if percent - previous_percent < 10:
                return
    previous_percent = percent

    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    fmt = '[%s] %s%s ...%s' % (bar, percent, '%', status)
    print('\b' * len(fmt), end='')  # clears the line
    sys.stdout.write(fmt)
    sys.stdout.flush()
