from content import operation_options
from login import logs_in
from signup import Register
from controller import BankingController
import sys
from color import colour_print, RED, GREEN, YELLOW, CYAN


""" """
# 12347890  1111
# 1234 1111
# 09874321 111


def airtime_self():
    print("\n")
    print("*"*10, colour_print(f"Please enter amount (10 - 10000)", CYAN), "*"*10)
    print("00. Back")
    print("0. Exit\n")
    airtime_self_amt = input(">>>>>>>> : ")

    if airtime_self_amt == "0":
        sys.exit(0)
    elif airtime_self_amt == "00":
        services()
    else:
        try:
            if type(int(airtime_self_amt)) == int:
                airtime_self_amt = int(airtime_self_amt)
                if 10 <= airtime_self_amt <= 10000:
                    print("*"*7, colour_print(f"You want to Purchase #{airtime_self_amt} airtime ", CYAN), "*"*7)
                    print("*"*7, colour_print(f"to {user_info['phone_number']} #11 charges fees will be apply", CYAN), "*"*7)
                    print("1. Yes")
                    print("0. No and Exit")
                    are_you_sure = input(">>>>>>>> : ")
                    print()
                    if are_you_sure == "1":
                        bank_operation.purchase_airtime(airtime_self_amt, user_info['phone_number'],)
                    else:
                        print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                        sys.exit(0)
                else:
                    print()
                    print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                    print("*"*7, colour_print(f"Please enter amount within #10 - 10,000", RED), "*"*7)
                    deposit()

            # raise ValueError(f"Please Enter an Integer Value {airtime_self_amt} is not a integer")
        except ValueError as e:
            print(colour_print(f"You have entered a wrong amount, : `{airtime_self_amt}` please enter value (10 - 10000)", RED))
            airtime_self()


def airtime_other():
    print("\n")
    print("*"*10, colour_print(f"Please enter amount (10 - 10000)", CYAN), "*"*10)
    print("00. Back")
    print("0. Exit")
    airtime_self_amt = input(">>>>>>>> : ")

    if airtime_self_amt == "0":
        sys.exit(0)
    elif airtime_self_amt == "00":
        services()
    else:
        try:
            if type(int(airtime_self_amt)) == int:
                airtime_self_amt = int(airtime_self_amt)
                if 10 <= airtime_self_amt <= 10000:
                    print()
                    print("*"*7, colour_print(f"Please enter destination phone number", CYAN), "*"*7)
                    print("0. To Exit")
                    destination_number = input(">>>>>>>> : ")
                    print()
                    if destination_number != "0" and destination_number is not None:
                        print("*"*7, colour_print(f"You want to Purchase #{airtime_self_amt} ", CYAN), "*"*7)
                        print("*"*7, colour_print(f"airtime to {destination_number} #11 charges fees will be apply", CYAN), "*"*7)
                        print("1. Yes")
                        print("0. No and Exit")
                        are_you_sure = input(">>>>>>>> : ")
                        print()
                        if are_you_sure == "1":
                            bank_operation.purchase_airtime(airtime_self_amt, destination_number,)
                        else:
                            print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                            sys.exit(0)
                    elif destination_number == "0":
                        print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                        sys.exit(0)
                    else:
                        raise ValueError(f"Invalid character {airtime_self_amt} Transaction Cancelled")
                        sys.exit(0)
                else:
                    print()
                    print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                    print("*"*7, colour_print(f"Please enter amount within #10 - 10,000", RED), "*"*7)
                    airtime_other()

            # raise ValueError(f"Please Enter an Integer Value {airtime_self_amt} is not a integer")
        except ValueError as e:
            print(colour_print(f"You have entered a wrong amount : `{airtime_self_amt}` please enter value (10 - 10000)", RED))
            airtime_self()


