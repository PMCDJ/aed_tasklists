from aed_ds.dictionaries.hash_table import HashTable
from models.users import User
class TaskListController:
    
    def __init__(self):
        self.users = HashTable()
    
    def has_user(self, user_name):
        self.users.has_key(user_name)

    def add_user(self, user_name):
        user = User(user_name)
        self.users.insert(user_name, user)

    def remove_user(self, user_name):
        user = User(user_name)
        self.users.remove(user_name,user)
    
    def has_users(self):
        pass

    # Returns a singly linked list of users
    def get_users(self):
        pass

    def has_task_list(self, user_name, task_list_name):
        pass

    def create_task_list(self, user_name, task_list_name):
        pass

    def remove_task_list(self, user_name, task_list_name):
        pass

    def has_task(self, user_name, task_list_name, task_id):
        pass
    
    def create_task(self, user_name, task_list_name, task_id, task_description):
        pass
    
    def remove_task(self, user_name, task_list_name, task_id):
        pass
    
    def edit_task(self, user_name, task_list_name, task_id, task_description):
        pass
    
    def has_task_lists(self, user_name):
        pass
    
    def get_task_lists(self, user_name):
        pass
    
    def has_tasks(self, user_name, task_list_name):
        pass
    
    def get_tasks(self, user_name, task_list_name):
        pass
    
    def has_task(self, user_name, task_list_name, task_id):
        pass
    
    def toggle_state(self, user_name, task_list_name, task_id):
        pass
    