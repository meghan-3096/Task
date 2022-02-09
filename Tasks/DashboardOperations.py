from abc import ABC, abstractmethod
from Tasks.TaskDetails import TaskDetails

'''
    Open-Close Principle: Objects or entities should be open for extension but closed for modification.
'''


# Demonstrating Abstraction
class DashboardOperations(ABC, TaskDetails):

    def __init__(self, name, task_id=(-1), operation_id=(-1)):
        self.name = name
        self.task_id = (task_id - 1)
        self.operation_id = operation_id

    @abstractmethod
    def delete(self, member, task_id):
        pass

    @abstractmethod
    def view(self):
        pass

    '''@abstractmethod
    def delete_sf(self, member, task_id):
        pass

    @abstractmethod
    def view_sf(self):
        pass
'''