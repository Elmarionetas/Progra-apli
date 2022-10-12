import tkinter as tk 
from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
#import mysql.connector
from py_mainform import mainform
import psycopg2

root = Tk()
#connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='', database='py_lg_rg_db')
#conexion = psycopg2.connect(host='localhost',database='aplicada', user='postgresql', password='Martin123')
connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1962',
        database='aplicada'
    )

c = connection.cursor()
#c = conexion.cursor()

# width and height
w = root.winfo_screenwidth()-150
h = root.winfo_screenheight()-170
# background color
bgcolor = "#ECDAFB"

# ----------- CENTER FORM ------------- #
#root.overrideredirect(1) # remove border
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# ----------- HEADER ------------- #

headerframe = tk.Frame(root, highlightbackground='#9E91E9', highlightcolor='#9E91E9', highlightthickness=2, bg='#9E91E9', width=ws, height=70)
titleframe = tk.Frame(headerframe, bg='#9E91E9', padx=1, pady=1)
title_label = tk.Label(titleframe, text=' INICIAR SESIÓN ', padx=50, pady=5, fg='black', font=('Orbitron',25), width=10)
#close_button = tk.Button(headerframe, text='x', borderwidth=1, relief='solid', font=('Verdana',12))

headerframe.pack()
titleframe.pack()
title_label.pack()
#close_button.pack()

titleframe.place(y=45, relx=0.5, anchor=CENTER)
#close_button.place(x=410, y=10)

# close window
def close_win():
    root.destroy()

#close_button['command'] = close_win

# ----------- END HEADER ------------- #

mainframe = tk.Frame(root, width=w, height=h)

# ----------- Login Page ------------- #
loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(loginframe, padx=600, pady=300, highlightbackground='#9E91E9', highlightcolor='#9E91E9', highlightthickness=30, bg=bgcolor)

username_label = tk.Label(login_contentframe, text='Usuario:', font=('Orbitron',16), bg=bgcolor)
password_label = tk.Label(login_contentframe, text='Contraseña:', font=('Orbitron',16), bg=bgcolor)

username_entry = tk.Entry(login_contentframe, font=('Orbitron',16))
password_entry = tk.Entry(login_contentframe, font=('Orbitron',16), show='*')

login_button = tk.Button(login_contentframe,text="Ingresar", font=('Orbitron',18), bg='#9E91E9',fg='#fff', padx=25, pady=10, width=25)

go_register_label = tk.Label(login_contentframe, text=">> Baboso, Regístrese" , font=('Orbitron',10), bg=bgcolor, fg='black')

#------------FALTAAAAAAAAAAAAAAAAAAAAA---------------#

mainframe.pack(fill='both', expand=1)
loginframe.pack(fill='both', expand=1)
login_contentframe.pack(fill='both', expand=1)

username_label.grid(row=0, column=0, pady=10)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0, pady=10)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, column=0, columnspan=2, pady=40)

go_register_label.grid(row=3, column=0, columnspan=2, pady=20)

# create a function to display the register frame
def go_to_register():
    loginframe.forget()
    registerframe.pack(fill="both", expand=1)
    title_label['text'] = ' REGISTRO '
    #title_label['bg'] = '#27ae60'


go_register_label.bind("<Button-1>", lambda page: go_to_register())


# create a function to make the user login
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    vals = (username, password,)
    select_query = "SELECT * FROM users WHERE username = %s and password = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        #messagebox.showinfo('Test','Test')
        mainformwindow = tk.Toplevel()
        app = mainform(mainformwindow)
        root.withdraw() # hide the root
        mainformwindow.protocol("WM_DELETE_WINDOW", close_win) # close the app

    else:
        messagebox.showwarning('Error','Usuario o contraseña errada')



login_button['command'] = login


# ----------- Register Page ------------- #

registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(registerframe, padx=600, pady=200, highlightbackground='#9E91E9', highlightcolor='#9E91E9', highlightthickness=30, bg=bgcolor)

fullname_label_rg = tk.Label(register_contentframe, text='Nombre:', font=('Orbitron',14), bg=bgcolor)
surname_label_rg = tk.Label(register_contentframe, text='Apellido:', font=('Orbitron',14), bg=bgcolor)
username_label_rg = tk.Label(register_contentframe, text='Usuario:', font=('Orbitron',14), bg=bgcolor)
password_label_rg = tk.Label(register_contentframe, text='Contraseña:', font=('Orbitron',14), bg=bgcolor)
phone_label_rg = tk.Label(register_contentframe, text='Teléfono:', font=('Orbitron',14), bg=bgcolor)
gender_label_rg = tk.Label(register_contentframe, text='Género:', font=('Orbitron',14), bg=bgcolor)
email_label_rg = tk.Label(register_contentframe, text='Correo:', font=('Orbitron',14), bg=bgcolor)



