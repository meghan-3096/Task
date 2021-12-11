class Dashboard:

    def __init__(self, dashboard_operation):
        self.dashboard_operation = dashboard_operation

    def delete(self, member, taskid):
        self.dashboard_operation.delete(member, taskid)

    def update(self, member, taskid):
        self.dashboard_operation.update(member, taskid)

    def view(self):
        self.dashboard_operation.view()

