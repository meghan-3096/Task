from Common.ConnectToSF import ConnectToSF


class Authentication:

    usernames = {"HARRY", "RON", "GINNY", "FRED", "GEORGE"}

    def __init__(self, username, password):
        self.__username = username.upper()
        self.__password = password

    def is_authentic(self):
        for name in self.usernames:
            if self.__username.upper() == name:
                if self.__password == 'password':
                    return True
                else:
                    return False
            else:
                continue

    '''def if_authentic(self, employee: EmployeeBean):
        user_details = DataAccess(employee)
        names = user_details
        for name in names:
            if self.__username.upper() == name:
                if self.__password == 'password':
                    return True
                else:
                    return False
            else:
                continue
        '''

    def is_valid(self):
        cursor = ConnectToSF.connect_snowflake()

        query = f"SELECT username, password FROM TASK.PUBLIC.TEAM " \
                f"WHERE username='{self.__username}' AND password='{self.__password}';"
        cursor.execute(query)

        if cursor.rowcount == 0:
            return False
        else:
            return True
