# main form
import tkinter as tk
from tkinter import *
import py_mainform


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
        self.sec = tk.Button(
            self.master,
            text=" CERRAR SESIÓN ",
            padx=50,
            pady=5,
            fg="black",
            font=("Orbitron", 18),
            width=7,
        )
        self.sec.pack()
        self.sec.place(rely=0.04, relx=0.92, anchor=CENTER)

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
            text=" PROYECTO 1 ",
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
            text=" PROYECTO 2 ",
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
            text=" PROYECTO 3 ",
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

        def scrumsalto():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = py_mainform.sb(scrumwindow)

        self.PY1["command"] = scrumsalto
        self.PY2["command"] = scrumsalto
        self.PY3["command"] = scrumsalto
