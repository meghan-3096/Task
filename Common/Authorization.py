class Authorization:

    def __init__(self, role):
        self.role = role

    def operations_authorized(self):

        if self.role == 'Team Lead':
            operations = {1: "delete", 2: "update", 3: "exit"}
        else:
            operations = {1: "mark done", 2: "exit"}

        return operations
