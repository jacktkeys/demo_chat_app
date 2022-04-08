from src.repositories.db import Database

class MessageRepository():
    def __init__(self):
        self.db = Database()
    
    def create_message(self, text, userid, roomid):
        command_text = "INSERT INTO messages (content, created_by, room_id) VALUES ('{0}', '{1}', '{2}') RETURNING id".format(text, userid, roomid)
        data = self.db.update(command_text)
        return data[0]
    
    def delete_message(self, messageid):
        command_text = "DELETE FROM messages WHERE messages.id = '{0}'".format(messageid)
        data = self.db.update(command_text)
        return data