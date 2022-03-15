numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
#print(new_list)

name = "Chris"
new_name = [letter for letter in name]
# makes a list of the letters
#print(new_name)

new_range = [num * 2 for num in range(1, 5)]
#print(new_range)

# you can add conditions to list comprehensions as well
names = ['Alex', "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]
#print(short_names)

upper_names = [name.upper() for name in names if len(name) > 4]
#print(upper_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num**2 for num in numbers]
#you can square by either **2 or num*num obviously
# print(squared_numbers)

result = [num for num in numbers if num % 2 == 0]
print(result)

