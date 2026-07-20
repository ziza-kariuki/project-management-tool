import unittest
import os
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import save_data, load_data

class TestStoragePersistence(unittest.TestCase):
    
    def setUp(self):
       #Creates test file path
        import utils.storage
        self.original_file = utils.storage.DATA_FILE
        utils.storage.DATA_FILE = "data/test_storage_temp.json"
        
        self.sample_users = [User(name=" Ziza", email="ziza@test.com")]
        self.sample_projects = [Project(title="Test Project", description="Specs", due_date="2026-12-31")]

    def tearDown(self):
        #Clean temporary files
        import utils.storage
        utils.storage.DATA_FILE = self.original_file
        if os.path.exists("data/test_storage_temp.json"):
            os.remove("data/test_storage_temp.json")

    def test_save_and_load_consistency(self):
        #Test saving data and loading it back 
        save_data(self.sample_users, self.sample_projects)
        loaded_users, loaded_projects = load_data()
        
        self.assertEqual(len(loaded_users), 1)
        self.assertEqual(loaded_users[0].name, " Ziza")
        self.assertEqual(loaded_users[0].email, "ziza@test.com")


class TestCoreDomainLogic(unittest.TestCase):

    def test_user_inheritance_and_validation(self):
       #Verify User inherits from person and is not empty
        user = User(name="Ziza Kariuki", email="ziza@test.com")
        
        # Test property reading
        self.assertEqual(user.name, "Ziza Kariuki")
        
        # Test setter validation rule (raises ValueError if empty)
        with self.assertRaises(ValueError):
            user.name = "   "

    def test_task_completion_flow(self):
        #Ensure tasks start Pending and correctly switch to Complete
        task = Task(title="Configure Database", assigned_to="ziza@test.com")
        self.assertEqual(task.status, "Pending")
        
        task.mark_complete()
        self.assertEqual(task.status, "Complete")


if __name__ == "__main__":
    unittest.main()