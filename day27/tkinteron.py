#Tkinter
from cgitb import text
import tkinter
from tkinter import Button, font, Entry

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
#the window object will scale to include all the objects inside, so if theres nothing inside, it will be very small, so set the minimum width to ensure no matter what it will be at minimu a certain size
window.config(padx=20, pady=20)
#padding
def button_clicked():
    
    user_input = entry_input.get()
    my_label.config(text=user_input)
    print(user_input)

#label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
#pack will grab the component and place it centered on the screen, it is NECESSARY

# inside the pack method you can pass in arguments like side="left", expand="true"

user_input = ''

#add label text
my_label.config(text="Hello?")
my_label.config(padx=50, pady=50)

my_label.grid(column=0, row=0)

#add a button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

entry_input = Entry(width=10)
entry_input.grid(column=3, row=2)

# label, button, entry, text, spinbox, scale, checkbutton, radiobutton, listbox


#Defining layout and positioning
#pack by default just packs things in order, unless you define left or right, but its still not very precise
#place is more precise, by providing an x, y
#grid, is the best option, dividing the ui into rows and columns

#this keeps the window open by maintain a while True loop basically that listens for activity
window.mainloop()