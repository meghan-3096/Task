from Common.ConnectToSF import ConnectToSF
from DAO.UserDAO import UserDAO
from Common.TaskAlreadyAllocatedError import TaskAlreadyAllocatedError
from Common.TaskAlreadyExistsError import TaskAlreadyExistsError


class DashboardDAO:
    cursor = ConnectToSF.connect_snowflake()

    def get_data(self, username):
        #  cursor = ConnectToSF.connect_snowflake()

        query = f"SELECT task_description FROM TASK.PUBLIC.TASKDETAILS as t " \
                f"join TASK.PUBLIC.DASHBOARD as d ON (t.task_id = d.task_id) WHERE username='{username.upper()}';"
        self.cursor.execute(query)

        tasks = self.cursor.fetch_pandas_all()['TASK_DESCRIPTION']

        return tasks

    def update_data(self, member, task_description):
        dashb = DashboardDAO()
        task_id = dashb.get_taskid(task_description)
        if not dashb.is_allocated(task_id):
            dashb.allocate_task(task_id, member)
        else:
            raise TaskAlreadyAllocatedError

    def delete_data(self, member, task_id):
        #  cursor = ConnectToSF.connect_snowflake()

        query = f"DELETE * FROM TASK.PUBLIC.TEAM WHERE username = '{member}'"
        self.cursor.execute(query)

        return self.cursor

    def get_lead_dashboard(self):
        #   cursor = ConnectToSF.connect_snowflake()

        # Getting members list
        user = UserDAO()
        members = user.get_usernames()
        all_tasks = dict()
        data = DashboardDAO()

        # Getting Tasks for each member
        for member in members:
            tasks = list()
            tasks.append(data.get_data(member))
            all_tasks[member] = tasks

        all_tasks['UNALLOCATED TASKS'] = data.get_unallocated_tasks()

        return all_tasks

    def is_allocated(self, task_id):
        #  cursor = ConnectToSF.connect_snowflake()

        query = f"SELECT TASK_ID FROM TASK.PUBLIC.DASHBOARD WHERE TASK_ID = '{task_id}';"
        self.cursor.execute(query)

        if self.cursor.rowcount == 0:
            return False
        else:
            return True

    def get_taskid(self, task_description):
        #  cursor = ConnectToSF.connect_snowflake()

        query = f"SELECT TASK_ID FROM TASK.PUBLIC.TASKDETAILS WHERE TASK_DESCRIPTION = '{task_description}';"
        self.cursor.execute(query)

        task_id = self.cursor.fetch_pandas_all()['TASK_ID']

        return task_id

    def add_task(self, task_description):
        # cursor = ConnectToSF.connect_snowflake()

        query = f"INSERT INTO TASK.PUBLIC.TASKDETAILS(TASK_DESCRIPTION) VALUES ('{task_description}');"
        print(query)
        self.cursor.execute(query)

    def is_present(self, task_description):
        query = f"SELECT TASK_DESCRIPTION FROM TASK.PUBLIC.TASKDETAILS WHERE TASK_DESCRIPTION = '{task_description}';"
        self.cursor.execute(query)

        if self.cursor.rowcount == 0:
            return False
        else:
            return True

    def allocate_task(self, task_id, member):
        query = f"INSERT INTO TASK.PUBLIC.DASHBOARD VALUES ('{member}', {task_id}); "
        self.cursor.execute(query)
        print(f"Task allocated to {member}")

    def add_task(self, task_description):
        dashb = DashboardDAO()
        if not dashb.is_present(task_description):
            query = f"INSERT INTO TASK.PUBLIC.TASKDETAILS(TASK_DESCRIPTION) VALUES ('{task_description}');"
            self.cursor.execute(query)
            print('Task Added Successfully')
        else:
            raise TaskAlreadyExistsError(task_description)

    def get_unallocated_tasks(self):
        dashb = DashboardDAO()
        task_ids = tuple(dashb.get_allocated_taskid())

        query = f"SELECT TASK_DESCRIPTION FROM TASK.PUBLIC.TASKDETAILS " \
                f"WHERE TASK_DESCRIPTION NOT IN ;"
        print(query)
        self.cursor.execute(query)

        unallocated_tasks = self.cursor.fetch_pandas_all()['TASK_DESCRIPTION']

        return unallocated_tasks

    def get_allocated_taskid(self):
        query = f"SELECT TASK_ID FROM TASK.PUBLIC.DASHBOARD;"
        self.cursor.execute(query)

        task_id_list = self.cursor.fetch_pandas_all()['TASK_ID']

        return task_id_list
