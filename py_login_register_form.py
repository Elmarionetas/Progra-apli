import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox

# import mysql.connector
import psycopg2

user = "fofia"
root = Tk()
# connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='', database='py_lg_rg_db')
# conexion = psycopg2.connect(host='localhost',database='aplicada', user='postgresql', password='Martin123')
connection = psycopg2.connect(
    host="localhost", user="postgres", password="1962", database="SCRUMBASE"
)

root.title("ScrumBase")
root.iconbitmap("s.ico")
root.withdraw
c = connection.cursor()
# c = conexion.cursor()

# width and height
w = root.winfo_screenwidth() - 150
h = root.winfo_screenheight() - 170
# background color
bgcolor = "#ECDAFB"

# ----------- CENTER FORM ------------- #
# root.overrideredirect(1) # remove border
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws - w) / 2
y = (hs - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# ----------- HEADER ------------- #

headerframe = tk.Frame(
    root,
    highlightbackground="#9E91E9",
    highlightcolor="#9E91E9",
    highlightthickness=2,
    bg="#9E91E9",
    width=ws,
    height=70,
)
titleframe = tk.Frame(headerframe, bg="#9E91E9", padx=1, pady=1)
title_label = tk.Label(
    titleframe,
    text=" INICIAR SESIÓN ",
    padx=50,
    pady=5,
    fg="black",
    font=("Orbitron", 25),
    width=10,
)
# close_button = tk.Button(headerframe, text='x', borderwidth=1, relief='solid', font=('Verdana',12))

headerframe.pack()
titleframe.pack()
title_label.pack()
# close_button.pack()

titleframe.place(y=45, relx=0.5, anchor=CENTER)
# close_button.place(x=410, y=10)

# close window
def close_win():
    root.destroy()


# close_button['command'] = close_win

# ----------- END HEADER ------------- #

mainframe = tk.Frame(root, width=w, height=h)

# ----------- Login Page ------------- #

loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(
    loginframe,
    padx=600,
    pady=300,
    highlightbackground="#9E91E9",
    highlightcolor="#9E91E9",
    highlightthickness=30,
    bg=bgcolor,
)

username_label = tk.Label(
    login_contentframe, text="Usuario:", font=("Orbitron", 16), bg=bgcolor
)
password_label = tk.Label(
    login_contentframe, text="Contraseña:", font=("Orbitron", 16), bg=bgcolor
)
username_entry = tk.Entry(login_contentframe, font=("Orbitron", 16))
password_entry = tk.Entry(login_contentframe, font=("Orbitron", 16), show="*")

login_button = tk.Button(
    login_contentframe,
    text="Ingresar",
    font=("Orbitron", 18),
    bg="#9E91E9",
    fg="#fff",
    padx=25,
    pady=10,
    width=25,
)

go_register_label = tk.Label(
    login_contentframe,
    text=">> Baboso, Regístrese",
    font=("Orbitron", 10),
    bg=bgcolor,
    fg="black",
)

mainframe.pack(fill="both", expand=1)
loginframe.pack(fill="both", expand=1)
login_contentframe.pack(fill="both", expand=1)

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
    title_label["text"] = " REGISTRO "
    # title_label['bg'] = '#27ae60'


go_register_label.bind("<Button-1>", lambda page: go_to_register())


# create a function to make the user login
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    globals()["user"] = username
    vals = (
        username,
        password,
    )
    select_query = "SELECT * FROM USUARIOS WHERE username = %s and password = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        # messagebox.showinfo('Test','Test')
        proyectoswindow = tk.Toplevel()
        app = proyectos(proyectoswindow)
        root.withdraw()  # hide the root
        proyectoswindow.protocol("WM_DELETE_WINDOW", close_win)  # close the app

    else:
        messagebox.showwarning("Error", "Usuario o contraseña errada")


login_button["command"] = login


# ----------- Register Page ------------- #

registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(
    registerframe,
    padx=600,
    pady=200,
    highlightbackground="#9E91E9",
    highlightcolor="#9E91E9",
    highlightthickness=30,
    bg=bgcolor,
)

fullname_label_rg = tk.Label(
    register_contentframe, text="Nombre:", font=("Orbitron", 14), bg=bgcolor
)
surname_label_rg = tk.Label(
    register_contentframe, text="Apellido:", font=("Orbitron", 14), bg=bgcolor
)
username_label_rg = tk.Label(
    register_contentframe, text="Usuario:", font=("Orbitron", 14), bg=bgcolor
)
password_label_rg = tk.Label(
    register_contentframe, text="Contraseña:", font=("Orbitron", 14), bg=bgcolor
)
phone_label_rg = tk.Label(
    register_contentframe, text="Teléfono:", font=("Orbitron", 14), bg=bgcolor
)
gender_label_rg = tk.Label(
    register_contentframe, text="Género:", font=("Orbitron", 14), bg=bgcolor
)
email_label_rg = tk.Label(
    register_contentframe, text="Correo:", font=("Orbitron", 14), bg=bgcolor
)
cedula_label_rg = tk.Label(
    register_contentframe, text="Cedula:", font=("Orbitron", 14), bg=bgcolor
)


fullname_entry_rg = tk.Entry(register_contentframe, font=("Orbitron", 14), width=22)
surname_entry_rg = tk.Entry(register_contentframe, font=("Orbitron", 14), width=22)
username_entry_rg = tk.Entry(register_contentframe, font=("Orbitron", 14), width=22)
password_entry_rg = tk.Entry(
    register_contentframe, font=("Orbitron", 14), width=22, show="*"
)
phone_entry_rg = tk.Entry(register_contentframe, font=("Orbitron", 14), width=22)
email_entry_rg = tk.Entry(register_contentframe, font=("Orbitron", 14), width=22)
cedula_entry_rg = tk.Entry(register_contentframe, font=("Orbitron", 14), width=22)


radiosframe = tk.Frame(register_contentframe)
gender = StringVar()
gender.set("Male")
male_radiobutton = tk.Radiobutton(
    radiosframe,
    text="Hombre",
    font=("Orbitron", 14),
    bg=bgcolor,
    variable=gender,
    value="Male",
)
female_radiobutton = tk.Radiobutton(
    radiosframe,
    text="Mujer",
    font=("Orbitron", 14),
    bg=bgcolor,
    variable=gender,
    value="Female",
)


register_button = tk.Button(
    register_contentframe,
    text="Registro",
    font=("Orbitron", 16),
    bg="#9E91E9",
    fg="#fff",
    padx=25,
    pady=10,
    width=25,
)

go_login_label = tk.Label(
    register_contentframe,
    text=">> Inicie sesion con su cuenta ",
    font=("Orbitron", 10),
    bg=bgcolor,
    fg="black",
)

# mainframe.pack(fill='both', expand=1)
# registerframe.pack(fill='both', expand=1)
register_contentframe.pack(fill="both", expand=1)

fullname_label_rg.grid(row=0, column=0, pady=5, sticky="e")
fullname_entry_rg.grid(row=0, column=1)

username_label_rg.grid(row=2, column=0, pady=5, sticky="e")
username_entry_rg.grid(row=2, column=1)

password_label_rg.grid(row=3, column=0, pady=5, sticky="e")
password_entry_rg.grid(row=3, column=1)

surname_label_rg.grid(row=1, column=0, pady=5, sticky="e")
surname_entry_rg.grid(row=1, column=1)

phone_label_rg.grid(row=4, column=0, pady=5, sticky="e")
phone_entry_rg.grid(row=4, column=1)

email_label_rg.grid(row=5, column=0, pady=5, sticky="e")
email_entry_rg.grid(row=5, column=1)

cedula_label_rg.grid(row=6, column=0, pady=5, sticky="e")
cedula_entry_rg.grid(row=6, column=1)

gender_label_rg.grid(row=7, column=0, pady=5, sticky="e")
radiosframe.grid(row=7, column=1)
male_radiobutton.grid(row=0, column=0)
female_radiobutton.grid(row=0, column=1)


register_button.grid(row=8, column=0, columnspan=2, pady=20)

go_login_label.grid(row=9, column=0, columnspan=2, pady=10)


# --------------------------------------- #


# create a function to display the login frame
def go_to_login():
    registerframe.forget()
    loginframe.pack(fill="both", expand=1)
    title_label["text"] = "INICIAR SESIÓN "
    # title_label['bg'] = '#2980b9'


go_login_label.bind("<Button-1>", lambda page: go_to_login())
# --------------------------------------- #

# create a function to check if the username already exists
def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM USUARIOS WHERE username = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False


# --------------------------------------- #


# create a function to register a new user
def register():

    fullname = fullname_entry_rg.get().strip()  # remove white space
    username = username_entry_rg.get().strip()
    password = password_entry_rg.get().strip()
    surname = surname_entry_rg.get().strip()
    email = email_entry_rg.get().strip()
    phone = phone_entry_rg.get().strip()
    gdr = gender.get()
    cedula = cedula_entry_rg.get().strip()

    if (
        len(fullname) > 0
        and len(username) > 0
        and len(password) > 0
        and len(phone) > 0
        and len(email) > 0
    ):
        if check_username(username) == False:
            if password:
                vals = (
                    fullname,
                    username,
                    password,
                    phone,
                    surname,
                    gdr,
                    email,
                    cedula,
                )
                insert_query = "INSERT INTO USUARIOS(fullname, username, password, phone, surname, gender, email, cedula) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo("Enhorabuena", "Tu cuenta ha sido creada")
            else:
                messagebox.showwarning("Contraseña")
        else:
            messagebox.showwarning(
                "Usuario existente", "Este usuario ya esta registrado, intente con otro"
            )
    else:
        messagebox.showwarning("Información incompleta", "Rellene todos los campos")


register_button["command"] = register

# ------------------------------------------------------------------------ #


class sb:
    def __init__(self, master):

        self.master = master
        w = self.master.winfo_screenwidth() - 150
        h = self.master.winfo_screenheight() - 170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws - w) / 2
        y = (hs - h) / 2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar, tearoff=0)
        self.products.add_command(label="Proyectos")
        self.products.add_command(label="Scrum Board")
        self.products.add_command(label="To do")
        self.products.add_command(label="In progres")
        self.products.add_command(label="Done")

        self.menubar.add_cascade(menu=self.products, label="Menu")

        self.frame.pack()

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg="#9E91E9")

        # -------- TITULO -------------- #

        self.header = tk.Frame(
            self.master,
            highlightbackground="#9E91E9",
            highlightcolor="#9E91E9",
            highlightthickness=2,
            bg="#9E91E9",
            width=ws,
            height=70,
        )
        self.titleframe = tk.Frame(self.header, bg="#9E91E9", padx=1, pady=1)
        self.lbl = tk.Label(
            self.titleframe,
            text=" SCRUM BOARD ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 25),
            width=10,
        )
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # -------- TO DO ------------- #

        self.ToDoCua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=450,
            height=800,
        )
        self.ToDoframe = tk.Frame(self.ToDoCua, bg="#9E91E9", padx=1, pady=1)
        self.toDo = tk.Button(
            self.ToDoframe,
            text="TO DO",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.ToDoCua.pack()
        self.ToDoframe.pack()
        self.toDo.pack()
        self.ToDoCua.place(rely=0.52, relx=0.2, anchor=CENTER)
        self.ToDoframe.place(rely=0.06, relx=0.5, anchor=CENTER)

        # ----- IN PROGRESS ------ #

        self.InProCua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=450,
            height=800,
        )
        self.InProframe = tk.Frame(self.InProCua, bg="#9E91E9", padx=1, pady=1)
        self.InPro = tk.Button(
            self.InProframe,
            text="IN PROGRESS",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.InProCua.pack()
        self.InProframe.pack()
        self.InPro.pack()
        self.InProCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.InProframe.place(rely=0.06, relx=0.5, anchor=CENTER)

        # ------- DONE -------- #

        self.DoneCua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=450,
            height=800,
        )
        self.Doneframe = tk.Frame(self.DoneCua, bg="#9E91E9", padx=1, pady=1)
        self.Done = tk.Button(
            self.Doneframe,
            text="DONE",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.DoneCua.pack()
        self.Doneframe.pack()
        self.Done.pack()
        self.DoneCua.place(rely=0.52, relx=0.8, anchor=CENTER)
        self.Doneframe.place(rely=0.06, relx=0.5, anchor=CENTER)

        # ------- VOLVER -------- #

        self.Vl = tk.Button(
            self.master,
            text=" PROYECTOS ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 18),
            width=7,
        )
        self.Vl.pack()
        self.Vl.place(rely=0.04, relx=0.92, anchor=CENTER)

        def scrumsalto():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = todo(scrumwindow)

        self.toDo["command"] = scrumsalto

        def scrumsalto2():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = progress(scrumwindow)

        self.InPro["command"] = scrumsalto2

        def scrumsalto3():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = done(scrumwindow)

        self.Done["command"] = scrumsalto3

        def volver():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = proyectos(scrumwindow)

        self.Vl["command"] = volver


# ------------------------------------------------------------------------ #


class proyectos:
    def __init__(self, master):

        self.master = master
        w = self.master.winfo_screenwidth() - 150
        h = self.master.winfo_screenheight() - 170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws - w) / 2
        y = (hs - h) / 2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ------------------------------ #

        self.master.config(bg="#9E91E9")
        c.execute("select cedula from usuarios where username = %s", (user,))
        ce = c.fetchone()
        c.execute("select proyect from proyectos where cedula = %s", (ce,))
        s = c.fetchall()
        if c.rowcount == 0:
            s1 = "P"
            s2 = "P"
            s3 = "P"
        elif c.rowcount == 1:
            s1 = s[0]
            s2 = "P"
            s3 = "P"
        elif c.rowcount == 2:
            s1 = s[0]
            s2 = s[1]
            s3 = "P"
        elif c.rowcount == 3:
            s1 = s[0]
            s2 = s[1]
            s3 = s[3]            
        print(s)

        # -------- TITULO -------------- #

        self.header = tk.Frame(
            self.master,
            highlightbackground="#9E91E9",
            highlightcolor="#9E91E9",
            highlightthickness=2,
            bg="#9E91E9",
            width=ws,
            height=70,
        )
        self.titleframe = tk.Frame(self.header, bg="#9E91E9", padx=1, pady=1)
        self.lbl = tk.Label(
            self.titleframe,
            text=" PROYECTOS ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 25),
            width=10,
        )
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # ------- PROYECTO 1 --------- #

        self.PY1Cua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=450,
            height=800,
        )
        self.PY1frame = tk.Frame(self.PY1Cua, bg="#9E91E9", padx=1, pady=1)
        self.PY1 = tk.Button(
            self.PY1frame,
            text="\n".join("".join(map(str, tup)) for tup in s1),
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 25),
            width=10,
        )
        self.PY1Cua.pack()
        self.PY1frame.pack()
        self.PY1.pack()
        self.PY1Cua.place(rely=0.52, relx=0.2, anchor=CENTER)
        self.PY1frame.place(rely=0.06, relx=0.5, anchor=CENTER)

        # ------- PROYECTO 2 --------- #

        self.PY2Cua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=450,
            height=800,
        )
        self.PY2frame = tk.Frame(self.PY2Cua, bg="#9E91E9", padx=1, pady=1)
        self.PY2 = tk.Button(
            self.PY2frame,
            text="\n".join("".join(map(str, tup)) for tup in s2),
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 25),
            width=10,
        )
        self.PY2Cua.pack()
        self.PY2frame.pack()
        self.PY2.pack()
        self.PY2Cua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.PY2frame.place(rely=0.06, relx=0.5, anchor=CENTER)

        # ------- PROYECTO 3 -------- #

        self.PY3Cua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=450,
            height=800,
        )
        self.PY3frame = tk.Frame(self.PY3Cua, bg="#9E91E9", padx=1, pady=1)
        self.PY3 = tk.Button(
            self.PY3frame,
            text="\n".join("".join(map(str, tup)) for tup in s3),
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 25),
            width=10,
        )
        self.PY3Cua.pack()
        self.PY3frame.pack()
        self.PY3.pack()
        self.PY3Cua.place(rely=0.52, relx=0.8, anchor=CENTER)
        self.PY3frame.place(rely=0.06, relx=0.5, anchor=CENTER)

        self.sec = tk.Button(
            self.master,
            text=" CERRAR SESIÓN ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 18),
            width=8,
        )
        self.sec.pack()
        self.sec.place(rely=0.04, relx=0.92, anchor=CENTER)

        def scrumsalto():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = sb(scrumwindow)

        def cerrar():
            self.master.destroy()

        self.sec["command"] = cerrar
        self.PY1["command"] = scrumsalto
        self.PY2["command"] = scrumsalto
        self.PY3["command"] = scrumsalto


