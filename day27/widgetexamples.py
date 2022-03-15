import tkinter
from tkinter import END, Button, Radiobutton, Spinbox, font, Entry, Text, Scale, Checkbutton, IntVar, Listbox

from setuptools import Command

window = tkinter.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=300)

#input box
user_input = Entry(width=10)
user_input.pack()

#create a button
def button_used():
    print("clicked")
button = Button(text="Click Me", command=button_used)
button.pack()

#create a text box
text = Text(height=5, width=30)

#add a focus outline to text
text.focus()
text.pack()
#add text
text.insert(END, "Example of a multi-line text entry!")

#Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to_=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)

scale = Scale(from_=1, to_=100, command=scale_used)
scale.pack()

#checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
# here we use the bind method, and pass in the listbox_used function as a call back, so anytime something is selected it will call the function
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()