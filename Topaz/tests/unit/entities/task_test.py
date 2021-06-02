import unittest

from entities.task import Task

INITIAL_TICK = 1
DURATION = 1


class TaskTest(unittest.TestCase):

    def test_decrease_duration_successfully(self):
        task = Task(initial_tick=INITIAL_TICK, duration=DURATION)
        task.decrease_duration()
        self.assertEqual(task.duration, DURATION - 1)
