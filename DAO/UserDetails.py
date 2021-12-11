from Common.ConnectToSQLServer import ConnectToSQLServer


class Userdetails:

    def __init__(self):
        pass

    def get_employee_details(user):
        cursor = ConnectToSQLServer.connect_to_db()

        query = f'SELECT * FROM Task.dbo.userdetails WHERE username = {user}'
        cursor.execute(query)

        return cursor
