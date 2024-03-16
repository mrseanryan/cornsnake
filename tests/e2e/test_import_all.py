import cornsnake_src

print(f"Using cornsnake [{cornsnake_src.__version__}] - 'import cornsnake'")

print("== util_print ==")
print('util_print.print_warning("a warning")')
cornsnake_src.util_print.print_warning("a warning")
print('util_print.print_error("an error")')
cornsnake_src.util_print.print_error("an error")

print("== util_progress ==")
total = 1000
count = 10
cornsnake_src.util_progress.progress(count, total)
cornsnake_src.util_wait.wait_seconds(1)
cornsnake_src.util_progress.progress(50, total)
cornsnake_src.util_wait.wait_seconds(1)
cornsnake_src.util_progress.complete()

print("== util_string ==")
print('util_string.is_empty("")', cornsnake_src.util_string.is_empty(""))
print('util_string.is_empty(" ")', cornsnake_src.util_string.is_empty(" "))
print('util_string.is_empty(" x")', cornsnake_src.util_string.is_empty(" x"))
