import random
from telnetlib import EC
from tkinter import *
from time import *
from time import sleep
from tkinter import *

window = Tk()
window_width = 1060
window_height = 900
x_location = (window.winfo_screenwidth() - window_width) / 2
y_location = (window.winfo_screenheight() - window_height) / 2
window.geometry(f'{window_width}x{window_height}+{int(x_location)}+{int(y_location)}')
window.title("Search Algorithm")
window.config(background="#999999")

# number generator
number_list = []
active_list = []
list_filler = 0
while len(number_list) <= 520:
    curr = list_filler + random.randint(1, 20)
    number_list.append(curr)
    active_list.append(0)
    list_filler = curr

# canvas and drawings
canvas = Canvas(window, height=window_height, width=window_width, bg="#ffffff")
canvas.pack()

drawing = 0

y = 0
count = 0
for j in range(0, 20):
    for i in range(0, 25):
        curr = i * 40
        canvas.create_rectangle(30 + curr, 70 + y, 70 + curr, 110 + y, outline="#000000", fill="#fb0")
        label = Label(text=number_list[count], bg="#fb0", width=4)
        label.place(x=33 + curr, y=80 + y)
        count += 1
    y += 40


x = 0

high = 499
low = 0

first_draw = 0


def binary():
    while active_list[0] == 1:
        y = 0
        count = 0
        for j in range(0, 20):
            for i in range(0, 25):
                curr = i * 40
                canvas.create_rectangle(30 + curr, 70 + y, 70 + curr, 110 + y, outline="#000000", fill="#fb0")
                label = Label(text=number_list[count], bg="#fb0", width=4)
                label.place(x=33 + curr, y=80 + y)
                count += 1
            y += 40
        active_list[0] = 0
        binary_label.config(text="0")

    input = entry_box.get()
    low = int(low_label["text"])
    high = int(high_label["text"])
    repeat = True

    middle = int(((high - low) / 2) + low)
    low_x = (low % 25)
    low_y = int(low / 25)
    high_x = high % 25
    high_y = int(high / 25)
    current_x = (middle % 25)
    current_y = int(middle / 25)
    if int(input) == number_list[middle]:

        low_label.config(text=middle)
        high_label.config(text=middle)
        repeat = False
    elif int(input) > number_list[middle]:
        low_label.config(text=middle)

    elif int(input) < number_list[middle]:
        high_label.config(text=middle)

    print("current :" + str(number_list[middle]))
    canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                            outline="#000000",
                            fill="#02f702")
    label = Label(text=number_list[middle], bg="#02f702", width=4)
    label.place(x=33 + current_x * 40, y=80 + current_y * 40)
    canvas.create_rectangle(30 + low_x * 40, 70 + low_y * 40, 70 + low_x * 40, 110 + low_y * 40, outline="#000000",
                            fill="#ff0000")
    label1 = Label(text=">", bg="#ff0000", width=4, fg="#ffffff")
    label1.place(x=33 + low_x * 40, y=80 + low_y * 40)
    canvas.create_rectangle(30 + high_x * 40, 70 + high_y * 40, 70 + high_x * 40, 110 + high_y * 40, outline="#000000",
                            fill="#0303ff")
    label2 = Label(text="<", bg="#0303ff", width=4, fg="#ffffff")
    label2.place(x=33 + high_x * 40, y=80 + high_y * 40)
    binary_current=int(binary_label["text"])
    binary_label.config(text=binary_current+1)
    if repeat:
        binary_button.after(3000, binary)
    else:
        active_list[0] = 1
        low_label.config(text="0")
        high_label.config(text="499")


def linear():
    while active_list[0] == 1:
        y = 0
        count = 0
        for j in range(0, 20):
            for i in range(0, 25):
                curr = i * 40
                canvas.create_rectangle(30 + curr, 70 + y, 70 + curr, 110 + y, outline="#000000", fill="#fb0")
                label = Label(text=number_list[count], bg="#fb0", width=4)
                label.place(x=33 + curr, y=80 + y)
                count += 1
            y += 40
        active_list[0] = 0
        linear_label.config(text="0")
    linear_input = entry_box.get()
    repeat = True
    middle = int(middle_label["text"])
    current_x = (middle % 25)
    current_y = int(middle / 25)

    if number_list[middle] == int(linear_input):
        canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                                outline="#000000",
                                fill="#02f702")
        label = Label(text=number_list[middle], bg="#02f702", width=4)
        label.place(x=33 + current_x * 40, y=80 + current_y * 40)
        repeat = False
    else:
        middle_label.config(text=(middle + 1))
        canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                                outline="#000000",
                                fill="#ff0000")
        label = Label(text="X", bg="#ff0000", width=4, fg="#ffffff")
        label.place(x=33 + current_x * 40, y=80 + current_y * 40)
        linear_current= int(linear_label["text"])
        linear_label.config(text=linear_current+1)
    if repeat:
        linear_button.after(25, linear)
    else:
        active_list[0] = 1
        middle_label.config(text="0")


