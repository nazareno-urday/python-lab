# Doubles even numbers and add them to the list
new_list = [n * 2 for n in range(1,11) if n % 2 == 0]
print(new_list)

names = ["Alex", "Mark", "Nazareno", "Tommy", "Charles", "Tyler", "Mourinho"]
# Creates a new list with names shorter than 6 characters and converts them to uppercase
new_names_list = [name.upper() for name in names if len(name) < 6]
print(new_names_list)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Creates a new list which every number in the list is squared
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# Converts strings into numbers
numbers = [int(letter) for letter in list_of_strings]
# Creates a list with only even numbers
result = [number for number in numbers if number % 2 == 0]
print(result)

# Creates a list of numbers repeated in different files
with open("file1.txt") as file:
    nums1 = [int(line.strip()) for line in file if line.strip()]
with open("file2.txt") as file:
    nums2 = [int(line.strip()) for line in file if line.strip()]
result = [number for number in nums1 if number in nums2]
print(result)