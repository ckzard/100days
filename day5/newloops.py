from unicodedata import numeric


a = 1
b = 101
total = 0

for number in range(a, b):
    if number == 1 or number % 2 == 0:
        total += number


print(total)