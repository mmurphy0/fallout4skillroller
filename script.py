import sys, random
import tkinter as tk
from tkinter import messagebox, Toplevel

num = []
i = 0
for i in range(28):
    i = i + 1
    num.append(i)

def exiting():
    messagebox.showinfo('Goodbye!','Thanks for using the Fallout 4 Skill Roller')
    sys.exit()

def home():
    strength = random.choice(num)
    perception = random.choice(num)
    endurance = random.choice(num)
    charisma = random.choice(num)
    intelligence = random.choice(num)
    agility = random.choice(num)
    luck = random.choice(num)
    
    roll_gui = Toplevel()
    roll_gui.title('Skill Roller')
    roll_gui.geometry('200x310')
    roll_gui.minsize(200,310)
    roll_gui.maxsize(200,310)

    s_label = tk.Label(
        roll_gui,
        text=(f'S -> {strength}'),
        font=('Arial',30),
        fg='Green'
    )
    s_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    p_label = tk.Label(
        roll_gui,
        text=(f'P -> {perception}'),
        font=('Arial',30),
        fg='Green'
    )
    p_label.grid(
        row=2,
        column=1,
        columnspan=2
    )

    e_label = tk.Label(
        roll_gui,
        text=(f'E -> {endurance}'),
        font=('Arial',30),
        fg='Green'
    )
    e_label.grid(
        row=3,
        column=1,
        columnspan=2
    )

    c_label = tk.Label(
        roll_gui,
        text=(f'C -> {charisma}'),
        font=('Arial',30),
        fg='Green'
    )
    c_label.grid(
        row=4,
        column=1,
        columnspan=2
    )

    i_label = tk.Label(
        roll_gui,
        text=(f'I -> {intelligence}'),
        font=('Arial',30),
        fg='Green'
    )
    i_label.grid(
        row=5,
        column=1,
        columnspan=2
    )

    a_label = tk.Label(
        roll_gui,
        text=(f'A -> {agility}'),
        font=('Arial',30),
        fg='Green'
    )
    a_label.grid(
        row=6,
        column=1,
        columnspan=2
    )

    l_label = tk.Label(
        roll_gui,
        text=(f'L -> {luck}'),
        font=('Arial',30),
        fg='Green'
    )
    l_label.grid(
        row=7,
        column=1,
        columnspan=2
    )

    back_button = tk.Button(
        roll_gui,
        text='Back',
        font=('Arial'),
        fg='Green',
        width=20,
        command=roll_gui.destroy
    )
    back_button.grid(
        row=8,
        column=1,
        columnspan=2
    )

root = tk.Tk()
root.title('Welcome')
root.geometry('215x90')
root.minsize(215,90)
root.maxsize(215,90)

root_title = tk.Label(
    root,
    text='Fallout 4 Skill Roller',
    font=('Arial',15),
    fg='Green'
)
root_title.grid(
    row=1,
    column=1,
    columnspan=2
)

start_button = tk.Button(
    root,
    text='Start',
    width=20,
    fg='Green',
    command=home
)
start_button.grid(
    row=2,
    column=1,
    columnspan=2
)

exit_button = tk.Button(
    root,
    text='Exit',
    width=20,
    fg='Green',
    command=exiting
)
exit_button.grid(
    row=3,
    column=1,
    columnspan=2
)

root.mainloop()