size = int(input("How many elements would you like to introduce?: "))
elements = []

for i in range(size):
    choice = int(input("Enter a number: "))
    elements.append(choice)

temp = 0
for i in range(size):
    for j in range(size):
        if elements[i] < elements[j]:
            temp = elements[i]
            elements[i] = elements[j]
            elements[j] = temp

print(f"This is the sorted list: {elements}")
