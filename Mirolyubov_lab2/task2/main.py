import json
from Container import Container
from User import User


if __name__ == "__main__":
    db = {}
    general_storage = Container("user", set())

    with open("db.json", "r") as f:
        f.seek(0, 2)
        if f.tell() != 0:
            f.seek(0, 0)
            db = json.load(f)

    print("Enter username: ", end="")
    username = input()

    if username not in db.keys():
        db[username] = set()
    general_storage = Container(username, db[username])

    #general_storage.add("5 6 7")
    #general_storage.save(db)
    general_storage.remove("7")
    general_storage.list()







