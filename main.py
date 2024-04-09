# Print boolean values in Python

my_bool = True

# ✅ print boolean value
print(my_bool)  # 👉️ True

# ✅ print boolean value in a string
print(f'is subscribed: {my_bool}')  # 👉️ is subscribed: True

# ✅ print integer representation of boolean value
print(int(True))  # 👉️ 1
print(int(False))  # 👉️ 0

# ✅ print boolean value converted to lowercase
print(f'{my_bool}'.lower())  # 👉️ true

# ✅ Convert a value to a boolean
print(bool('hello'))  # 👉️ True
print(bool(0))  # 👉️ False