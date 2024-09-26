import customtkinter as ctk
from controller import Controller
from views import (
    Select,
    View_Data
)

class App(ctk.CTk):
    def __init__(self):
        # Window
        super().__init__()
        self.title("Database viewer")
        self.geometry("550x450")
        ctk.set_appearance_mode("dark")

        views = []
        v1 = Select(self)
        v2 = View_Data(self)
        ctr = Controller()

        v1.Set_Connect(ctr.Connect)
        v1.Set_Redirect(ctr.Redirect)
        v2.Set_Refresh(ctr.Connect)
        v2.Set_Redirect(ctr.Redirect)
        v2.Set_Get_Data(ctr.Get_data)
        views.append(v1)
        views.append(v2)
        ctr.Set_views(views)

        self.mainloop()

if __name__ == "__main__":
    App()
