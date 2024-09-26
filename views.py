import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from random import choice

class Select(ctk.CTkFrame):
    view_index = 0

    def __init__(self,parent):
        super().__init__(parent)

        self.db_string = ctk.StringVar()
        self.table_string = ctk.StringVar()

        self.db_label = ctk.CTkLabel(master = self,text="Filename")
        self.db_entry = ctk.CTkEntry(self,textvariable=self.db_string)
        self.connect_btn = ctk.CTkButton(master=self,text = "Connect",command = self.Connect)

        self.db_label.pack()
        self.db_entry.pack()
        self.connect_btn.pack()

        self.Display()

    def Set_Connect(self,connect):
        self.Connect_Func= connect

    def Set_Redirect(self,redirect):
        self.redirect = redirect

    def Display(self):
        self.pack()

    def Redirect(self,view_index):
        self.redirect(1)

    def Connect(self):
        self.Connect_Func(self.db_string.get())


class View_Data(ctk.CTkFrame):
    view_index = 1

    def __init__(self,parent):
        super().__init__(parent)
        self.file_name = ctk.CTkLabel(master=self,text="File name")
        self.file_name.pack()
        self.refresh_btn = ctk.CTkButton(master=self,text="Refresh",command = self.Refresh_Table)
        self.refresh_btn.pack()

    def Set_Get_Data(self,get_data):
        self.get_data = get_data

    def Set_Refresh(self,refresh):
        self.refresh = refresh

    def Set_Redirect(self,redirect):
        self.redirect = redirect

    def Set_Switch(self,switch):
        self.switch_table = switch

    def Build_Table(self):
        # get data
        self.tabs = ctk.CTkTabview(master=self,anchor="nw")

        for table in self.tables:
            self.tabs.add(table)
        self.tabs.pack()

        #Create tables
        for table in self.tables:
            tableFrame = ctk.CTkScrollableFrame(master = self.tabs.tab(table),width=500,orientation="horizontal")
            cols = tuple(self.columns[table])
            self.table = ttk.Treeview(master = tableFrame,columns=cols,show = "headings")
            for col in self.columns[table]:
                self.table.heading(col, text =col)
            self.table.pack()
            tableFrame.pack()

        #Insert data
            for data in self.table_data[table]:
                self.table.insert(parent="",index = tk.END, values = data)

    def Display(self):
        # Get data
        # Build Table
        self.tables, self.table_data,self.columns = self.get_data()
        self.Build_Table()
        self.pack()

    def Redirect(self,view_index):
        self.redirect(view_index)

    def Refresh_Table(self):
        #self.refresh()
        self.tabs.pack_forget()
        self.Display()

