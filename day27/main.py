#miles to Km converted
#type in certain type of miles and receive a converted about of km
#first GUI, MILES to KM converter
from tkinter import Entry, Button, Label, Tk, Text

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

#text entry
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

def miles_km_convert():
    miles_input = float(user_input.get())
    miles_input *= 1.609344
    km_result_label.config(text=round(miles_input, 2))

#labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#calculate button
button = Button(text="Calculate", command=miles_km_convert)
button.grid(column=1, row=2)

window.mainloop()