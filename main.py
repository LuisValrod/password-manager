import tkinter
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []
    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += [choice(numbers) for numb in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password':  password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please, make sure you haven't left any field empty")
    else:
        try:
            with open('data.json', 'r') as data_file:
                #Reading old data
                data = json.load(data_file)
                #Updating with new data
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                #Writing all data
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                #Writing all data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title='Success', message='Information added successfully')

def search():
    web = web_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message="The file with the data doesn't exist. Try to save some data first")
    else:
        if web in data:
            messagebox.showinfo(title='Success',
                                message=f"Website: {web}\n "
                                        f"Email: {data[web]['email']}\n Password: {data[web]['password']}")
        else:
            messagebox.showinfo(title='Oops', message=f"Web {web} not found")
    finally:
        web_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0, padx=0)

#webiste label
web_label = Label(text='Website:', )

#Email/Username label
email_label = Label(text='Email/Username:', )

# Password label
password_label = Label(text='Password:')

# Web Entry
web_entry = Entry(width=30)
web_entry.focus()

#Email Entry
email_entry = Entry(width=51)
email_entry.insert(0,'luisrv@hotmail.com')

# Password Entry
password_entry = Entry(width=30)
password_entry.config()

#Generate Password button
gen_pass  = Button(text='Generate Password', command=generate_password)

# Search Button
search_button = Button(text='Search', width=14, command=search)#
search_button.grid(column=2, row=1, sticky=tkinter.W)

# Add button
add_button = Button(text='Add', width=36, command=save)

web_label.grid(column=0, row=1)
email_label.grid(column=0, row=2, padx=0)
password_label.grid(column=0, row=3, padx=0)
web_entry.grid(column=1, row=1, columnspan=2, sticky=tkinter.W, padx=5)
email_entry.grid(column=1, row=2, columnspan=2, sticky=tkinter.W, padx=5)
password_entry.grid(column=1, row=3, sticky=tkinter.W, padx=5)
gen_pass.grid(column=2, row=3, sticky=tkinter.W)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
