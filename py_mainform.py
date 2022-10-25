# main form
import tkinter as tk
from tkinter import *
from py_todo import todo
from py_progress import progress
from py_done import done
import py_mainformpro

class sb:

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
        self.Vl = tk.Button (self.master, text= ' PROYECTOS ', padx=50, pady=5, fg='black', font=('Orbitron',18), width=7)
        self.header.pack()
        self.titleframe.pack()
        self.lbl.pack()
        self.Vl.pack()
        self.titleframe.place(rely=0.5, relx=0.5, anchor=CENTER)
        self.Vl.place(rely=0.04, relx=0.92, anchor=CENTER)

        # -------- TO DO ------------- #

        self.ToDoCua =tk.Frame (self.master, highlightbackground='#ECDAFB', highlightcolor='#ECDAFB', highlightthickness=2, bg='#ECDAFB', width=450, height=800)
        self.ToDoframe = tk.Frame (self.ToDoCua, bg='#9E91E9', padx=1, pady=1)
        self.toDo = tk.Button (self.ToDoframe, text= 'TO DO', padx=50, pady=5, fg='black', font=('Orbitron',20), width=10)
        self.ToDoCua.pack()
        self.ToDoframe.pack()
        self.toDo.pack()
        self.ToDoCua.place(rely=0.52, relx=0.2, anchor=CENTER)
        self.ToDoframe.place(rely=0.06, relx=0.5, anchor=CENTER)

        # ----- IN PROGRESS ------ #

        self.InProCua =tk.Frame (self.master, highlightbackground='#ECDAFB', highlightcolor='#ECDAFB', highlightthickness=2, bg='#ECDAFB', width=450, height=800)
        self.InProframe = tk.Frame (self.InProCua, bg='#9E91E9', padx=1, pady=1)
        self.InPro = tk.Button (self.InProframe, text= 'IN PROGRESS', padx=50, pady=5, fg='black', font=('Orbitron',20), width=10)
        self.InProCua.pack()
        self.InProframe.pack()
        self.InPro.pack()
        self.InProCua.place(rely=0.52, relx=0.5, anchor=CENTER)
        self.InProframe.place(rely=0.06, relx=0.5, anchor=CENTER)

        # ------- DONE -------- #

        self.DoneCua =tk.Frame (self.master, highlightbackground='#ECDAFB', highlightcolor='#ECDAFB', highlightthickness=2, bg='#ECDAFB', width=450, height=800)
        self.Doneframe = tk.Frame (self.DoneCua, bg='#9E91E9', padx=1, pady=1)
        self.Done = tk.Button (self.Doneframe, text= 'DONE', padx=50, pady=5, fg='black', font=('Orbitron',20), width=10)
        self.DoneCua.pack()
        self.Doneframe.pack()
        self.Done.pack()
        self.DoneCua.place(rely=0.52, relx=0.8, anchor=CENTER)
        self.Doneframe.place(rely=0.06, relx=0.5, anchor=CENTER)

        def scrumsalto():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = todo(scrumwindow)
        
        self.toDo['command'] = scrumsalto

        def scrumsalto2():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = progress(scrumwindow)
        
        self.InPro['command'] = scrumsalto2

        def scrumsalto3():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = done(scrumwindow)
        
        self.Done['command'] = scrumsalto3

        def volver():
            scrumwindow = tk.Toplevel()
            self.master.withdraw()
            app = py_mainformpro.proyectos(scrumwindow)

        self.Vl['command'] = volver