SELECT username, task_description FROM TASK.PUBLIC.TASKDETAILS as t join TASK.PUBLIC.DASHBOARD as d ON (t.task_id = d.task_id) WHERE username='HARRY';
