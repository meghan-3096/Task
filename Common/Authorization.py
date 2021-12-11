from Beans.EmployeeBean import EmployeeBean


class Authorization:

    def __init__(self, role):
        self.role = role

    def operations_authorized(self):

        if self.role == 'Team Lead':
            operations = ["delete", "update", "exit"]
        else:
            operations = ["mark done", "exit"]

        return operations
