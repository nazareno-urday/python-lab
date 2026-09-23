from turtle import Turtle, Screen
import pandas as pd

def create_turtle():
    state_name = Turtle()
    state_name.color("black")
    state_name.hideturtle()
    state_name.penup()
    state_name.goto(coords)
    state_name.write(guess)

def create_csv():
    missing_states = [state for state in states if state not in correct_guesses]
    new_df = pd.DataFrame({"state": missing_states})
    new_df.to_csv("missing_states.csv", index=False)

df = pd.read_csv("50_states.csv")
screen = Screen()
screen.title("US States map game")
image = "blank_states_img.gif"
turtle = Turtle()

states = list(df.state) # Turns the states in the csv into an iterable list
screen.addshape(image)
turtle.shape(image)

score = 0
in_game = True
correct_guesses = []

while in_game:

    guess = str(screen.textinput(
        title=f"{score}/50 states correct",
        prompt="Whats the next state name?")).title()

    if guess == "Exit":
        in_game = False
        create_csv()

    elif guess not in correct_guesses:
        if guess in states:
            correct_guesses.append(guess)

            state_coords = df[df.state == guess]
            state_xcor = state_coords["x"].item()
            state_ycor = state_coords["y"].item()
            coords = (state_xcor, state_ycor)

            create_turtle()
            score += 1

            if score == 50:
                in_game = False
                print("Congratulations, you guessed all 50 states!")

        else:
            in_game = False
            print(f"Wrong guess! Your score was {score}")
            create_csv()

    else:
        print(f"You have already guessed '{guess}'")