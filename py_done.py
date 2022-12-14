# main form
import tkinter as tk
from tkinter import *
import py_mainform


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

        # -------- TO DO ------------- #

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
            app = py_mainform.sb(scrumwindow)

        self.Vl["command"] = volver
