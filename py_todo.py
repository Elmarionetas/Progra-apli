# main form
import tkinter as tk
from tkinter import *

class todo:

    def __init__(self, master):
        
        self.master = master
        w = self.master.winfo_screenwidth()-150
        h = self.master.winfo_screenheight()-170
        # ----------- CENTER FORM ------------- #
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
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

        self.header = tk.Frame (self.master, highlightbackground='#9E91E9', highlightcolor='#9E91E9', highlightthickness=2, bg='#9E91E9', width=ws, height=70)
        self.titleframe = tk.Frame(self.header, bg='#9E91E9', padx=1, pady=1)
        self.lbl = tk.Label(self.titleframe, text=' SCRUM BOARD ', padx=50, pady=5, fg='black', font=('Orbitron',25), width=10)
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)

        # -------- TO DO ------------- #

        self.ToDoCua =tk.Frame (self.master, highlightbackground='#ECDAFB', highlightcolor='#ECDAFB', highlightthickness=2, bg='#ECDAFB', width=ws-250, height=800)
        self.ToDoframe = tk.Frame (self.ToDoCua, bg='#9E91E9', padx=1, pady=1)
        self.toDo = tk.Label (self.ToDoframe, text= ' TO DO ', padx=50, pady=5, fg='black', font=('Orbitron',25), width=10)
        self.ToDoCua.pack()
        self.ToDoframe.pack()
        self.toDo.pack()
        self.ToDoCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.ToDoframe.place(rely=0.06, relx=0.5, anchor=CENTER)