def deposit():
    print("\n")
    print("*"*10, colour_print(f"Please enter amount to save (40 - 200000)", CYAN), "*"*10)
    print("00. Back")
    print("0. Exit")
    transfer_amount = input(">>>>>>>> : ")

    if transfer_amount == "0":
        sys.exit(0)
    elif transfer_amount == "00":
        services()
    else:
        try:
            if type(int(transfer_amount)) == int:
                transfer_amount = int(transfer_amount)
                if 40 <= transfer_amount <= 200000:
                    print()
                    print("*"*7, colour_print(f"Are you sure, you want to", CYAN), "*"*7)
                    print("*"*7, colour_print(f"Deposit #{transfer_amount} to your account,(`{user_info['surname']}`)", CYAN), "*"*7)
                    print("1. Yes")
                    print("0. No and Exit")
                    are_you_sure = input(">>>>>>>> : ")
                    print()
                    if are_you_sure == "1":
                        bank_operation.deposit(transfer_amount)
                    else:
                        print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                        sys.exit(0)
                else:
                    print()
                    print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                    print("*"*7, colour_print(f"Please enter amount within #40 -200,000", RED), "*"*7)
                    deposit()

            # raise ValueError(f"Please Enter an Integer Value {airtime_self_amt} is not a integer")
        except ValueError as e:
            print(colour_print(f"You have entered a wrong amount : `{transfer_amount}` please enter value (40 - 200,000)", RED))
            deposit()


def transfer():
    print("\n")
    print("*"*10, colour_print(f"Please enter amount (1 - 200000)", CYAN), "*"*10)
    print("00. Back")
    print("0. Exit")
    transfer_amount = input(">>>>>>>> : ")

    if transfer_amount == "0":
        sys.exit(0)
    elif transfer_amount == "00":
        services()
    else:
        try:
            if type(int(transfer_amount)) == int:
                transfer_amount = int(transfer_amount)
                if 1 <= transfer_amount <= 200000:
                    print()
                    print("*"*7, colour_print(f"Please enter destination Account number", CYAN), "*"*7)
                    print("0. To Exit")
                    destination_acct = input(">>>>>>>> : ")
                    print()
                    if destination_acct != "0" and destination_acct is not None:
                        print("*"*7, colour_print(f"  Are you sure, you want to Transfer", CYAN), "*"*7)
                        print("*"*7, colour_print(f"#{transfer_amount} to {destination_acct}, Note #11 charge will apply", CYAN), "*"*7)
                        print("1. Yes")
                        print("0. No and Exit")
                        are_you_sure = input(">>>>>>>> : ")
                        print()
                        if are_you_sure == "1":
                            bank_operation.transfer(transfer_amount, destination_acct)
                        else:
                            print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                            sys.exit(0)
                    elif destination_acct == "0":
                        print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                        sys.exit(0)
                    else:
                        raise ValueError(f"Invalid character {transfer_amount} Transaction Cancelled")
                        sys.exit(0)
                else:
                    print()
                    print("*"*7, colour_print(f"  Transaction Cancelled", RED), "*"*7)
                    print("*"*7, colour_print(f"Please enter amount within #40 -200,000", RED), "*"*7)
                    transfer()

        # raise ValueError(f"Please Enter an Integer Value {airtime_self_amt} is not a integer")
        except ValueError as e:
            print(colour_print(f"You have entered a wrong amount : `{transfer_amount}` please enter value (1 - 200,000)", RED))
            transfer()


def withdraw():
    print("\n")
    print("*"*10, colour_print(f"Please enter amount to Withdraw (40 - 200000)", CYAN), "*"*10)
    print("00. Back")
    print("0. Exit")
    transfer_amount = input(">>>>>>>> : ")

    if transfer_amount == "0":
        sys.exit(0)
    elif transfer_amount == "00":
        services()
    else:
        try:
            if type(int(transfer_amount)) == int:
                transfer_amount = int(transfer_amount)
                if 40 <= transfer_amount <= 200000:
                    print()
                    print("*"*7, colour_print(f"Are you sure, you want to", CYAN), "*"*7)
                    print("*"*7, colour_print(f"Withdraw #{transfer_amount} from your account,(`{user_info['surname']}`)", CYAN), "*"*7)
                    print("1. Yes")
                    print("0. No and Exit")
                    are_you_sure = input(">>>>>>>> : ")
                    print()
                    if are_you_sure == "1":
                        bank_operation.withdraw(transfer_amount)
                    else:
                        print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                        sys.exit(0)
                else:
                    print()
                    print("*"*7, colour_print(f"Transaction Cancelled", RED), "*"*7)
                    print("*"*7, colour_print(f"Please enter amount within #40 -200,000", RED), "*"*7)
                    deposit()

            # raise ValueError(f"Please Enter an Integer Value {airtime_self_amt} is not a integer")
        except ValueError as e:
            print(colour_print(f"You have entered a wrong amount : `{transfer_amount}` please enter value (40 - 200,000)", RED))
            deposit()


