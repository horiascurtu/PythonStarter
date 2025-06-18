import unittest
from utils import core

class TestTaskManager(unittest.TestCase):
    def test_add_and_list(self):
        core.save_tasks([])  # Clear existing tasks
        core.add_task("Test task")
        tasks = core.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Test task")
        self.assertFalse(tasks[0]["done"])

if __name__ == "__main__":
    unittest.main()
