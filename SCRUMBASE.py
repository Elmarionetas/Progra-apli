import tkinter as tk
from tkinter import *  # type: ignore
from tkinter import ttk
from tkinter.ttk import *  # type: ignore
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font
import numpy as np

import psycopg2

user = "fofia"
tppy = "NUMERO DE PROYECTO"
root = Tk()
connection = psycopg2.connect(
    host="localhost", user="postgres", password="1962", database="SCRUMBASE"
)

root.title("ScrumBase")
root.iconbitmap("s.ico")
root.withdraw
c = connection.cursor()

# width and height
w = root.winfo_screenwidth() - 150
h = root.winfo_screenheight() - 170
# background color
bgcolor = "#ECDAFB"

# ----------- CENTER FORM ------------- #

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

headerframe.pack()
titleframe.pack()
title_label.pack()

titleframe.place(y=45, relx=0.5, anchor=CENTER)

# close window
def close_win():
    root.destroy()


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
    text=">> Registrarse ",
    font=("Orbitron", 12),
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
        app = py(proyectoswindow)
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
    font=("Orbitron", 12),
    bg=bgcolor,
    fg="black",
)


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


class py:
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

        def scrumsalto():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = sb(scrumwindow)

        def pyidget(f):
            globals()["tppy"] = f

        # -------- PROYECTOS ----------- #

        c.execute("select cedula from usuarios where username = %s", (user,))
        ce = c.fetchone()

        c.execute(
            "select proyect from proyectos where cedula = %s and pyid = %s", (ce, 1)
        )
        s1 = c.fetchall()
        c.execute(
            "select proyect from proyectos where cedula = %s and pyid = %s", (ce, 2)
        )
        s2 = c.fetchall()
        c.execute(
            "select proyect from proyectos where cedula = %s and pyid = %s", (ce, 3)
        )
        s3 = c.fetchall()

        c.execute("select proyect from proyectos where cedula = %s", (ce,))

        s = "PARA PONER EL NOMBRE DEL PROYECTO"
        suno = "PARA PONER EL NOMBRE DEL PROYECTO CUANDO HAY +"
        pyids = "PARA ID DEL PROYECTO "
        pyidsuno = "PARA ID DEL PROYECTO CUANDO HAY +"

        if c.rowcount == 0:

            # ------- SIN PROYECTOS --------- #

            self.PYCua = tk.Frame(
                self.master,
                highlightbackground="#ECDAFB",
                highlightcolor="#ECDAFB",
                highlightthickness=2,
                bg="#ECDAFB",
                width=1300,
                height=750,
            )
            self.PYframe = tk.Frame(self.PYCua, bg="#9E91E9", padx=1, pady=1)
            self.PY = tk.Label(
                self.PYframe,
                text="NO PROYECTOS \n ASIGNADOS",
                padx=200,
                pady=20,
                fg="black",
                font=("Orbitron", 50),
                width=10,
            )
            self.PYCua.pack()
            self.PYframe.pack()
            self.PY.pack()
            self.PYCua.place(rely=0.55, relx=0.5, anchor=CENTER)
            self.PYframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # ------- UN PROYECTO --------- #

        elif c.rowcount == 1:

            # ------- PROYECTO 1 --------- #

            if s1:
                s = s1
                pyids = 1
            elif s2:
                s = s2
                pyids = 2
            elif s3:
                s = s3
                pyids = 3

            self.PY1Cua = tk.Frame(
                self.master,
                highlightbackground="#ECDAFB",
                highlightcolor="#ECDAFB",
                highlightthickness=2,
                bg="#ECDAFB",
                width=800,
                height=800,
            )

            self.PY1frame = tk.Frame(self.PY1Cua, bg="#9E91E9", padx=1, pady=1)
            self.PY1 = tk.Button(
                self.PY1frame,
                text="\n".join("".join(map(str, tup)) for tup in s),
                padx=120,
                pady=5,
                fg="black",
                font=("Orbitron", 20),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (1, ce, pyids),
            )

            todo = c.fetchall()
            self.todo = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in todo),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (2, ce, pyids),
            )

            inpro = c.fetchall()
            self.inpro = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in inpro),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (3, ce, pyids),
            )

            done = c.fetchall()
            self.done = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in done),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            self.PY1Cua.pack()
            self.PY1frame.pack()
            self.PY1.pack()
            self.todo.pack()
            self.inpro.pack()
            self.done.pack()
            self.PY1Cua.place(rely=0.52, relx=0.5, anchor=CENTER)
            self.PY1frame.place(rely=0.07, relx=0.5, anchor=CENTER)
            self.todo.place(rely=0.3, relx=0.5, anchor=CENTER)
            self.inpro.place(rely=0.5, relx=0.5, anchor=CENTER)
            self.done.place(rely=0.7, relx=0.5, anchor=CENTER)

            self.PY1["command"] = lambda: [pyidget(pyids), scrumsalto()]

        # ------- DOS PROYECTOS --------- #

        elif c.rowcount == 2:

            # ------- PROYECTO 1 --------- #

            if s1:
                suno = s1
                pyidsuno = 1
            elif s2:
                suno = s2
                pyidsuno = 2

            self.PY1Cua = tk.Frame(
                self.master,
                highlightbackground="#ECDAFB",
                highlightcolor="#ECDAFB",
                highlightthickness=2,
                bg="#ECDAFB",
                width=600,
                height=800,
            )

            self.PY1frame = tk.Frame(self.PY1Cua, bg="#9E91E9", padx=1, pady=1)
            self.PY1 = tk.Button(
                self.PY1frame,
                text="\n".join("".join(map(str, tup)) for tup in suno),
                padx=120,
                pady=5,
                fg="black",
                font=("Orbitron", 20),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (1, ce, pyidsuno),
            )

            todo = c.fetchall()
            self.todo = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in todo),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (2, ce, pyidsuno),
            )

            inpro = c.fetchall()
            self.inpro = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in inpro),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (3, ce, pyidsuno),
            )

            done = c.fetchall()
            self.done = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in done),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            self.PY1Cua.pack()
            self.PY1frame.pack()
            self.PY1.pack()
            self.todo.pack()
            self.inpro.pack()
            self.done.pack()
            self.PY1Cua.place(rely=0.52, relx=0.3, anchor=CENTER)
            self.PY1frame.place(rely=0.07, relx=0.5, anchor=CENTER)
            self.todo.place(rely=0.3, relx=0.5, anchor=CENTER)
            self.inpro.place(rely=0.5, relx=0.5, anchor=CENTER)
            self.done.place(rely=0.7, relx=0.5, anchor=CENTER)

            self.PY1["command"] = lambda: [pyidget(pyidsuno), scrumsalto()]

            # ------- PROYECTO 2 --------- #

            if s3:
                s = s3
                pyids = 3
            elif s2:
                s = s2
                pyids = 2

            self.PY2Cua = tk.Frame(
                self.master,
                highlightbackground="#ECDAFB",
                highlightcolor="#ECDAFB",
                highlightthickness=2,
                bg="#ECDAFB",
                width=600,
                height=800,
            )

            self.PY2frame = tk.Frame(self.PY2Cua, bg="#9E91E9", padx=1, pady=1)
            self.PY2 = tk.Button(
                self.PY2frame,
                text="\n".join("".join(map(str, tup)) for tup in s),
                padx=120,
                pady=5,
                fg="black",
                font=("Orbitron", 20),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (1, ce, pyids),
            )

            todo = c.fetchall()
            self.todo = tk.Label(
                self.PY2Cua,
                text="\n".join("".join(map(str, tup)) for tup in todo),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (2, ce, pyids),
            )

            inpro = c.fetchall()
            self.inpro = tk.Label(
                self.PY2Cua,
                text="\n".join("".join(map(str, tup)) for tup in inpro),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (3, ce, pyids),
            )

            done = c.fetchall()
            self.done = tk.Label(
                self.PY2Cua,
                text="\n".join("".join(map(str, tup)) for tup in done),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            self.PY2Cua.pack()
            self.PY2frame.pack()
            self.PY2.pack()
            self.todo.pack()
            self.inpro.pack()
            self.done.pack()
            self.PY2Cua.place(rely=0.52, relx=0.7, anchor=CENTER)
            self.PY2frame.place(rely=0.07, relx=0.5, anchor=CENTER)
            self.todo.place(rely=0.3, relx=0.5, anchor=CENTER)
            self.inpro.place(rely=0.5, relx=0.5, anchor=CENTER)
            self.done.place(rely=0.7, relx=0.5, anchor=CENTER)

            self.PY2["command"] = lambda: [pyidget(pyids), scrumsalto()]

        # ------- TRES PROYECTOS --------- #

        elif c.rowcount == 3:

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
                padx=100,
                pady=5,
                fg="black",
                font=("Orbitron", 20),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (1, ce, 1),
            )

            todo = c.fetchall()
            self.todo = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in todo),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (2, ce, 1),
            )

            inpro = c.fetchall()
            self.inpro = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in inpro),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (3, ce, 1),
            )

            done = c.fetchall()
            self.done = tk.Label(
                self.PY1Cua,
                text="\n".join("".join(map(str, tup)) for tup in done),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            self.PY1Cua.pack()
            self.PY1frame.pack()
            self.PY1.pack()
            self.todo.pack()
            self.inpro.pack()
            self.done.pack()
            self.PY1Cua.place(rely=0.52, relx=0.2, anchor=CENTER)
            self.PY1frame.place(rely=0.07, relx=0.5, anchor=CENTER)
            self.todo.place(rely=0.3, relx=0.5, anchor=CENTER)
            self.inpro.place(rely=0.5, relx=0.5, anchor=CENTER)
            self.done.place(rely=0.7, relx=0.5, anchor=CENTER)

            self.PY1["command"] = lambda: [pyidget(1), scrumsalto()]

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
                padx=100,
                pady=5,
                fg="black",
                font=("Orbitron", 20),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (1, ce, 2),
            )

            todo = c.fetchall()
            self.todo = tk.Label(
                self.PY2Cua,
                text="\n".join("".join(map(str, tup)) for tup in todo),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (2, ce, 2),
            )

            inpro = c.fetchall()
            self.inpro = tk.Label(
                self.PY2Cua,
                text="\n".join("".join(map(str, tup)) for tup in inpro),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (3, ce, 2),
            )

            done = c.fetchall()
            self.done = tk.Label(
                self.PY2Cua,
                text="\n".join("".join(map(str, tup)) for tup in done),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            self.PY2Cua.pack()
            self.PY2frame.pack()
            self.PY2.pack()
            self.todo.pack()
            self.inpro.pack()
            self.done.pack()
            self.PY2Cua.place(rely=0.52, relx=0.5, anchor=CENTER)
            self.PY2frame.place(rely=0.07, relx=0.5, anchor=CENTER)
            self.todo.place(rely=0.3, relx=0.5, anchor=CENTER)
            self.inpro.place(rely=0.5, relx=0.5, anchor=CENTER)
            self.done.place(rely=0.7, relx=0.5, anchor=CENTER)

            self.PY2["command"] = lambda: [pyidget(2), scrumsalto()]

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
                padx=100,
                pady=5,
                fg="black",
                font=("Orbitron", 20),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (1, ce, 3),
            )
            todo = c.fetchall()

            self.todo = tk.Label(
                self.PY3Cua,
                text="\n".join("".join(map(str, tup)) for tup in todo),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (2, ce, 3),
            )
            inpro = c.fetchall()

            self.inpro = tk.Label(
                self.PY3Cua,
                text="\n".join("".join(map(str, tup)) for tup in inpro),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            c.execute(
                "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
                (3, ce, 3),
            )
            done = c.fetchall()

            self.done = tk.Label(
                self.PY3Cua,
                text="\n".join("".join(map(str, tup)) for tup in done),
                padx=100,
                pady=10,
                fg="black",
                font=("Orbitron", 15),
                width=10,
            )

            self.PY3Cua.pack()
            self.PY3frame.pack()
            self.PY3.pack()
            self.todo.pack()
            self.inpro.pack()
            self.done.pack()
            self.PY3Cua.place(rely=0.53, relx=0.8, anchor=CENTER)
            self.PY3frame.place(rely=0.07, relx=0.5, anchor=CENTER)
            self.todo.place(rely=0.3, relx=0.5, anchor=CENTER)
            self.inpro.place(rely=0.5, relx=0.5, anchor=CENTER)
            self.done.place(rely=0.7, relx=0.5, anchor=CENTER)

            self.PY3["command"] = lambda: [pyidget(3), scrumsalto()]

        # ------- CERRAR SESIÓN -------- #

        self.sec = tk.Button(
            self.master,
            text=" CERRAR SESIÓN ",
            padx=55,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=8,
        )
        self.sec.pack()
        self.sec.place(rely=0.045, relx=0.915, anchor=CENTER)

        def cerrar():
            self.master.destroy()

        self.sec["command"] = cerrar

        # ------- ADMINISTRAR PROYECTOS -------- #

        self.proy = tk.Button(
            self.master,
            text=" ADMINISTRAR PROYECTOS ",
            padx=135,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=8,
        )
        self.proy.pack()
        self.proy.place(rely=0.045, relx=0.13, anchor=CENTER)

        def proyectos():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = modicrea(scrumwindow)

        self.proy["command"] = proyectos


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

        # ------------------------------ #

        self.master.config(bg="#9E91E9")
        self.master.iconbitmap("s.ico")

        c.execute("select cedula from usuarios where username = %s", (user,))
        ce = c.fetchone()

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

        c.execute(
            "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
            (1, ce, tppy),
        )

        todotx = c.fetchall()
        self.todolb = tk.Label(
            self.ToDoCua,
            text="\n".join("".join(map(str, tup)) for tup in todotx),
            padx=100,
            pady=300,
            fg="black",
            font=("Orbitron", 15),
            width=10,
        )

        self.ToDoCua.pack()
        self.ToDoframe.pack()
        self.toDo.pack()
        self.todolb.pack()
        self.ToDoCua.place(rely=0.52, relx=0.2, anchor=CENTER)
        self.ToDoframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.todolb.place(rely=0.55, relx=0.5, anchor=CENTER)

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

        c.execute(
            "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
            (2, ce, tppy),
        )

        inprotx = c.fetchall()
        self.inprolb = tk.Label(
            self.InProCua,
            text="\n".join("".join(map(str, tup)) for tup in inprotx),
            padx=100,
            pady=300,
            fg="black",
            font=("Orbitron", 15),
            width=10,
        )

        self.InProCua.pack()
        self.InProframe.pack()
        self.InPro.pack()
        self.inprolb.pack()
        self.InProCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.InProframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.inprolb.place(rely=0.55, relx=0.5, anchor=CENTER)

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

        c.execute(
            "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
            (3, ce, tppy),
        )

        donetx = c.fetchall()
        self.donelb = tk.Label(
            self.DoneCua,
            text="\n".join("".join(map(str, tup)) for tup in donetx),
            padx=100,
            pady=300,
            fg="black",
            font=("Orbitron", 15),
            width=10,
        )

        self.DoneCua.pack()
        self.Doneframe.pack()
        self.Done.pack()
        self.donelb.pack()
        self.DoneCua.place(rely=0.52, relx=0.8, anchor=CENTER)
        self.Doneframe.place(rely=0.06, relx=0.5, anchor=CENTER)
        self.donelb.place(rely=0.55, relx=0.5, anchor=CENTER)

        # ------- ADMINISTRAR TAREAS -------- #

        self.proy = tk.Button(
            self.master,
            text=" ADMINISTRAR TAREAS ",
            padx=135,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=8,
        )
        self.proy.pack()
        self.proy.place(rely=0.045, relx=0.13, anchor=CENTER)

        def proyectos():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = modicreatk(scrumwindow)

        self.proy["command"] = proyectos

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
            app = py(scrumwindow)

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

        # ------------------------------ #

        self.master.config(bg="#9E91E9")
        self.master.iconbitmap("s.ico")

        c.execute("select cedula from usuarios where username = %s", (user,))
        ce = c.fetchone()

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

        c.execute(
            "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
            (1, ce, tppy),
        )
        todo = c.fetchall()

        if c.rowcount == 1:
            s = todo[0]
            s1 = "NO"
        elif c.rowcount == 2:
            s = todo[0]
            s1 = todo[1]
        else:
            s = "NO"
            s1 = "NO"

        self.ToDoEspa = tk.Frame(self.ToDoCua, bg="#9E91E9", padx=1, pady=1)
        self.ToDoEspa1 = tk.Label(
            self.ToDoEspa,
            text="\n".join("".join(map(str, tup)) for tup in s),
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.ToDoEspa2 = tk.Frame(self.ToDoCua, bg="#9E91E9", padx=1, pady=1)
        self.ToDoEspa3 = tk.Label(
            self.ToDoEspa2,
            text="\n".join("".join(map(str, tup)) for tup in s1),
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

        # ------------------------------ #

        self.master.config(bg="#9E91E9")
        self.master.iconbitmap("s.ico")

        c.execute("select cedula from usuarios where username = %s", (user,))
        ce = c.fetchone()

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

        c.execute(
            "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
            (2, ce, tppy),
        )
        inpro = c.fetchall()

        if c.rowcount == 1:
            s = inpro[0]
            s1 = "NO"
        elif c.rowcount == 2:
            s = inpro[0]
            s1 = inpro[1]
        else:
            s = "NO"
            s1 = "NO"

        self.InProEspa = tk.Frame(self.InProCua, bg="#9E91E9", padx=1, pady=1)
        self.InProEspa1 = tk.Label(
            self.InProEspa,
            text="\n".join("".join(map(str, tup)) for tup in s),
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.InProEspa2 = tk.Frame(self.InProCua, bg="#9E91E9", padx=1, pady=1)
        self.InProEspa3 = tk.Label(
            self.InProEspa2,
            text="\n".join("".join(map(str, tup)) for tup in s1),
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

        # ------------------------------ #

        self.master.config(bg="#9E91E9")
        self.master.iconbitmap("s.ico")

        c.execute("select cedula from usuarios where username = %s", (user,))
        ce = c.fetchone()

        # ---------- TITULO ------------ #

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

        c.execute(
            "select tarea from tareas where estado = %s and cedula = %s and pyid = %s",
            (3, ce, tppy),
        )
        done = c.fetchall()

        if c.rowcount == 1:
            s = done[0]
            s1 = "NO"
        elif c.rowcount == 2:
            s = done[0]
            s1 = done[1]
        else:
            s = "NO"
            s1 = "NO"

        self.DoneEspa = tk.Frame(self.DoneCua, bg="#9E91E9", padx=1, pady=1)
        self.DoneEspa1 = tk.Label(
            self.DoneEspa,
            text="\n".join("".join(map(str, tup)) for tup in s),
            padx=150,
            pady=150,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.DoneEspa2 = tk.Frame(self.DoneCua, bg="#9E91E9", padx=1, pady=1)
        self.DoneEspa3 = tk.Label(
            self.DoneEspa2,
            text="\n".join("".join(map(str, tup)) for tup in s1),
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


# ------------------------------------------------------------------------ #


class modicrea:
    def __init__(self, master):

        # ----------- Register Page ------------- #
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
        self.master.iconbitmap("s.ico")

        # -------- TITULO -------------- #

        self.Pycua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=ws - 230,
            height=700,
        )

        self.titleframe = tk.Frame(self.master, bg="#9E91E9", padx=1, pady=1)
        self.lbl = tk.Label(
            self.titleframe,
            text="ADMINISTRAR PROYECTOS",
            padx=150,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.framepy = tk.Frame(self.Pycua, bg="#9E91E9", padx=1, pady=1)
        self.lbpy = tk.Label(
            self.framepy,
            text="Proyecto: ",
            padx=10,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.py_entry = tk.Text(self.Pycua, font=("Orbitron", 14))

        self.frameusu = tk.Frame(self.Pycua, bg="#9E91E9", padx=1, pady=1)
        self.lbusu = tk.Label(
            self.frameusu,
            text="Usuario: ",
            padx=10,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        c.execute("select username from usuarios")
        usuarios = c.fetchall()
        for n in range(0, c.rowcount):
            self.usuario = ttk.Combobox(
                self.Pycua,
                values=usuarios[0] + usuarios[n],
                font=Font(size=15),
                state="readonly",
            )

        self.frameid = tk.Frame(self.Pycua, bg="#9E91E9", padx=1, pady=1)
        self.lbid = tk.Label(
            self.frameid,
            text="ID proyecto: ",
            padx=10,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.pyidlista = ttk.Combobox(
            self.Pycua, values=["1", "2", "3"], font=Font(size=15), state="readonly"
        )

        self.boton = tk.Button(
            self.Pycua,
            text="Guardar",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.dele = tk.Button(
            self.Pycua,
            text="Eliminar Proyecto",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.titleframe.pack()
        self.lbl.pack()
        self.Pycua.pack()
        self.framepy.pack()
        self.lbpy.pack()
        self.py_entry.pack()
        self.frameusu.pack()
        self.lbusu.pack()
        self.frameid.pack()
        self.lbid.pack()
        self.usuario.pack()
        self.boton.pack()
        self.dele.pack()
        self.pyidlista.pack()
        self.titleframe.place(rely=0.05, relx=0.5, anchor=CENTER)
        self.Pycua.place(rely=0.5, relx=0.5, anchor=CENTER)
        self.framepy.place(rely=0.38, relx=0.1, anchor=CENTER)
        self.py_entry.place(rely=0.45, relx=0.36, anchor=CENTER, width=600, height=150)
        self.frameusu.place(rely=0.23, relx=0.1, anchor=CENTER)
        self.frameid.place(rely=0.23, relx=0.42, anchor=CENTER)
        self.usuario.place(rely=0.23, relx=0.25, anchor=CENTER)
        self.pyidlista.place(rely=0.23, relx=0.57, anchor=CENTER)
        self.boton.place(rely=0.7, relx=0.3, anchor=CENTER)
        self.dele.place(rely=0.7, relx=0.7, anchor=CENTER)

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

        def volver():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = py(scrumwindow)

        self.Vl["command"] = volver

        def guardar():
            usupy = self.usuario.get()
            c.execute("select cedula from usuarios where username = %s", (usupy,))
            cepy = c.fetchone()
            c.execute("select pyid from proyectos where cedula = %s", (cepy,))
            pyid = np.array(c.fetchall())
            pyidnm = int(self.pyidlista.get())
            textopy = self.py_entry.get("1.0", "end-1c")
            if pyidnm not in pyid:
                c.execute(
                    "insert into proyectos(cedula,proyect,pyid) values (%s,%s,%s)",
                    (cepy, textopy, pyidnm),
                )
                connection.commit()
                messagebox.showinfo("CONFIRMACION", "Proyecto Guardado")
            else:
                c.execute(
                    "update proyectos set proyect = %s where pyid = %s and cedula = %s",
                    (textopy, pyidnm, cepy),
                )
                connection.commit()
                messagebox.showinfo("CONFIRMACION", "Proyecto Actualizado")
            self.py_entry.delete(0.0, END)

        self.boton["command"] = guardar

        def rellenarcuadro(event):
            usupy = self.usuario.get()
            c.execute("select cedula from usuarios where username = %s", (usupy,))
            cepy = c.fetchone()
            c.execute("select pyid from proyectos where cedula = %s", (cepy,))
            pyid = np.array(c.fetchall())
            pyidnm = int(self.pyidlista.get())
            c.execute("select proyect from proyectos where pyid  = %s", (pyidnm,))
            text = c.fetchall()
            if pyidnm in pyid:
                self.py_entry.delete(0.0, END)
                self.py_entry.insert(
                    tk.END, "\n".join("".join(map(str, tup)) for tup in text[0])
                )
            else:
                self.py_entry.delete(0.0, END)

        self.pyidlista.bind("<<ComboboxSelected>>", rellenarcuadro)

        def eliminar():
            usupy = self.usuario.get()
            c.execute("select cedula from usuarios where username = %s", (usupy,))
            cepy = c.fetchone()
            c.execute("select pyid from proyectos where cedula = %s", (cepy,))
            pyid = np.array(c.fetchall())
            pyidnm = int(self.pyidlista.get())
            if pyidnm in pyid:
                c.execute(
                    "delete from proyectos where pyid = %s and cedula = %s",
                    (
                        pyidnm,
                        cepy,
                    ),
                )
                c.execute(
                    "delete from tareas where pyid = %s and cedula = %s",
                    (
                        pyidnm,
                        cepy,
                    ),
                )
                connection.commit()
                messagebox.showinfo("CONFIRMACION", "Proyecto Eliminado")
            else:
                messagebox.showinfo("CONFIRMACION", "Proyecto No Existe")
            self.py_entry.delete(0.0, END)

        self.dele["command"] = eliminar


# ------------------------------------------------------------------------ #


class modicreatk:
    def __init__(self, master):

        # ----------- Register Page ------------- #
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

        # -------- TITULO -------------- #

        self.Pycua = tk.Frame(
            self.master,
            highlightbackground="#ECDAFB",
            highlightcolor="#ECDAFB",
            highlightthickness=2,
            bg="#ECDAFB",
            width=ws - 200,
            height=700,
        )

        self.titleframe = tk.Frame(self.master, bg="#9E91E9", padx=1, pady=1)
        self.lbl = tk.Label(
            self.titleframe,
            text="ADMINISTRAR TAREAS",
            padx=150,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.framepy = tk.Frame(self.Pycua, bg="#9E91E9", padx=1, pady=1)
        self.lbpy = tk.Label(
            self.framepy,
            text="Tarea: ",
            padx=10,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.py_entry = tk.Text(self.Pycua, font=("Orbitron", 14))

        self.frameusu = tk.Frame(self.Pycua, bg="#9E91E9", padx=1, pady=1)
        self.lbusu = tk.Label(
            self.frameusu,
            text="Usuario: ",
            padx=10,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        c.execute("select username from usuarios where username = %s", (user,))
        usuarios = c.fetchall()
        print(usuarios)

        self.usuario = ttk.Combobox(
            self.Pycua,
            values=usuarios[0],
            font=Font(size=15),
            state="readonly",
        )

        self.frameid = tk.Frame(self.Pycua, bg="#9E91E9", padx=1, pady=1)
        self.lbid = tk.Label(
            self.frameid,
            text="Estado Tarea: ",
            padx=10,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.pyidlista = ttk.Combobox(
            self.Pycua, values=["1", "2", "3"], font=Font(size=15), state="readonly"
        )

        self.boton = tk.Button(
            self.Pycua,
            text="Guardar",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.dele = tk.Button(
            self.Pycua,
            text="Eliminar Tarea",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 20),
            width=10,
        )

        self.titleframe.pack()
        self.lbl.pack()
        self.Pycua.pack()
        self.framepy.pack()
        self.lbpy.pack()
        self.py_entry.pack()
        self.frameusu.pack()
        self.lbusu.pack()
        self.frameid.pack()
        self.lbid.pack()
        self.usuario.pack()
        self.boton.pack()
        self.dele.pack()
        self.pyidlista.pack()
        self.titleframe.place(rely=0.05, relx=0.5, anchor=CENTER)
        self.Pycua.place(rely=0.5, relx=0.5, anchor=CENTER)
        self.framepy.place(rely=0.38, relx=0.1, anchor=CENTER)
        self.py_entry.place(rely=0.45, relx=0.36, anchor=CENTER, width=600, height=150)
        self.frameusu.place(rely=0.23, relx=0.1, anchor=CENTER)
        self.frameid.place(rely=0.23, relx=0.42, anchor=CENTER)
        self.usuario.place(rely=0.23, relx=0.25, anchor=CENTER)
        self.pyidlista.place(rely=0.23, relx=0.57, anchor=CENTER)
        self.boton.place(rely=0.7, relx=0.3, anchor=CENTER)
        self.dele.place(rely=0.7, relx=0.7, anchor=CENTER)

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

        def guardar():
            usupy = self.usuario.get()
            c.execute("select cedula from usuarios where username = %s", (usupy,))
            cepy = c.fetchone()
            c.execute("select tarea from tareas where cedula = %s", (cepy,))
            tareatx = c.fetchall()
            estadotr = int(self.pyidlista.get())
            textopy = self.py_entry.get("1.0", "end-1c")
            if textopy not in tareatx:
                c.execute(
                    "insert into tareas(cedula,tarea,pyid,estado) values (%s,%s,%s,%s)",
                    (cepy, textopy, tppy, estadotr),
                )
                connection.commit()
                messagebox.showinfo("CONFIRMACION", "Tarea Guardado")
            else:
                c.execute(
                    "update tareas set tarea = %s where estado = %s and cedula = %s and pyid = %s",
                    (textopy, estadotr, cepy, tppy),
                )
                connection.commit()
                messagebox.showinfo("CONFIRMACION", "Tarea Actualizado")
            self.py_entry.delete(0.0, END)

        self.boton["command"] = guardar

        def rellenarcuadro(event):
            usupy = self.usuario.get()
            c.execute("select cedula from usuarios where username = %s", (usupy,))
            cepy = c.fetchone()
            c.execute("select tarea from tareas where cedula = %s", (cepy,))
            tareatx = np.array(c.fetchall())
            estadotr = int(self.pyidlista.get())
            c.execute(
                "select tarea from tareas where pyid  = %s and cedula = %s and estado = %s",
                (tppy, cepy, estadotr),
            )
            text = c.fetchall()
            if text in tareatx:
                self.py_entry.insert(
                    tk.END, "\n".join("".join(map(str, tup)) for tup in text)
                )
            else:
                self.py_entry.delete(0.0, END)

        self.pyidlista.bind("<<ComboboxSelected>>", rellenarcuadro)

        def eliminar():
            usupy = self.usuario.get()
            c.execute("select cedula from usuarios where username = %s", (usupy,))
            cepy = c.fetchone()
            c.execute("select tarea from tareas where cedula = %s", (cepy,))
            tareatx = np.array(c.fetchall())
            textopy = self.py_entry.get("1.0", "end-1c")
            if textopy in tareatx:
                c.execute(
                    "delete from tareas where tarea = %s and cedula = %s",
                    (
                        textopy,
                        cepy,
                    ),
                )
                connection.commit()
                messagebox.showinfo("CONFIRMACION", "Tarea Eliminada")
            else:
                messagebox.showinfo("CONFIRMACION", "Tarea No Existe")
            self.py_entry.delete(0.0, END)

        self.dele["command"] = eliminar


root.mainloop()
