#List comprehension with files
file_1 = open("day26/file1.txt", "r")
file_2 = open("day26/file2.txt", "r")

nums_1 = [int(line.strip('\n')) for line in file_1]
nums_2 = [int(line.strip('\n')) for line in file_2]

same_nums = [int(num) for num in nums_1 if num in nums_2]

print(same_nums)

file_2.close()
file_1.close()