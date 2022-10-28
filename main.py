from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list += random.choice(symbols)

for char in range(nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Writing data to file
    website_name = website_entry.get()
    email_id = email_entry.get()
    user_password = password_entry.get()

    if len(website_name) == 0 or len(email_id) == 0 or len(user_password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty!")
        # messagebox.showerror(title="Oops", message="Please don't leave any of the fields empty!")
        # messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered, Please verify:"
                                                                   f"\n Email ID: {email_id}\nPassword: {user_password} ")

        if is_ok:
            with open("user_file.txt", mode="a") as file:
                file.write(f"{website_name} | {email_id} | {user_password}\n")

            # Clearing data after clicking add button
            website_entry.delete(0, END)     # Deleting from 0 means start to END= "end" for that entry
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

key_image = PhotoImage(file="logo.png")

root.iconphoto(False, key_image)

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=key_image)
canvas.grid(column=1, row=0)

# Label Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Label Email/username
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# label Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Website entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()        # Will make cursor appear in the box when program starts

# Email/Username Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "myemail@gamail.com")

# password Entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

# Generate password button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

root.mainloop()
