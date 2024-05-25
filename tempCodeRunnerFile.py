def listbox_used(event):

    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)

fruits = ["Apple", "Pear", "Orange", "Banana"]

for fruit in fruits:

    listbox.insert(fruits.index(fruit), fruit)

listbox.bind("<<ListboxSelect>>", listbox_used)

listbox.pack()