# ------------------------------------------------------------------------ #


class progress:
    def __init__(self, master):

        self.master = master
        w = self.master.winfo_screenwidth() - 150
        h = self.master.winfo_screenheight() - 170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws - w) / 2
        y = (hs - h) / 2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar, tearoff=0)
        self.products.add_command(label="Proyectos")
        self.products.add_command(label="Scrum Board")
        self.products.add_command(label="To do")
        self.products.add_command(label="In progres")
        self.products.add_command(label="Done")

        self.menubar.add_cascade(menu=self.products, label="Menu")

        self.frame.pack()

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg="#9E91E9")
        
        # -------- TITULO -------------- #

        self.header = tk.Frame(
            self.master,
            highlightbackground="#9E91E9",
            highlightcolor="#9E91E9",
            highlightthickness=2,
            bg="#9E91E9",
            width=ws,
            height=70,
        )
        self.titleframe = tk.Frame(self.header, bg="#9E91E9", padx=1, pady=1)
        self.lbl = tk.Label(
            self.titleframe,
            text=" SCRUM BOARD ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # -------- IN PROGRESS ------------- #

        self.InProCua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=ws - 250,
            height=800,
        )
        self.InProframe = tk.Frame(self.InProCua, bg="#9E91E9", padx=1, pady=1)
        self.InPro = tk.Label(
            self.InProframe,
            text=" PROGRESS ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.InProEspa = tk.Frame(self.InProCua, bg="#9E91E9", padx=1, pady=1)
        self.InProEspa1 = tk.Label(
            self.InProEspa,
            text=" EN PROGRESO 1 ",
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.InProEspa2 = tk.Frame(self.InProCua, bg="#9E91E9", padx=1, pady=1)
        self.InProEspa3 = tk.Label(
            self.InProEspa2,
            text=" EN PROGRESO 2 ",
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.InProCua.pack()
        self.InProframe.pack()
        self.InPro.pack()
        self.InProEspa.pack()
        self.InProEspa1.pack()
        self.InProEspa2.pack()
        self.InProEspa3.pack()
        self.InProCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.InProframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.InProEspa.place(rely=0.4, relx=0.3, anchor=CENTER)
        self.InProEspa2.place(rely=0.4, relx=0.7, anchor=CENTER)

        # ------- VOLVER -------- #

        self.Vl = tk.Button(
            self.master,
            text=" VOLVER ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 18),
            width=7,
        )
        self.Vl.pack()
        self.Vl.place(rely=0.04, relx=0.92, anchor=CENTER)

        def volver():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = sb(scrumwindow)

        self.Vl["command"] = volver


# ------------------------------------------------------------------------ #


class todo:
    def __init__(self, master):

        self.master = master
        w = self.master.winfo_screenwidth() - 150
        h = self.master.winfo_screenheight() - 170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws - w) / 2
        y = (hs - h) / 2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar, tearoff=0)
        self.products.add_command(label="Proyectos")
        self.products.add_command(label="Scrum Board")
        self.products.add_command(label="To do")
        self.products.add_command(label="In progres")
        self.products.add_command(label="Done")

        self.menubar.add_cascade(menu=self.products, label="Menu")

        self.frame.pack()

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg="#9E91E9")

        # -------- TITULO -------------- #

        self.header = tk.Frame(
            self.master,
            highlightbackground="#9E91E9",
            highlightcolor="#9E91E9",
            highlightthickness=2,
            bg="#9E91E9",
            width=ws,
            height=70,
        )
        self.titleframe = tk.Frame(self.header, bg="#9E91E9", padx=1, pady=1)
        self.lbl = tk.Label(
            self.titleframe,
            text=" SCRUM BOARD ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # -------- TO DO ------------- #

        self.ToDoCua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=ws - 250,
            height=800,
        )
        self.ToDoframe = tk.Frame(self.ToDoCua, bg="#9E91E9", padx=1, pady=1)
        self.toDo = tk.Label(
            self.ToDoframe,
            text=" TO DO ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 25),
            width=10,
        )
        self.ToDoEspa = tk.Frame(self.ToDoCua, bg="#9E91E9", padx=1, pady=1)
        self.ToDoEspa1 = tk.Label(
            self.ToDoEspa,
            text="TO DO 1",
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.ToDoEspa2 = tk.Frame(self.ToDoCua, bg="#9E91E9", padx=1, pady=1)
        self.ToDoEspa3 = tk.Label(
            self.ToDoEspa2,
            text="TO DO 2",
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.ToDoCua.pack()
        self.ToDoframe.pack()
        self.toDo.pack()
        self.ToDoEspa.pack()
        self.ToDoEspa1.pack()
        self.ToDoEspa2.pack()
        self.ToDoEspa3.pack()
        self.ToDoCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.ToDoframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.ToDoEspa.place(rely=0.4, relx=0.3, anchor=CENTER)
        self.ToDoEspa2.place(rely=0.4, relx=0.7, anchor=CENTER)

        # ------- VOLVER -------- #

        self.Vl = tk.Button(
            self.master,
            text=" VOLVER ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 18),
            width=7,
        )
        self.Vl.pack()
        self.Vl.place(rely=0.04, relx=0.92, anchor=CENTER)

        def volver():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = sb(scrumwindow)

        self.Vl["command"] = volver


# ------------------------------------------------------------------------ #


class done:
    def __init__(self, master):

        self.master = master
        w = self.master.winfo_screenwidth() - 150
        h = self.master.winfo_screenheight() - 170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws - w) / 2
        y = (hs - h) / 2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        self.products = Menu(self.menubar, tearoff=0)
        self.products.add_command(label="Proyectos")
        self.products.add_command(label="Scrum Board")
        self.products.add_command(label="To do")
        self.products.add_command(label="In progres")
        self.products.add_command(label="Done")

        self.menubar.add_cascade(menu=self.products, label="Menu")

        self.frame.pack()

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg="#9E91E9")

        # -------- TITULO -------------- #

        self.header = tk.Frame(
            self.master,
            highlightbackground="#9E91E9",
            highlightcolor="#9E91E9",
            highlightthickness=2,
            bg="#9E91E9",
            width=ws,
            height=70,
        )
        self.titleframe = tk.Frame(self.header, bg="#9E91E9", padx=1, pady=1)
        self.lbl = tk.Label(
            self.titleframe,
            text=" SCRUM BOARD ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # -------- TERMINADO ------------- #

        self.DoneCua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=ws - 250,
            height=800,
        )
        self.Doneframe = tk.Frame(self.DoneCua, bg="#9E91E9", padx=1, pady=1)
        self.Done = tk.Label(
            self.Doneframe,
            text=" DONE ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.DoneEspa = tk.Frame(self.DoneCua, bg="#9E91E9", padx=1, pady=1)
        self.DoneEspa1 = tk.Label(
            self.DoneEspa,
            text=" TERMINADO 1 ",
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.DoneEspa2 = tk.Frame(self.DoneCua, bg="#9E91E9", padx=1, pady=1)
        self.DoneEspa3 = tk.Label(
            self.DoneEspa2,
            text=" TERMINADO 2 ",
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )
        self.DoneCua.pack()
        self.Doneframe.pack()
        self.Done.pack()
        self.DoneEspa.pack()
        self.DoneEspa1.pack()
        self.DoneEspa2.pack()
        self.DoneEspa3.pack()
        self.DoneCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.Doneframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.DoneEspa.place(rely=0.4, relx=0.3, anchor=CENTER)
        self.DoneEspa2.place(rely=0.4, relx=0.7, anchor=CENTER)

        # ------- VOLVER -------- #

        self.Vl = tk.Button(
            self.master,
            text=" VOLVER ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 18),
            width=7,
        )
        self.Vl.pack()
        self.Vl.place(rely=0.04, relx=0.92, anchor=CENTER)

        def volver():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = sb(scrumwindow)

        self.Vl["command"] = volver


root.mainloop()
