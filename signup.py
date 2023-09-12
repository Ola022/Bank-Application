from color import colour_print, RED, GREEN
from controller import UserController
from content import userInfo


# Confirm Pass
def check_password_match(passwd, confirmed):
    password = passwd
    confirmed_pass = confirmed
    while password != confirmed_pass:
        print()
        print("*"*14, colour_print("Password enter did not match, Re-Enter!!", RED), "*"*14)
        password = input("Enter your Password here: ")
        confirmed_pass = input("Confirm your Password here: ")

    else:
        return password


class Register(object):

    def __init__(self):
        self.info: userInfo.keys() = {}
        self.surname: str = ""
        self.other_name = ""
        self.phone_number = ""
        self.email = ""
        self.password = ""
        self.confirmed_pass = ""
        self.is_saving = ""

    def user_input(self):
        while self.is_saving != "2":
            self.surname = input("Enter your Surname here: ")
            self.other_name = input("Enter your other name here: ")
            self.phone_number = input("Enter your Phone Number here: ")
            self.email = input("Enter your Email Number here: ")
            self.password = input("Enter your Password here: ")
            self.confirmed_pass = input("Confirm your Password here: ")
            self.password = check_password_match(self.password, self.confirmed_pass)

            print()
            print("******* Please confirm Your details before proceed *******")
            print(f"Surname : {self.surname};  \t\t\tOther Name: {self.other_name}; "
                  f"\nPhone Number: {self.phone_number};   \t\tEmail: {self.email}; \t\tPassword: {self.password}")
            print("1. Cancel ")
            print("2. Proceed and Save")
            self.is_saving = input(">>>>> :  ")
            if self.is_saving == "1":
                break
        else:
            self.save()

    def save(self):
        self.info["surname"] = self.surname
        self.info["other_name"]= self.other_name
        self.info["phone_number"] = self.phone_number
        self.info["email"] = self.email
        self.info["userId"] = self.phone_number
        self.info["password"] = self.password
        UserController().register_user(self.info)

    def __str__(self):
        print("*******Please confirm Your details before proceed *******")


if __name__ == "__main__":
    Register().user_input()
    # info: userInfo.keys() = {}
    # info["password"] = "__main__"
    # print(info["password"])
    # print(info)






