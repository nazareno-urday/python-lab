size = int(input("Enter number of elements: "))
elements = []

for i in range(size):
    num = int(input("Enter element: "))
    elements.append(num)

temp = 0
for i in range(size):
    for j in range(size - 1):
        if elements[j] > elements[j + 1]:
            temp = elements[j]
            elements[j] = elements[j + 1]
            elements[j + 1] = temp

print(f"sorted elements: {elements}")