import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

# Label

my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))

my_label.pack()

# Button

def button_clicked():

    print("I got clicked")

button = tk.Button(text="Click Me", command=button_clicked)

button.pack()

# Entry

input = tk.Entry(width=10)

input.pack()

# Text

text = tk.Text(height=5, width=30)

text.pack()

# Spinbox

def spinbox_used():

    print(spinbox.get())

spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)

spinbox.pack()

# Scale

def scale_used(value):

    print(value)

scale = tk.Scale(from_=0, to=100, command=scale_used)

scale.pack()

# Checkbutton

def checkbutton_used():

    print(checked_state.get())

checked_state = tk.IntVar()

checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)

checkbutton.pack()

# Radiobutton

def radio_used():

    print(radio_state.get())

radio_state = tk.IntVar()

radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)

radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()

radiobutton2.pack()

# Listbox

def listbox_used(event):

    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)

fruits = ["Apple", "Pear", "Orange", "Banana"]

for fruit in fruits:

    listbox.insert(fruits.index(fruit), fruit)

listbox.bind("<<ListboxSelect>>", listbox_used)

listbox.pack()

window.mainloop()