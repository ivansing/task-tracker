import unittest
import os
import json
from unittest.mock import patch, mock_open

from task_manager import (
    load_tasks,
    save_tasks,
    add_task,
    list_tasks,
    mark_in_progress,
    mark_done,
    update_task,
    delete_task
)

class TestTaskManager(unittest.TestCase):

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_load_tasks_empty(self, mock_file, mock_exists):
        tasks = load_tasks("test.json")
        self.assertEqual(tasks, [])
        mock_file.assert_called_once_with("test.json", "r")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_file):
        tasks = [{"id":1, "description":"Test", "status":"todo"}]
        save_tasks(tasks, "test.json")
        mock_file.assert_called_once_with("test.json", "w")

        
        handle = mock_file()
        handle.write.assert_called()  
    def test_add_task(self):
        
        if os.path.exists("test_tasks.json"):
            os.remove("test_tasks.json")

        new_id = add_task("Write unit tests")

        
        tasks = load_tasks("tasks.json")  
        self.assertTrue(any(t["id"] == new_id for t in tasks))
        self.assertTrue(any(t["description"] == "Write unit tests" for t in tasks))

        # Clean up if desired
        # os.remove("tasks.json")

    # Additional tests for mark_in_progress, mark_done, etc. would follow...

if __name__ == "__main__":
    unittest.main()
 
                