def jump_search():
    while active_list[0] == 1:
        y = 0
        count = 0
        for j in range(0, 20):
            for i in range(0, 25):
                curr = i * 40
                canvas.create_rectangle(30 + curr, 70 + y, 70 + curr, 110 + y, outline="#000000", fill="#fb0")
                label = Label(text=number_list[count], bg="#fb0", width=4)
                label.place(x=33 + curr, y=80 + y)
                count += 1
            y += 40
        active_list[0] = 0
        jump_label.config(text="0")

    jump_input = int(entry_box.get())
    repeat = True
    middle = int(middle_label["text"])
    current_x = (middle % 25)
    current_y = int(middle / 25)

    if jump_input > number_list[middle]:
        middle_label.config(text=middle + 7)
        canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                                outline="#000000",
                                fill="#ff0000")
        label = Label(text="X", bg="#ff0000", width=4, fg="#ffffff")
        label.place(x=33 + current_x * 40, y=80 + current_y * 40)
    elif jump_input < number_list[middle]:
        middle_label.config(text=middle - 1)
        canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                                outline="#000000",
                                fill="#0303ff")
        label = Label(text="<", bg="#0303ff", width=4, fg="#ffffff")
        label.place(x=33 + current_x * 40, y=80 + current_y * 40)
    else:
        middle_label.config(text=middle - 1)
        canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                                outline="#000000",
                                fill="#02f702")
        label = Label(text=number_list[middle], bg="#02f702", width=4)
        label.place(x=33 + current_x * 40, y=80 + current_y * 40)
        repeat = False
    jump_current=int(jump_label["text"])
    jump_label.config(text=jump_current+1)
    if repeat:
        jump_search_button.after(50, jump_search)
    else:
        active_list[0] = 1
        middle_label.config(text="0")


def interpolation():
    while active_list[0] == 1:
        y = 0
        count = 0
        for j in range(0, 20):
            for i in range(0, 25):
                curr = i * 40
                canvas.create_rectangle(30 + curr, 70 + y, 70 + curr, 110 + y, outline="#000000", fill="#fb0")
                label = Label(text=number_list[count], bg="#fb0", width=4)
                label.place(x=33 + curr, y=80 + y)
                count += 1
            y += 40
        active_list[0] = 0
        interpolation_label.config(text="0")


    interpolation_input = int(entry_box.get())

    interpolation_low = int(low_label["text"])
    interpolation_high = int(high_label["text"])
    repeat = True

    middle = interpolation_low + int(((interpolation_input-number_list[interpolation_low])*(interpolation_high-interpolation_low))/(number_list[interpolation_high]-number_list[interpolation_low]))
    print(middle)
    low_x = (interpolation_low % 25)
    low_y = int(interpolation_low / 25)
    high_x = interpolation_high % 25
    high_y = int(interpolation_high / 25)
    current_x = (middle % 25)
    current_y = int(middle / 25)
    if int(interpolation_input) == number_list[middle]:

        low_label.config(text=middle)
        high_label.config(text=middle)
        repeat = False
    elif int(interpolation_input) > number_list[middle]:
        low_label.config(text=middle)

    elif int(interpolation_input) < number_list[middle]:
        high_label.config(text=middle)

    print("current :" + str(number_list[middle]))
    canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                            outline="#000000",
                            fill="#02f702")
    label = Label(text=number_list[middle], bg="#02f702", width=4)
    label.place(x=33 + current_x * 40, y=80 + current_y * 40)
    canvas.create_rectangle(30 + low_x * 40, 70 + low_y * 40, 70 + low_x * 40, 110 + low_y * 40, outline="#000000",
                            fill="#ff0000")
    label1 = Label(text=">", bg="#ff0000", width=4, fg="#ffffff")
    label1.place(x=33 + low_x * 40, y=80 + low_y * 40)
    canvas.create_rectangle(30 + high_x * 40, 70 + high_y * 40, 70 + high_x * 40, 110 + high_y * 40, outline="#000000",
                            fill="#0303ff")
    label2 = Label(text="<", bg="#0303ff", width=4, fg="#ffffff")
    label2.place(x=33 + high_x * 40, y=80 + high_y * 40)
    interpolation_current = int(interpolation_label["text"])
    interpolation_label.config(text=interpolation_current + 1)
    if repeat:
        interpolation_button.after(500, interpolation)
    else:
        active_list[0] = 1
        low_label.config(text="0")
        high_label.config(text="499")


