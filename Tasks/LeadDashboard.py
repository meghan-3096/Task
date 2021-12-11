from Tasks.TaskDetails import TaskDetails
from Tasks.DashboardOperations import DashboardOperations

# Demonstrating Inheritance and Polymorphism


class LeadDashboard(DashboardOperations, TaskDetails):

    def update(self, member, task_description):
        task_list = self._allTasks
        print(f'Task for {member.upper()} before Update: {task_list.get(member.upper())}')
        self._allTasks.get(member.upper()).append(task_description)
        print(f'Task updated for {member.upper()}')
        print(f'Task for {member.upper()} after Update: {task_list.get(member.upper())}')
        print(task_list)

    def delete(self, member, task_id):
        task_list = self._allTasks
        print(f'Task for {member.upper()} before deletion: {task_list.get(member.upper())}')
        self._allTasks.get(member.upper()).pop(task_id)
        print(f'Task deleted for {member.upper()}')
        print(f'Task for {member.upper()} after deletion: {task_list.get(member.upper())}')

    def view(self):
        tasks = self._allTasks
        return tasks
