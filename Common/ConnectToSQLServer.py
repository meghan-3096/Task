import pyodbc as pyodbc


class ConnectToSQLServer:

    @staticmethod
    def connect_to_db():
        conn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL server};'
            'Server=HG609G3;'
            'Database=Task;'
            'Trusted_Connection=yes;'
        )

        cursor = conn.cursor()

        return cursor
