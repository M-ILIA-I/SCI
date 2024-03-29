import json
from Container import Container
from User import User
from Functions import *
from CONSTANTS import *

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

    Run = True

    while Run:
        menu()
        a = int(input())
        match a:
            case 1:
                print("Enter information that you want to add: ", end="")
                general_storage.add(input())
            case 2:
                general_storage.list()
                print("Enter information that you want to remove: ", end="")
                general_storage.remove(input())
            case 3:
                print("Which element do you want to find?")
                general_storage.find(input())
            case 4:
                general_storage.list()
            case 5:
                general_storage.save(db)
                print("You have successfully saved the container")
            case 6:
                full_list(db)
                print("\n Enter username: ", end="")
                general_storage.load(FILE_PATH, input())
            case 7:
                print("Enter 1 if you want to save data: ", end="")
                if input() == '1':
                    general_storage.save(db)
                full_list(db)
                print("Enter username: ", end="")
                general_storage.switch(input(), db)
            case 8:
                break

    print("Program end")









