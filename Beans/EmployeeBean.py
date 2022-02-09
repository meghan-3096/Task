"""
    Single Responsibility Principle:
    A class should have one and only one reason to change, meaning that a class should have only one job.

    EmployeeBean class deals with the operations and attributes related to user input details only
"""


# Demonstrating Encapsulation
class EmployeeBean:
    __role = 'Team Member'

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        if self.__username.upper() == 'HARRY':
            self.__role = 'Team Lead'

    def get_role(self):
        return self.__role

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
