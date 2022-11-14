import sys
from dbhelper import DBhelper
class Flikart:
    def __init__(self):
        # connect to database
        self.db=DBhelper()
        self.menu()

    def menu(self):
        user_input=input("""
        1.enter 1 to register
        2.enter 2 to login
        3. anything else to leave
        """)

        if user_input=="1":
            self.register()
        elif user_input=="2":
            self.login()
        else:
            sys.exit(1000)

    def login_menu(self):
        input("""1. enter 1 to see profile.
        2. enter 2 to edit profile
        3. enter 3 to update profile
        4. enter 4 to delete profile.
        """)


    def register(self):
        name=input("enter the name")
        email=input("enter email")
        password=input("enter password")

        response=self.db.register(name,email,password)

        if response:
            print("regristration successful")

        else:
            print("regristration failed")
        self.menu()

    def login(self):
        email = input("enter email")
        password = input("enter password")

        data=self.db.search(email,password)
        if len(data)==0:
            print("invalid email/password")
            self.menu()
        else:
            print("hello ",data[0][1])
            self.login_menu()


obj=Flikart()