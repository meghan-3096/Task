class TaskAlreadyExistsError(Exception):

    def __init__(self, task_description):
        self.__task_description = task_description
        self.__message = f'{task_description} is already present in task list'
        super().__init__(self.__message)
