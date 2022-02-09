from abc import ABC, abstractmethod
from Tasks.DashboardOperations import DashboardOperations

'''
    Interface Segregation: 
    Clients should not be forced to depend upon interfaces that they do not use.
'''


# Inheritance
class LeadDashboardOperations(DashboardOperations):

    @abstractmethod
    def update(self, member, task_description):
        pass

    @abstractmethod
    def add(self, task_description):
        pass
