from Common.ConnectToSQLServer import ConnectToSQLServer
from Common.ConnectToSF import ConnectToSF


class UserDAO:


    def get_userdetails_SQL(self, username):
        cursor = ConnectToSQLServer.connect_to_db()

        query = f"SELECT * FROM Task.dbo.userdetails WHERE username = '{username}';"
        cursor.execute(query)

        return cursor


    def get_userdata(self, username):
        cursor = ConnectToSF.connect_snowflake()

        query = f"SELECT * FROM TASK.PUBLIC.TEAM WHERE username = '{username}';"
        cursor.execute(query)

        return cursor

    def get_usernames(self):
        cursor = ConnectToSF.connect_snowflake()

        query = f"SELECT USERNAME FROM TASK.PUBLIC.TEAM;"
        cursor.execute(query)

        usernames = cursor.fetch_pandas_all()['USERNAME']

        return usernames
