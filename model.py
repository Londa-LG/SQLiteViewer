import sqlite3

class Model:
    def __init__(self,database):
        self.connection = sqlite3.Connection(database)
        self.cursor = self.connection.cursor()

    def Create(self):
        pass

    def Read(self,table):
        data = self.cursor.execute(f"""
            SELECT * FROM {table}
        """)
        return data.fetchall()

    def Get_Tables(self):
        tables = self.cursor.execute("""
            SELECT GROUP_CONCAT(NAME,',')
            FROM sqlite_master
            WHERE type="table";
        """)
        return tables.fetchone()[0].split(',')

    def Get_Table_Columns(self,table):
        columns = self.cursor.execute(f"""
            SELECT GROUP_CONCAT(NAME,',')
            FROM pragma_table_info('{table}');
        """)
        return columns.fetchone()[0].split(',')

    def Update(self):
        pass

    def Delete(self):
        pass

    def Exit(self):
        self.connection.close()
