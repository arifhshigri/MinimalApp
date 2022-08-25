import json


class UserService:
    def __init__(self):
        users = [
            {"id": 1, "name": "Harry Simon","number":"54442334"},
            {"id": 2, "name": "David Mclaren" ,"number":"522883057"},
            {"id": 3, "name": "Jhon Doe","numbers":"655992045"},
        ]
        self.users = users

    def get_users(self):
        return self.users

    def get_users_by_number(self, num):
        user = [s for s in self.users if s.get("number", '') == num]
        return user[0] if user else {}

    def get_users_by_id(self, id):
        user = [s for s in self.users if str(s.get("id","")) == str(id)]
        return user[0] if user else {}


    def create_user(self, user):
        user['id'] = len(self.users)+1
        if self.get_users_by_number(user.get("number")):
            raise Exception("User with number already exist")
        self.users.append(user)
        return self.users


    def update_user(self, request_user):
        users = [s for s in self.users if str(request_user.get("id")) != str(s.get("id")) and request_user.get("number")==s.get("number")]
        if users:
            raise Exception("User with same number exists.")
        users = [s for s in self.users if int(request_user.get("id"))== s.get("id")]
        if users:
            users[0].update(request_user)
            return users[0]
        return json.dumps({'message': 'user id not found'});

