from Tasks.TaskDetails import TaskDetails
from Tasks.LeadDashboardOperations import LeadDashboardOperations
from DAO.DashboardDAO import DashboardDAO


# Demonstrating Inheritance and Polymorphism
class LeadDashboard(LeadDashboardOperations, TaskDetails):

    def update(self, member, task_description):
        #  task_list = self._allTasks
        task_list = DashboardDAO()
        # print(f'Task for {member.upper()} before Update: {task_list.get(member.upper())}')
        print(f'Task for {member.upper()} before Update: {task_list.get_data(member.upper())}')
        # self._allTasks.get(member.upper()).append(task_description)
        task_list.update_data(member, task_description)
        print(f'Task updated for {member.upper()}')
        # print(f'Task for {member.upper()} after Update: {task_list.get(member.upper())}')
        print(f'Task for {member.upper()} after Update: {task_list.get_data(member.upper())}')
        print(task_list)

    def delete(self, member, task_id):
        task_list = self._allTasks
        print(f'Task for {member.upper()} before deletion: {task_list.get(member.upper())}')
        self._allTasks.get(member.upper()).pop(task_id)
        print(f'Task deleted for {member.upper()}')
        print(f'Task for {member.upper()} after deletion: {task_list.get(member.upper())}')

    def view(self):
        # tasks = self._allTasks
        lead_dashboard = DashboardDAO()
        tasks = lead_dashboard.get_lead_dashboard()
        return tasks

    def add(self, task_description):
        lead_dashboard = DashboardDAO()
        lead_dashboard.add_task(task_description)