fullname_entry_rg = tk.Entry(register_contentframe, font=('Orbitron',14), width=22)
surname_entry_rg = tk.Entry(register_contentframe, font=('Orbitron',14), width=22)
username_entry_rg = tk.Entry(register_contentframe, font=('Orbitron',14), width=22)
password_entry_rg = tk.Entry(register_contentframe, font=('Orbitron',14), width=22, show='*')
phone_entry_rg = tk.Entry(register_contentframe, font=('Orbitron',14), width=22)
email_entry_rg = tk.Entry(register_contentframe, font=('Orbitron', 14), width=22)



radiosframe = tk.Frame(register_contentframe)
gender = StringVar()
gender.set('Male')
male_radiobutton = tk.Radiobutton(radiosframe, text='Hombre', font=('Orbitron',14), bg=bgcolor, variable=gender, value='Male')
female_radiobutton = tk.Radiobutton(radiosframe, text='Mujer', font=('Orbitron',14), bg=bgcolor, variable=gender, value='Female')


register_button = tk.Button(register_contentframe,text="Registro", font=('Orbitron',16), bg='#9E91E9',fg='#fff', padx=25, pady=10, width=25)

go_login_label = tk.Label(register_contentframe, text=">> Inicie sesion con su cuenta " , font=('Orbitron',10), bg=bgcolor, fg='black')

#mainframe.pack(fill='both', expand=1)
#registerframe.pack(fill='both', expand=1)
register_contentframe.pack(fill='both', expand=1)

fullname_label_rg.grid(row=0, column=0, pady=5, sticky='e')
fullname_entry_rg.grid(row=0, column=1)

username_label_rg.grid(row=2, column=0, pady=5, sticky='e')
username_entry_rg.grid(row=2, column=1)

password_label_rg.grid(row=3, column=0, pady=5, sticky='e')
password_entry_rg.grid(row=3, column=1)

surname_label_rg.grid(row=1, column=0, pady=5, sticky='e')
surname_entry_rg.grid(row=1, column=1)

phone_label_rg.grid(row=4, column=0, pady=5, sticky='e')
phone_entry_rg.grid(row=4, column=1)

email_label_rg.grid(row=5, column=0, pady=5, sticky='e')
email_entry_rg.grid(row=5, column=1)

gender_label_rg.grid(row=6, column=0, pady=5, sticky='e')
radiosframe.grid(row=6, column=1)
male_radiobutton.grid(row=0, column=0)
female_radiobutton.grid(row=0, column=1)


register_button.grid(row=7, column=0, columnspan=2, pady=20)

go_login_label.grid(row=8, column=0, columnspan=2, pady=10)


# --------------------------------------- #


# create a function to display the login frame
def go_to_login():
    registerframe.forget()
    loginframe.pack(fill="both", expand=1)
    title_label['text'] = 'INICIAR SESIÓN '
    #title_label['bg'] = '#2980b9'


go_login_label.bind("<Button-1>", lambda page: go_to_login())
# --------------------------------------- #

# create a function to check if the username already exists
def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM users WHERE username = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False



# --------------------------------------- #


# create a function to register a new user
def register():

    fullname = fullname_entry_rg.get().strip() # remove white space
    username = username_entry_rg.get().strip()
    password = password_entry_rg.get().strip()
    surname = surname_entry_rg.get().strip()
    email = email_entry_rg.get().strip()
    phone = phone_entry_rg.get().strip()
    gdr = gender.get()
    
    

    if len(fullname) > 0 and  len(username) > 0 and len(password) > 0 and len(phone) > 0:
        if check_username(username) == False: 
            if password:
                vals = (fullname, username, password, phone, surname, gdr, email)
                insert_query = "INSERT INTO users(fullname, username, password, phone, surname, gender, email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo('Enhorabuena','Tu cuenta ha sido creada')
            else:
                messagebox.showwarning('Contraseña')
        else:
            messagebox.showwarning('Usuario existente','Este usuario ya esta registrado, intente con otro')
    else:
        messagebox.showwarning('Información incompleta','Rellene todos los campos')

register_button['command'] = register

# --------------------------------------- #

# ------------------------------------------------------------------------ #

root.mainloop()