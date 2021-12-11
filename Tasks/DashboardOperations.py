from abc import ABC, abstractmethod
from Tasks.TaskDetails import TaskDetails


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

    def update(self, member, task_description):
        pass
