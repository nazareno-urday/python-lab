# FileNotFoundError handling
try:
    file = open("hello.txt")
    my_dictionary = {"key":"value"}
    print(my_dictionary["key"])
except FileNotFoundError:
    file = open("hello.txt", "w")
    file.write("Hello World")
except KeyError as error:
    print(f"The key: {error} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()

height = float(input("Please enter your height in meters: "))
weight = int(input("Please enter your weight in kilograms: "))

# Creating my own exception with "raise"
if height >= 3:
    raise ValueError("Human height cant be greater than 3")

bmi = weight / (height ** 2)
print("Your BMI is: ", bmi)

# IndexError handling
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")

make_pie(4)

# KeyError handling
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass

    return total_likes

print(count_likes(facebook_posts))