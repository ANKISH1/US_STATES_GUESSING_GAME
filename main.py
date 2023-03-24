import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state

correct_answers = []
# screen.textinput(title="Guess the state", prompt="What's another state's name?")


while len(correct_answers) < 50:
    answer_state = (screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                                     prompt="What's another state's name?")).title()

    if answer_state == "Exit":
        states_to_learn = []
        for i in states:
            if i not in correct_answers:
                states_to_learn.append(i)
        data_1 =pandas.Series(states_to_learn)
        data_1.to_csv("states_to_learn.csv")
        break


    def get_State(user_answer):
        x = int(data[data["state"] == user_answer].x)
        y = int(data[data["state"] == user_answer].y)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(x, y)
        tim.write(answer_state)


    for i in states:
        if i == answer_state:
            correct_answers.append(answer_state)
            get_State(answer_state)








#To get x and y coordinates on click when user clicks on a state in map
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor) #
# screen.exitonclick()