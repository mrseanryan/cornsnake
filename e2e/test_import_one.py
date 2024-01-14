from cornsnake import util_string, __version__

print(f"Using cornsnake [{__version__}] - 'from import X'")

print("== util_string ==")
print('util_string.is_empty("")', util_string.is_empty(""))
print('util_string.is_empty(" ")', util_string.is_empty(" "))
print('util_string.is_empty(" x")', util_string.is_empty(" x"))
