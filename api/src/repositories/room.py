from src import config
from src.repositories.db import Database
from datetime import datetime

MESSAGE_LIMIT = config.MESSAGE_LIMIT

class RoomRepository():
    def __init__(self):
        self.db = Database()

    def get_room(self, roomid):
        self.db.connect()
        
        message_command_text = "SELECT messages.id, messages.content, users.id, users.username FROM messages INNER JOIN users ON (messages.created_by = users.id) WHERE room_id = '{0}' ORDER BY created_date DESC".format(roomid)
        message_data = self.db.many(message_command_text, MESSAGE_LIMIT)
        val = [{"id":val[0],"content":val[1],"sentBy":{"id":val[2],"name":val[3]}} for val in message_data]

        return val

    def get_rooms(self):
        rooms_command_text = "SELECT id, name FROM chatrooms"
        room_data = self.db.all(rooms_command_text)
        val = []

        # I really, really, really hate the next block of code. Should be refactored with one SQL query to get the messages with the room info.
        for room in room_data:
            message_command_text = "SELECT m.id, m.created_date, m.content, u.id, u.username FROM messages m INNER JOIN users u ON m.created_by = u.id WHERE m.room_id = '{0}' ORDER BY m.created_date DESC LIMIT 1".format(room[0])
            message_data = self.db.one(message_command_text)
            message = {}
            if message_data:
                user = { "id": message_data[3], "name": message_data[4] }
                sent_date = datetime.strftime(message_data[1], "%m/%d/%Y, %H:%M:%S")
                message = { "id":message_data[0], "sentBy": user, "sentAt": sent_date, "content": message_data[2] }
            else:
                message = None
                
            val.append({ "id": room[0], "name": room[1], "mostRecentMessage": message })

        return val
    
    def create_room(self, roomname, userid):
        command_text = "INSERT INTO chatrooms (name, created_by) VALUES ('{0}', '{1}') RETURNING id".format(roomname, userid)
        data = self.db.update(command_text)
        return data

    def delete_room(self, roomid):
        command_text = "DELETE FROM chatrooms WHERE id = '{0}'".format(roomid)
        data = self.db.update(command_text)
        return data