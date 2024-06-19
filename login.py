from color import colour_print, RED, GREEN, YELLOW
from controller import UserController


def logs_in():
    """
    Accept user Phone and Password to valid the user
    :return: User info is returned

    Some user acc:
    phone: "1234", 09012341234
    pass: 1111
    """
    count = 0
    while count < 3:
        count += 1
        phone_number = input("Enter your Phone Number here: ")
        password = input("Enter your Password here: ")
        if phone_number != "" and password is not None:
            print("*"*14, colour_print(f"Processing!, Please wait", YELLOW), "*"*14)
            user_info = UserController().login(phone_number, password)
            if user_info is not None:
                print("")
                print("*"*17, colour_print(f"Login Successful {user_info['surname']} {user_info['other_name']}", GREEN),
                      "*"*17)
                print("Welcome to USSD Banking. Please note the that a #11 ")
                print(" network charge will be applied to your bank account ")
                print("   for banking services in this channel.")
                return user_info
            elif user_info is None and count < 3:
                print()
                print("Please enter a valid Phone Number and Password")
                print("*"*14, colour_print(f"Your attempt remain {3-count}", RED), "*"*14)
                # print("*"*14, f"Your attempt remain {3-count}", "*"*14)

        elif count < 3:
            print()
            print("Please fill all the required inputs" )
            print("*"*14, f"Your attempt remain {3-count}", "*"*14)

    else:
        print()
        print("*"*14, colour_print(f"No more attempt, Please ensure you have registered", RED), "*"*14)
        # print("*"*14, f"No more attempt, Please ensure you have registered", "*"*14)
        return 0


if __name__ == "__main__":
    print("Main Login module")
    logs_in()



