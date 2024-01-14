import cornsnake

print(f"Using cornsnake [{cornsnake.__version__}]")

print("== util_string ==")
print('util_string.is_empty("")', cornsnake.util_string.is_empty(""))
print('util_string.is_empty(" ")', cornsnake.util_string.is_empty(" "))
print('util_string.is_empty(" x")', cornsnake.util_string.is_empty(" x"))
