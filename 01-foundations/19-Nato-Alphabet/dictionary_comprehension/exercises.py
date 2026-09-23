import random

# Creates a students dictionary and for each of them, it creates a random score
names = ["Alex", "Mark", "Nazareno", "Tommy", "Charles", "Tyler", "Mourinho"]
students = {name: random.randint(1,100 ) for name in names}
# Creates a dictionary that shows those students who got a score over 60
pass_students = {name: score for (name, score) in students.items() if score >= 60}
print(pass_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_of_words = sentence.split()
# Create a result dictionary that takes each word and calculates the number of letters
result = {word:len(word) for word in list_of_words}
print(result)

# Using a dictionary, creates another that shows the temperature in degrees Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()}
print(weather_f)


"""Now how to work with a data frame?"""
import pandas as pd
student_dict = {
    "student":["Alex", "Marcos", "Nazareno"],
    "score": [67,89,55]
}

# Looping through columns of a Dataframe
df  = pd.DataFrame(student_dict)
print(df.head())

for (key,value) in df.items():
    print(value)

# How to loop through a row?
for (index,row) in df.iterrows():
    if row.student == "Nazareno":
        print(row.score)