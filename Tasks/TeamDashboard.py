from Tasks.DashboardOperations import DashboardOperations
from Tasks.TaskDetails import TaskDetails


class TeamDashboard(DashboardOperations, TaskDetails):

    def view(self):
        tasks = self._allTasks.get(self.name.upper())
        return tasks

    def delete(self, member, task_id):
        self._allTasks.get(member.upper()).pop(task_id)
        print('Task Marked Done')
        print(f'Pending Tasks: {self._allTasks.get(member.upper())}')
