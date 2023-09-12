import sys
import sqlite3
from content import userInfo
from color import colour_print, RED, GREEN, YELLOW


class UserController(object):

    def __init__(self):
        self.con_str = "banking.sqlite"
        self.info = {}
        self.surname = ""
        self.other_name = ""
        self.phone_number = ""
        self.email = ""
        self.user_info = ""
        self.password = ""
        self.money = 0

    def login(self, phone_no, passwd):
        self.phone_number = phone_no
        self.password = passwd

        try:
            info: userInfo = {}
            db = sqlite3.connect(self.con_str)
            cursor = db.cursor()

            cursor.execute(
                f"SELECT * FROM userinfo where phone_number= '{self.phone_number}' and password = '{self.password}' ")
            row = cursor.fetchone()
            if row is not None:
                info = {"surname": row[0], "other_name": row[1], "phone_number": row[2], "email": row[3],
                        "user_info": row[4], "money": row[5]}
            else:
                print("User Not Found")
                return None
        except RuntimeError as e:
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            sys.exit(0)
        else:
            # print(row, "User found")
            return info
        finally:
            cursor.close()
            db.close()

    def get_user_info(self, phone_no):
        self.phone_number = phone_no
        try:
            db = sqlite3.connect(self.con_str)  # 12347890   1111
            for self.surname, self.other_name, self.phone_number, self.email, self.user_info, self.password, self.money \
                    in db.execute(f"SELECT * FROM userinfo where phone_number = {self.phone_number}"):
                # print(self.surname, type(self.password), self.phone_number)
                pass
        except RuntimeError:
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            sys.exit(0)
        finally:
            db.close()

    def register_user(self, userinfo: userInfo):
        try:
            db = sqlite3.connect(self.con_str)
            self.info = userinfo
            self.surname = self.info["surname"]
            self.other_name = self.info["other_name"]
            self.phone_number = self.info["phone_number"]
            self.email = self.info["email"]
            self.user_info = self.info["phone_number"]
            self.password = self.info["password"]
            self.info["money"] = self.money

            db.execute("CREATE TABLE IF NOT EXISTS userinfo "
                       "(surname TEXT,other_name TEXT, phone_number TEXT, email TEXT, userId TEXT,"
                       " password TEXT, money INTEGER)")
            # db.execute(f"INSERT INTO userinfo(surname, other_name, phone_number, email, userId, password, money) "
            #           f"VALUES{tuple(self.info.values())}")
            db.execute(f"INSERT INTO userinfo(surname, other_name, phone_number, email, userId, password, money) "
                       f"VALUES('{self.surname}', '{self.other_name}', '{self.phone_number}', "
                       f"'{self.email}', '{self.user_info}', '{self.password}', '{self.money}')")
            db.commit()
        except RuntimeError:
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            sys.exit(0)
        else:
            print()
            print("*" * 17, colour_print(f"Successful Created", GREEN), "*" * 17)
            print("*" * 10, colour_print(f"You can login with phone number and password", GREEN), "*" * 10)
            print()
        finally:
            self.info = {}
            db.close()


