from model import Model

class Controller:

    def Connect(self,database):
        self.columns = {}
        self.table_data = {}
        self.model = Model(database)
        self.tables = self.model.Get_Tables()
        for table in self.tables:
            self.columns[table] = self.model.Get_Table_Columns(table)
        for table in self.tables:
            self.data = self.model.Read(table)
            self.table_data[table] = self.data
        self.Redirect(1)

    def Set_views(self,views):
        self.views = views

    def Get_data(self):
        for i in self.tables:
            self.data = self.model.Read(i)
            self.table_data[i] = self.data
        return self.tables, self.table_data, self.columns

    def Redirect(self,view_index):
        self.current_view=self.views[view_index]
        self.current_view.Display()

    def Refresh(self):
        self.Get_data(self.current_table)
