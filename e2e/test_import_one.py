from cornsnake import util_print, util_string, __version__

print(f"Using cornsnake [{__version__}] - 'from import X'")

print("== util_print ==")
print('util_print.print_warning("a warning")')
util_print.print_warning("a warning")
print('util_print.print_error("an error")')
util_print.print_error("an error")

print("== util_string ==")
print('util_string.is_empty("")', util_string.is_empty(""))
print('util_string.is_empty(" ")', util_string.is_empty(" "))
print('util_string.is_empty(" x")', util_string.is_empty(" x"))
