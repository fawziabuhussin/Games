import turtle
import pandas

# Gif because turtle only works with this type of files.

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


#        THIS CODE JUST TO GET CORDS ON THE SCREEN!

# def get_mouse_cord (x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_cord)
#
# turtle.mainloop()


# print(answer_state)

gameOn = True


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []
missing_state = []
while len(guessed_state) < 50:
#If the states is on.
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_state)}/50", prompt="What's the name of the state?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        # return csv of all the missed states.
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break

    # Make turtle to write the name of the state on the screen.
    if answer_state in all_states:
        tur = turtle.Turtle()
        tur.penup()
        tur.hideturtle()
        state_data = data[data["state"] == answer_state]
        tur.goto(int(state_data.x), int(state_data.y))
        tur.write(answer_state)
        guessed_state.append(answer_state)
        #Create a turtle to write the state on the screen.


