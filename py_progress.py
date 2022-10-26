# main form
import tkinter as tk
from tkinter import *
import py_mainform


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
            app = py_mainform.sb(scrumwindow)

        self.Vl["command"] = volver
