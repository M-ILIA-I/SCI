def full_list(db: dict):
    for i, j in db.items():
        print("{}: {}".format(i, j))


def menu():
    print("Enter 1 if you want to add data")
    print("Enter 2 if you want to remove data")
    print("Enter 3 if you want to find data")
    print("Enter 4 if you want to show all data in your container")
    print("Enter 5 if you want to save you container")
    print("Enter 6 if you want load the data")
    print("Enter 7 if you want switch user")
    print("Enter 8 if you want stop the program")

