"""
The planner takes some limits and constructs a set of targets based on
those limits and a specific task.
"""


def create_plan(task_cls, start, end):
    task = task_cls(start, end)
    return task.spec()


def execute_plan(plan):
    pass


def execute_task(task, **kw):
    """
    Given a task and its arguments, construct a dadd spec and
    submit it to the master.
    """
    spec = {
        'cmd': 'python ',
    }