class BankingController(object):

    def __init__(self, phone_number):
        self.con_str = "banking.sqlite"
        try:
            self.info: userInfo = {}
            db = sqlite3.connect(self.con_str)
            cursor = db.cursor()

            cursor.execute(
                f"SELECT * FROM userinfo where phone_number= '{phone_number}'")
            row = cursor.fetchone()
            if row is not None:
                self.info = {"surname": row[0], "other_name": row[1], "phone_number": row[2], "email": row[3],
                             "user_info": row[4], "money": row[6]}
                self.surname = self.info["surname"]
                self.other_name = self.info["other_name"]
                self.phone_number = self.info["phone_number"]
                self.email = self.info["email"]
                self.user_info = self.info["user_info"]
                self.money = self.info["money"]
            else:
                print()
                print("*" * 17, colour_print(f" User not Found", RED), "*" * 17)
                print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
        except RuntimeError as e:
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            sys.exit(0)
        finally:
            cursor.close()
            db.close()

    def check_balance(self):
        return self.money

    def transfer(self, amount: int, phone_number: str):
        try:
            amount_and_charges = amount + 11
            balance = self.check_balance()
            if balance >= amount_and_charges:
                new_amount = balance - amount_and_charges
                db = sqlite3.connect(self.con_str)
                update_cursor = db.cursor()
                update_sql = "UPDATE userinfo SET money =? WHERE userinfo.phone_number = ?"
                update_cursor.execute(update_sql, (new_amount, self.phone_number))
                if update_cursor.rowcount == 1:
                    self.money = new_amount
                    print()
                    print("*" * 7, colour_print(f"  Transaction Successful", GREEN), "*" * 7)
                    print("*" * 7,
                          colour_print(f"#{amount} has been Successfully sent to, {phone_number}", GREEN),
                          "*" * 7)
                    print("*" * 7, colour_print(f"Your new balance is #{self.money} ", YELLOW), "*" * 7)
                    update_cursor.connection.commit()
                    update_cursor.close()
                    db.close()
                    self.save_transaction_history(phone_number=self.phone_number, operation='Transfer',
                                                  previous_amount=balance, new_amount=new_amount,
                                                  operation_amount=amount_and_charges, acct_or_phone=self.phone_number)
                else:
                    update_cursor.close()
                    db.close()
                    print()
                    print("*" * 7, colour_print(f"Operation Failed", RED), "*" * 7)
            else:
                print()
                print("*" * 7, colour_print(f"Please deposit to your Acct {self.surname} {self.other_name}", YELLOW),"*" * 7)
                print("*" * 7,
                      colour_print(f"Amount Required is {amount_and_charges}, Your balance is {balance}", YELLOW),
                      "*" * 7)
        except:
            update_cursor.close()
            db.close()
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            sys.exit(0)
        finally:
            # update_cursor.close()
            sys.exit(0)

    def withdraw(self, amount: int):
        try:
            amount_and_charges = amount + 11
            balance = self.check_balance()
            if balance >= amount_and_charges:
                new_amount = balance - amount_and_charges
                db = sqlite3.connect(self.con_str)
                update_cursor = db.cursor()
                update_sql = "UPDATE userinfo SET money =? WHERE userinfo.phone_number = ?"
                update_cursor.execute(update_sql, (new_amount, self.phone_number))
                if update_cursor.rowcount == 1:
                    self.money = new_amount
                    print()
                    print("*" * 7, colour_print(f"  Transaction Successful", GREEN), "*" * 7)
                    print("*" * 7,
                          colour_print(f"#{amount} has been Successfully ", GREEN),
                          "*" * 7)
                    print("*" * 7, colour_print(f"Your new balance is #{self.money} ", YELLOW), "*" * 7)
                    update_cursor.connection.commit()
                    update_cursor.close()
                    db.close()
                    self.save_transaction_history(phone_number=self.phone_number, operation='Withdraw',
                                                  previous_amount=balance, new_amount=new_amount,
                                                  operation_amount=amount_and_charges, acct_or_phone=self.phone_number)
                else:
                    print()
                    update_cursor.close()
                    db.close()
                    print("*" * 7, colour_print(f"Operation Failed", RED), "*" * 7)
            else:
                print()
                print("*" * 7, colour_print(f"Please deposit to your Acct {self.surname} {self.other_name}", YELLOW),
                      "*" * 7)
                print("*" * 7,
                      colour_print(f"Amount Required is {amount_and_charges}, Your balance is {balance}", YELLOW),
                      "*" * 7)
        except:
            update_cursor.close()
            db.close()
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            sys.exit(0)
        finally:
            sys.exit(0)

    def deposit(self, amount: int):
        try:
            amount_and_charges = amount - 11
            balance = self.check_balance()
            new_amount = balance + amount_and_charges
            db = sqlite3.connect(self.con_str)
            update_cursor = db.cursor()
            update_sql = "UPDATE userinfo SET money =? WHERE userinfo.phone_number = ?"
            update_cursor.execute(update_sql, (new_amount, self.phone_number))
            if update_cursor.rowcount == 1:
                self.money = new_amount
                print()
                print("*" * 7, colour_print(f"Transaction Successful", GREEN), "*" * 7)
                print("*" * 7,
                      colour_print(f"{amount_and_charges} has been Successfully added to your Account, {self.surname}",
                                   GREEN), "*" * 7)
                print("*" * 7, colour_print(f"Your new balance is #{self.money} ", YELLOW), "*" * 7)
                update_cursor.connection.commit()
                update_cursor.close()
                db.close()
                self.save_transaction_history(phone_number=self.phone_number, operation='Deposit',
                                              previous_amount=str(balance), new_amount=str(new_amount),
                                              operation_amount=str(amount_and_charges), acct_or_phone=self.phone_number)
            else:
                print()
                print("*" * 7, colour_print(f"Operation Failed", RED), "*" * 7)
        except:
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            sys.exit(0)
        finally:
            # update_cursor.close()
            db.close()
            sys.exit(0)

    def purchase_airtime(self, amount: int, phone_no):
        try:
            db = sqlite3.connect(self.con_str)
            update_cursor = db.cursor()
            amount_and_charges = amount + 11
            balance = self.check_balance()
            if balance >= amount_and_charges:
                new_amount = balance - amount_and_charges
                update_sql = "UPDATE userinfo SET money =? WHERE userinfo.phone_number = ?"
                update_cursor.execute(update_sql, (new_amount, self.phone_number))
                if update_cursor.rowcount == 1:
                    self.money = new_amount
                    print()
                    print("*" * 7, colour_print(f"Successful", GREEN), "*" * 7)
                    print("*" * 7, colour_print(f"Airtime Successfully Purchased, to {phone_no}", GREEN), "*" * 7)
                    print("*" * 7, colour_print(f"#{amount_and_charges} has being deducted from your account", YELLOW),
                          "*" * 7)
                    print("*" * 7, colour_print(f"Your new balance is #{self.money} ", YELLOW), "*" * 7)
                    update_cursor.connection.commit()
                    update_cursor.close()
                    db.close()
                    self.save_transaction_history(phone_number=self.phone_number, operation='Airtime',
                                                  previous_amount=balance, new_amount=new_amount,
                                                  operation_amount=amount_and_charges, acct_or_phone=phone_no)
                else:
                    update_cursor.close()
                    db.close()
                    print()
                    print("*" * 7, colour_print(f"Operation Failed", RED), "*" * 7)
            else:
                update_cursor.close()
                db.close()
                print()
                print("*" * 7, colour_print(f"Please deposit to your Acct {self.surname} {self.other_name}", YELLOW),
                      "*" * 7)
                print("*" * 7,
                      colour_print(f"Amount Required is {amount_and_charges}, Your balance is {balance}", YELLOW),
                      "*" * 7)
        except:
            update_cursor.close()
            db.close()
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            sys.exit(0)
        finally:
            sys.exit(0)

    def save_transaction_history(self, phone_number, operation: str, previous_amount, new_amount, operation_amount,
                                 acct_or_phone):
        try:
            trans_db = sqlite3.connect(self.con_str)
            trans_db.execute("CREATE TABLE IF NOT EXISTS transactionHistory (phone_number TEXT, operation TEXT,"
                             " previous_amount TEXT, new_amount TEXT, operation_amount TEXT, acct_or_phone TEXT)")

            trans_db.execute(f"INSERT INTO transactionHistory(phone_number, operation, previous_amount, new_amount, "
                             f"operation_amount, acct_or_phone) VALUES('{phone_number}', '{operation}', '{previous_amount}', "
                             f"'{new_amount}','{operation_amount}','{acct_or_phone}')")
            trans_db.commit()
            trans_db.close()
        except:
            trans_db.close()
            print("*" * 17, colour_print(f" Operation Failed", RED), "*" * 17)
            # sys.exit(0)

    def transaction_history(self):
        "CREATE TABLE IF NOT EXISTS  ( TEXT, operation TEXT,"
        " previous_amount TEXT, new_amount TEXT, operation_amount TEXT, acct_or_phone TEXT)"
        try:
            info = {}
            db = sqlite3.connect(self.con_str)
            cursor = db.cursor()

            cursor.execute(
                f"SELECT * FROM transactionHistory where phone_number= '{self.phone_number}'")
            rows = cursor.fetchmany(7)
            if len(rows) > 0:
                print()
                return rows
            else:
                # print("No History Found")
                return None
        except RuntimeError as e:
            print("*" * 17, colour_print(f" Operation Failed"), "*" * 17)
            sys.exit(0)
        finally:
            cursor.close()
            db.close()

    def generate_history_file(self):
        rows = self.transaction_history()
        if rows is not None:
            with open("transaction_history.txt", 'w') as history:
                for row in rows:
                    print(f"#{row[4]} {row[1]} to {row[5]} ==> Remaining Balance is {row[3]}", file=history)
                    print("-" * 40, file=history)
                else:
                    print("File Generated")
        else:
            print("No History Found")


if __name__ == "__main__":
    pass
    # BankingController().purchase_airtime("12347890", 20)
    # UserController().get_user_info("12347890")
    # UserController().login("12347890", "1111")
    # info: userInfo.keys() = {}

    # user_controller.register_user()
    # db.close()
