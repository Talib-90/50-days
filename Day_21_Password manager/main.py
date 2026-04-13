from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 11))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 3))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 3))]

    passwordList = password_letters + password_symbols + password_numbers
    shuffle(passwordList)

    password = ''.join(passwordList)
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = websiteEntry.get()
    email = user_email_entry.get()
    password = passwordEntry.get()

    new_data = {website:
        {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="don't leave any of the field empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}
        # \nPassword: {password} " f"\nIs it ok to save?") if is_ok:
        try:
            with open("data.json", "r") as file:
                # file.write(f"{website} | {email} | {password}\n")
                # Read older data
                data = json.load(file)
        except FileNotFoundError:
            print("File created.")
            # Saving updated data
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update that data into new data
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)


def findPassword():
    website = websiteEntry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"{website} details not found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)
photoImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photoImage)

canvas.grid(column=1, row=0)

# Website Label
websiteLabel = Label(text="website:")
websiteLabel.grid(column=0, row=1)

# Website Entry
websiteEntry = Entry()
websiteEntry.focus()
websiteEntry.grid(column=1, row=1, sticky="ew")

# User/Email Label
user_email_label = Label(text="Email/Username:")
user_email_label.grid(column=0, row=2)

# User/Email Entry
# user_email_entry = Entry(width=35)
user_email_entry = Entry()
user_email_entry.insert(0, "talib@gmail.com")
# user_email_entry.grid(column=1, row=2, columnspan=2)
user_email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

# Password Label
passwordLabel = Label(text="Password:")
passwordLabel.grid(column=0, row=3)

# Password Entry
# passwordEntry = Entry(width=20)
# passwordEntry.grid(column=1, row=3)
passwordEntry = Entry()
passwordEntry.grid(column=1, row=3, sticky="ew")

# Buttons
generatePassword = Button(text="Generate Password", command=generate_password)
# generatePassword.grid(column=2, row=3, padx=5)
generatePassword.grid(column=2, row=3, sticky="ew")

addButton = Button(text="Add", width=36, command=save)
addButton.grid(column=1, row=4, columnspan=2, sticky="ew")

searchButton = Button(text="Search", command=findPassword)
searchButton.grid(column=2, row=1, sticky="ew")

window.mainloop()
