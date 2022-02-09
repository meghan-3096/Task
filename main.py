from Common.Authentication import Authentication
from Common.Authorization import Authorization
from Common.ConnectToSQLServer import ConnectToSQLServer
from Beans.EmployeeBean import EmployeeBean
from Tasks.Dashboard import Dashboard
from Tasks.TeamDashboard import TeamDashboard
from Tasks.LeadDashboard import LeadDashboard
from Tasks.TaskDetails import TaskDetails


def execute_operation(option, employee):

    if employee.get_role() == 'Team Lead':
        #operation = LeadDashboard(employee.get_username())
        operation = Dashboard(LeadDashboard(employee.get_username()))
        if option == 1: #Delete
            member = input('For: ')
            taskid = int(input("Task Number: "))
            taskid -= 1
            operation.delete(member, taskid)
        elif option == 2: #Update
            print('Choose: \n1. Add New Task \n2. Allocate Task')
            choice = int(input('Choice: '))
            if choice == 1:
                task_desc = input('Enter Task: ')
                operation.add(task_desc)
            elif choice == 2:
                member = input('For: ')
                task_desc = input('Enter Task: ')
                operation.update(task_desc)
        elif option == 3: #exit
            pass
        else:
            print('Choice Does Not Exist')
    elif employee.get_role() == 'Team Member':
       # operation = TeamDashboard(employee.get_username())
        operation = Dashboard(TeamDashboard(employee.get_username()))
        if option == 1: #Delete
            taskid = int(input("Task Number: "))
            taskid -= 1
            operation.delete(employee.get_username(), taskid)
        elif option == 2: #Exit
            pass
        else:
            print('Choice Does Not Exist')

def get_data(employee):
    auth1 = Authentication(employee.get_username(), employee.get_password())

 #   if auth1.is_authentic():
    if auth1.is_valid():

        if employee.get_role() == 'Team Lead':
            LeadTasks = Dashboard(LeadDashboard(employee.get_username()))
            data = LeadTasks.view()
        elif employee.get_role() == 'Team Member':
            MemberTasks = Dashboard(TeamDashboard(employee.get_username()))
            data = MemberTasks.view()
    else:
        data = 'Not Authorized'

    return data

def getOperations(employee):

    op = Authorization(employee.get_role())
    operations = op.operations_authorized()

    return operations


def main():

    username = input('username: ')
    password = input('password: ')

    employee = EmployeeBean(username, password)
    data = get_data(employee)
    if data == 'Not Authorized':
        print('Wrong Username or Password')
    else:
        print(data)
        operations = getOperations(employee)
        print(f'Choose: {operations}')
        option = int(input('Choice: '))
        execute_operation(option, employee)



if __name__ == '__main__':
    main()

