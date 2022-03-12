# List COMPREHENSION

numbers = [1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 55]
# square every item in the list
squared_numbers = [item ** 2 for item in numbers]
print(squared_numbers)

# Get only the even numbers from the list
result1 = [item for item in numbers if item % 2 == 0]
print(result1)

# creating a list called result which contains the numbers that are common in both files

file1 = open('file1.txt')
file = file1.readlines()
file1_list = [int(num) for num in file if num != '\n']
# print(file1_list)

file2 = open('file2.txt')
file2 = file2.readlines()
file2_list = [int(num) for num in file2 if num != '\n']
# print(file2_list)

result = [int(num) for num in file1_list if num in file2_list]

print(result)
