from tkinter import *
from  tkinter import messagebox
from random import randint, choice , shuffle

from pyperclip  import copy #pyperclip will copy immediately your new generated password, so that you can easily paste it on the website you need it
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pass_generator():



    password_letters = [choice(letters) for char in range( randint(8,10))]
    password_numbers = [choice(numbers) for num in range(randint(2,4))]
    password_symbols= [choice(symbols) for symbol in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)


    password_text =''.join(password_list)
    password_entry.insert(0,password_text)
    #copy in order to paste it rapidly on website entry
    copy(password_text)

# ---------------------------- SAVE PASSWORD ------------------------------- #

#add button function
def save():
    #get what is written in entry boxes

    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()


    #empty pop up

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title='Oops', message="Please don't leave any field empty!")
    else:
        #savings pop up
        is_ok = messagebox.askokcancel(title = website_text,message = f'These are the details entered:'
                                                          f'\n Website: {website_text}\n '
                                                          f'Email/Username : {username_text}\n'
                                                          f' Password: {password_text}\n'
                                                          f'Is it ok to save?')

        if is_ok:
            #save it
            with open('data.txt','a') as password_file:
                password_file.write(f'{website_text} | {username_text} | {password_text} \n')
                #delete it
                website_entry.delete(0,END)
                username_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx= 50,pady= 50)

#lock
canvas = Canvas(width = 200,height = 200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image( 100, 100,image = lock_img)
canvas.grid(column = 1,row = 0)





#labels
website_label = Label(text='Website:')
website_label.grid(column= 0,row = 1)

user_label = Label(text='Email/Username:')
user_label.grid(column= 0,row=2)

pass_label = Label(text='Password:')
pass_label.grid(column= 0 ,row=3)

#entry
#Entry
website_entry = Entry(width = 42)
website_entry.grid(column = 1,row=1,columnspan=2)
website_entry.focus()




username_entry = Entry(width=42)
username_entry.grid(column= 1, row=2, columnspan= 2)
username_entry.insert(0,'highair-sketch@yahoo.io')



password_entry = Entry(width= 25)
password_entry.grid(column= 1, row= 3)

#button
generator_pass_button = Button(text='Generate Password', width= 16,command = pass_generator)
generator_pass_button.grid(column = 2, row=3)


add_button = Button(text= 'Add',width= 42, command = save )
add_button.grid(column= 1,row=4,columnspan= 2)

window.mainloop()
