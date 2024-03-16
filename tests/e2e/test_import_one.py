from cornsnake_src import util_print, util_progress, util_string, util_wait, __version__

print(f"Using cornsnake [{__version__}] - 'from import X'")

print("== util_print ==")
print('util_print.print_warning("a warning")')
util_print.print_warning("a warning")
print('util_print.print_error("an error")')
util_print.print_error("an error")

print("== util_progress ==")
total = 1000
count = 10
util_progress.progress(count, total)
util_wait.wait_seconds(1)
util_progress.progress(50, total)
util_wait.wait_seconds(1)
util_progress.complete()

print("== util_string ==")
print('util_string.is_empty("")', util_string.is_empty(""))
print('util_string.is_empty(" ")', util_string.is_empty(" "))
print('util_string.is_empty(" x")', util_string.is_empty(" x"))
