import turtle
import pandas
# pandas.iterrows()

screen = turtle.Screen()
screen.title("India States Game")
image = "political_map.gif"  # Only gif's work with turtle
screen.addshape(image)
turtle.shape(image)


# states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
# x = []
# y = []

#
# def get_mouse_click_coor(x1, y1):
#      print(x1,y1)
#      x.append(x1)
#      y.append(y1)
#
# # turtle.onscreenclick(get_mouse_click_coor)
# with open("x.txt", mode="w") as file:
#      file.write(" ".join(x))
# data = []
#
# with open("y.txt",) as file:
#      data =file.readlines()
# for str in data:
#      x1, y1 = str.strip().split(" ")
#      x.append(x1)
#      y.append(y1)
#


# data = {
#      "states": states, "x" : x, "y": y
# }
# all_states = pandas.DataFrame(data)
# all_states.to_csv("states_36.csv")

data = pandas.read_csv("states_36.csv")
all_states = data.states.to_list()

guessed_state = []

while len(guessed_state) < 36:
    answer_state = screen.textinput(
        title=f" {len(guessed_state)} /" f" 36 States Correct", prompt="Guess a state!"
    ).title()
    print(answer_state)

    if answer_state == "Exit":
        # missing_states = []
        missing_states = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("new_data")
        break
    # If answer in dataframe i.e. CSV
    if (answer_state in all_states) and (answer_state not in guessed_state):
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(answer_state)
        t.write(state_data.states.item())


turtle.mainloop()

# screen.exitonclick()
