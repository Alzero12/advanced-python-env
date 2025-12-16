a = float(input())

int_part = int(a)
fractional_part = int(round((a - int_part) * 100))

new = fractional_part + int_part / 100
print(new)
