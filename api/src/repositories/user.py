from src.repositories.db import Database

class UserRepository():
    def __init__(self):
        self.db = Database()

    def authenticate(self, username):
        command_text = "SELECT * FROM users WHERE username = '{0}'".format(username)
        data = self.db.many(command_text)
        val = data[0] if data else None
        return {"id":val[0],"name":val[1]} if val else {}
    
    def create_user(self, username):
        command_text = "INSERT INTO users (username) VALUES ('{0}') RETURNING id".format(username)
        data = self.db.update(command_text)
        return data
