from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.grid(column=1, row=1,columnspan=2, sticky="ew")

# Email/Username Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

# password Entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

# Generate password button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

root.mainloop()
