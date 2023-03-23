import json

from User import User


class Container:
    storage = set()
    user = User("unknown")

    def __init__(self, username, storage):
        self.user.username = username
        self.storage = set(storage)

    def add(self, key: str):
        buffer = key.split(" ")
        if buffer:
            self.storage.update(buffer)

    def remove(self, element):
        self.storage.discard(element)

    def find(self, element):
        if element in self.storage:
            print(element)
        else:
            print("No such elements")

    def list(self):
        for i in self.storage:
            print(i, end=" ")
        print()

    def grep(self):
        pass

    def save(self, db: dict):
        db[self.user.username] = self.storage
        for i in db.keys():
            db[i] = list(db[i])
        with open("db.json", "w") as f:
            json.dump(db, f)

    def load(self, filename, username):
        db = {}
        with open(filename, "r") as f:
            db = json.load(f)
        self.storage.update(db[username])

    def switch(self, username, db):
        self.user.username = username
        if username not in db.keys():
            db[username] = set()
            self.storage = set()
        else:
            self.storage = db[username]