def check_balance():
    print()
    print("*"*7, colour_print(f"  Operation Successful ", GREEN), "*"*7)
    print("*"*7, colour_print(f"Your remaining balance is # {bank_operation.check_balance()}", GREEN), "*"*7)


def transaction_history():
    print()
    print("*"*7, colour_print(f"  Transaction History  ", GREEN), "*"*7)
    rows = bank_operation.transaction_history()
    if rows is not None:
        for row in rows:
            print( f"#{row[4]} {row[1]} to {row[5]} ==> Remaining Balance is {row[3]}")
            print(colour_print("-" * 40, YELLOW ),)
        # print("*"*7, colour_print(f" Successful ", GREEN), "*"*7)
        # print()
        print("*"*7, colour_print(f"Will you like to generate the text file", CYAN), "*"*7)
        print("1. Yes")
        print("0. No and Exit")
        file_need = input(">>>>>>>> : ")
        if file_need == "1":
            bank_operation.generate_history_file()
        else:
            sys.exit(0)
    else:
        print("No History Found")


def services():
    print()
    print("*"*10, colour_print(f"Select your option", CYAN), "*"*10)
    print("1. Airtime-Self")
    print("2. Airtime Other")
    print("3. Transfer ")
    print("4. Withdraw")
    print("5. Deposit")
    print("6. Check Balance")
    print("7. Transaction History")
    print("0. Exit")

    service_option = input(">>>>>>>> : ")
    print("*"*44)

    if service_option == "1":
        airtime_self()
    elif service_option == "2":
        airtime_other()
    elif service_option == "3":
        transfer()
    elif service_option == "4":
        withdraw()
    elif service_option == "5":
        deposit()
    elif service_option == "6":
        check_balance()
    elif service_option == "7":
        transaction_history()
    elif service_option == "0":
        print("*"*10, colour_print(f"Operation Cancelled", RED), "*"*10)
        sys.exit(0)
    else:
        print("*"*10, colour_print(f"Incorrect character entered", RED), "*"*10)
        sys.exit(0)
    # print("reach elif")


def banking():
    option = None
    while option != "1":
        print("1. Proceed: ")
        print("99. Exit ")
        option = input("Enter your option here: ")
        if option == "99":
            sys.exit(0)
        elif option == "1":
            services()
            break
        else:
            print()
            print("*"*10, colour_print(f"Incorrect character entered, Please enter...", RED), "*"*10)


user_info = {}
bank_operation = None
if __name__ == "__main__":
    print("Welcome to Orlam Banking App" )
    print("Please Select option")
    print("1. Create Account ")
    print("2. Login")
    try:
        action = int(input(">>>>>>>> : "))
        print()
        if action == 1:
            try:
                Register().user_input()
            except:
                sys.exit(0)
            finally:
                user_info = logs_in()

        elif action == 2:
            user_info = logs_in()
            if user_info is not None:
                bank_operation = BankingController(phone_number=user_info["phone_number"])
                banking()

        else:
            print("*"*10, colour_print(f"Incorrect value entered", RED), "*"*10)
            # print(f"{user_info['surname']} {user_info['other_name']}, render from main app")

    except ValueError as e:
        print("*"*10, colour_print(f"Operation Cancelled", RED), "*"*10)
        print("*"*10, colour_print(f"Incorrect value entered", RED), "*"*10)


