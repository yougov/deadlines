from datetime import datetime, timedelta

from mock import patch, ANY

from deadlines import planner
from footasks import FooPlanner


class TestPlanner(object):

    def create_plan(self):
        end = datetime.now()
        start = end - timedelta(days=2)
        return planner.create_plan(FooPlanner, start, end)

    def test_create_plan_api(self):
        plan = self.create_plan()
        assert len(plan) == 3

        for spec in plan:
            assert 'task' in spec and spec['task'] == 'foo'
            assert 'kwargs' in spec

    def test_execute_plan(self):
        with patch('deadlines.planner.execute_task') as ex:
            plan = self.create_plan()
            planner.execute(plan)
            assert len(ex.mock_calls) == 3
            ex.assert_called_with(day=ANY)
