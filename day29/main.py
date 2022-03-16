#mypass password manager
from cgitb import text
import random
from tkinter import *
from tkinter import messagebox
import pyperclip

RED = "#e7305b"
GREEN = "#9bdeac"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ["!", '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    #this new list, will get a random letter from letters, middle section doesn't matter, certain amount of times based on the range, so either 8, 9 or 10 letters
    password_letters = [random.choice(letters) for letter in range(num_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(num_symbols)]
    password_numbers = [random.choice(numbers) for number in range(num_numbers)]
    
    final_pass = password_letters + password_symbols + password_numbers
    random.shuffle(final_pass)

    password = ''
    for char in final_pass:
        password += str(char)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    confirm_and_pyper_label.config(text="Password copied to clipboard!", fg=RED)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#take the inputs from each entry, when Add is clicked, save the data into a file called data.txt

def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    
    if not website or not email or not password:
        messagebox.showinfo(title="ERROR", message="One or more inputs are missing (website, email or password)")
        # messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \n Password: {password} \n Is it okay to save?")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \n Password: {password} \n Is it okay to save?")

        if is_okay:

            file = open("day29/data.txt", "a")
            file.write(f"{website} | {email} | {password} \n")
            file.close()

            confirm_and_pyper_label.config(text="Details saved!", fg="green")

            website_entry.delete(0, END)
            # email_username_entry.delete(0, END)
            password_entry.delete(0, END)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

my_pass_img = PhotoImage(file="day29/mypass.png")

canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_username_entry = Entry()
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_username_entry.insert(0, "chris.burns006@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1, columnspan=1, sticky="EW")

generate_password_button = Button(text="Generate Password", command=pass_gen)
generate_password_button.grid(row=3, column=2, sticky="EW")
add_password = Button(text="Add", command=save_password)
add_password.grid(row=4, column=1, columnspan=2, sticky="EW")

confirm_and_pyper_label = Label(text="")
confirm_and_pyper_label.grid(row=5, column=1, sticky="EW")

# confirm_label = Label(text="", fg=GREEN)
# confirm_label.grid(row=6, column=1, sticky="EW")

window.mainloop()