from Common.ConnectToSQLServer import ConnectToSQLServer


class Authentication:

    usernames = {"HARRY", "RON", "GINNY", "FRED", "GEORGE"}

    def __init__(self, username, password):
        self.__username = username
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

    def if_authentic(self):
        pass


