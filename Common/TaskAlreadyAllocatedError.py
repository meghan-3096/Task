from Common.ConnectToSF import ConnectToSF


class TaskAlreadyAllocatedError(Exception):

    def __init__(self, task_id):
        self.__task_id = task_id
        dashb = TaskAlreadyAllocatedError(task_id)
        allocated_member = dashb.get_name()
        self.message = f"Task has already been allocated to {allocated_member}"
        super().__init__(self.message)

    def get_name(self):
        cursor = ConnectToSF.connect_snowflake()
        query = f"SELECT USERNAME FROM TASK.PUBLIC.DASHBOARD WHERE TASK_ID = '{self.__task_id}';"
        cursor.execute(query)

        name = cursor.fetch_pandas_all()['USERNAME']

        return name
