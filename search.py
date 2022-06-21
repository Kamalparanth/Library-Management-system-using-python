from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error


class Sea(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Book")
        self.maxsize(800,500)
        self.minsize(800,500)
    
        l1=Label(self,text="Search Books",font=("Algerian",20,'bold')).place(x=290,y=20)
        l = Label(self, text="Search By", font=("Arial", 15, 'bold')).place(x=60, y=96)
        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], 'Available' if row[2] == 1 else 'Unavailable',row[3],row[5]))
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+g.get())
            elif g.get() == 'Book Name':
                try:
                    self.conn = sqlite3.connect('Bookstore.db')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from Book_details where B_name LIKE ?",['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
            elif g.get() == 'Author Name':
                try:
                    self.conn = sqlite3.connect('Bookstore.db')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from Book_details where author_name LIKE ?", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Author Name not found")
                except Error:
                    messagebox.showerror("Error","Something goes wrong")
          
        b=Button(self,text="Find",width=15,font=("Arial",10,'bold'),command=ge).place(x=460,y=148)
        c=ttk.Combobox(self,textvariable=g,values=["Book Name","Author Name"],width=40,state="readonly").place(x = 180, y = 100)
        en = Entry(self,textvariable=f,width=43).place(x=180,y=155)
        la = Label(self, text="Enter", font=("Arial", 15, 'bold')).place(x=100, y=150)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Availability','Edition','price'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading('#0',text='Book Name',anchor='center')
        self.listTree.column('#0', width=100, anchor='center')
        self.listTree.heading('#1', text='Book Author',anchor='center')
        self.listTree.column("#1", width=100, anchor='center')
        self.listTree.heading("#2", text='Availability')
        self.listTree.column("#2", width=100, anchor='center')
        self.listTree.heading("#3", text='Edition')
        self.listTree.column("#3", width=100, anchor='center')
        self.listTree.heading("#4", text='price')
        self.listTree.column("#4", width=100, anchor='center')
        self.listTree.bind('<Button-1>', handle)
        self.listTree.place(x=20, y=200)
        self.vsb.place(x=750,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

Sea().mainloop()
