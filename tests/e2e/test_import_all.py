import cornsnake

print(f"Using cornsnake [{cornsnake.__version__}] - 'import cornsnake'")

print("== util_print ==")
print('util_print.print_warning("a warning")')
cornsnake.util_print.print_warning("a warning")
print('util_print.print_error("an error")')
cornsnake.util_print.print_error("an error")

print("== util_progress ==")
total = 1000
count = 10
cornsnake.util_progress.progress(count, total)
cornsnake.util_wait.wait_seconds(1)
cornsnake.util_progress.progress(50, total)
cornsnake.util_wait.wait_seconds(1)
cornsnake.util_progress.complete()

print("== util_string ==")
print('util_string.is_empty("")', cornsnake.util_string.is_empty(""))
print('util_string.is_empty(" ")', cornsnake.util_string.is_empty(" "))
print('util_string.is_empty(" x")', cornsnake.util_string.is_empty(" x"))
