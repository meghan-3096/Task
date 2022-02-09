class Dashboard:

    def __init__(self, dashboard_operation):
        self.dashboard_operation = dashboard_operation

    def delete(self, member, taskid):
        self.dashboard_operation.delete(member, taskid)

    def update(self, member, task_description):
        self.dashboard_operation.update(member, task_description)

    def add(self, task_description):
        self.dashboard_operation.add(task_description)

    def view(self):
        tasks = self.dashboard_operation.view()
        return tasks