def exponential():
    while active_list[0] == 1:
        y = 0
        count = 0
        for j in range(0, 20):
            for i in range(0, 25):
                curr = i * 40
                canvas.create_rectangle(30 + curr, 70 + y, 70 + curr, 110 + y, outline="#000000", fill="#fb0")
                label = Label(text=number_list[count], bg="#fb0", width=4)
                label.place(x=33 + curr, y=80 + y)
                count += 1
            y += 40
        active_list[0] = 0
        exponential_label.config(text="0")

    jump_input = int(entry_box.get())
    repeat = True
    middle = int(middle_label["text"])
    if (middle > 499):
        middle = 499
    print(middle)
    current_x = (middle % 25)
    current_y = int(middle / 25)

    if jump_input > number_list[middle]:
        middle_label.config(text=middle*2+1)
        canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                                outline="#000000",
                                fill="#ff0000")
        label = Label(text="X", bg="#ff0000", width=4, fg="#ffffff")
        label.place(x=33 + current_x * 40, y=80 + current_y * 40)
    elif jump_input < number_list[middle]:
        middle_label.config(text=middle - 1)
        canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                                outline="#000000",
                                fill="#0303ff")
        label = Label(text="<", bg="#0303ff", width=4, fg="#ffffff")
        label.place(x=33 + current_x * 40, y=80 + current_y * 40)
    else:
        middle_label.config(text=middle - 1)
        canvas.create_rectangle(30 + current_x * 40, 70 + current_y * 40, 70 + current_x * 40, 110 + current_y * 40,
                                outline="#000000",
                                fill="#02f702")
        label = Label(text=number_list[middle], bg="#02f702", width=4)
        label.place(x=33 + current_x * 40, y=80 + current_y * 40)
        repeat = False
    exponential_current=int(exponential_label["text"])
    exponential_label.config(text=exponential_current+1)
    if repeat:
        exponential_button.after(50, exponential)
    else:
        active_list[0] = 1
        middle_label.config(text="0")


binary_button = Button(canvas, text="binary", command=binary, width=10, bg="#222222", fg="#ffffff")
binary_button.place(x=500, y=18)
linear_button = Button(canvas, text="linear", command=linear, width=10, bg="#222222", fg="#ffffff")
linear_button.place(x=600, y=18)
jump_search_button = Button(canvas, text="jump", command=jump_search, width=10, bg="#222222", fg="#ffffff")
jump_search_button.place(x=700, y=18)
entry_box = Entry(canvas,bd= 4, bg="#333333", fg="#ffffff")
entry_box.place(x=100, y=25)
interpolation_button = Button(canvas, text="interpolitan", command=interpolation, width=10, bg="#222222", fg="#ffffff", state=DISABLED)
interpolation_button.place(x=800, y=18)
exponential_button = Button(canvas, text="exponential" ,command= exponential, width=10, bg="#222222", fg="#ffffff")
exponential_button.place(x=900,y=18)

low_label = Label(canvas, text=low)
low_label.place(x=400, y=1000)
middle_label = Label(canvas, text="0")
middle_label.place(x=450, y=1000)
high_label = Label(canvas, text=high)
high_label.place(x=500, y=1000)
key_label = Label(canvas, text="Key :", bg="#ffffff")
key_label.place(x=68,y=27)
binary_label = Label(canvas,text="0", width=2, bg="#ffffff")
binary_label.place(x=530,y=45)
linear_label = Label(canvas,text="0", width=2, bg="#ffffff")
linear_label.place(x=630,y=45)
jump_label = Label(canvas,text="0", width=2, bg="#ffffff")
jump_label.place(x=730,y=45)
interpolation_label = Label(canvas,text="0", width=2, bg="#ffffff")
interpolation_label.place(x=830,y=45)
exponential_label = Label(canvas,text="0", width=2, bg="#ffffff")
exponential_label.place(x=930,y=45)
window.mainloop()