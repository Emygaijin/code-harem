import random
import os
import time
from os import path

user_login = []
token_used = []

bank_coffers = 0
customers_balance = {"bolade": 120000, "jibola": 309999, "seun": 540000, "emeka": 8709999, "musa": 34568}
admin = ["tobi", "chika", "abdul"]


def removePlus():
    print("""
        1 > REMOVE ANOTHER CUSTOMER
        2 > BACK TO MAIN MENU
        3 > LOG - OUT""")
    try:
        ron = int(input(">: "))
    except ValueError:
        print("INVALID COMMAND")
    else:
        if ron == 1:
            remove()
        elif ron == 2:
            home()
        elif ron == 3:
            quit()
        else:
            print("INVALID COMMAND")
            removePlus()


def addPlus():
    print("""
    1 > ADD ANOTHER CUSTOMER
    2 > BACK TO MAIN MENU
    3 > LOG - OUT""")
    try:
        aon = int(input(">: "))
    except ValueError:
        print("INVALID COMMAND")
    else:
        if aon == 1:
            add()
        elif aon == 2:
            home()
        elif aon == 3:
            quit()
        else:
            print("INVALID COMMAND")
            addPlus()


def another():
    print("""
    1 > ANOTHER TRANSFER
    2 > BACK TO MAIN MENU
    3 > LOG - OUT""")
    try:
        ano = int(input(">: "))
    except ValueError:
        print("INVALID COMMAND")
    else:
        if ano == 1:
            transfer()
        elif ano == 2:
            home()
        elif ano == 3:
            quit()
        else:
            print("INVALID COMMAND")
            another()


def back():
    print("""
    1 > BACK TO MAIN MENU
    2 > LOG - OUT""")
    try:
        choice = int(input(">: "))
    except ValueError:
        print("INVALID COMMAND")
    else:
        if choice == 1:
            home()
        elif choice == 2:
            quit()
        else:
            print("INVALID COMMAND")
            back()


def add():
    new = input("ENTER NEW CUSTOMER NAME: ")
    figure = int(input("ENTER DEPOSIT: "))
    plus = random.randint(1000, 9999)
    print(plus)
    take = int(input("ENTER TOKEN DIGITS:"))
    if take == plus:
        print("CUSTOMER HAS BEEN SUCCESSFULLY ADDED ")
        customers_balance[new] = figure
        print(customers_balance)
        addPlus()
    else:
        print("INVALID TOKEN DIGITS")
        add()


def remove():
    rem = input("ENTER CUSTOMER TO BE REMOVED: ")
    if rem in customers_balance:
        removalToken = random.randint(1000, 9999)
        print(removalToken)
        fin = int(input("ENTER TOKEN CODE: "))
        if fin == removalToken:
            customers_balance.pop(rem)
            print(f"{rem.capitalize()} HAS BEEN SUCCESSFULLY REMOVED")
            print(f"THE UPDATED CUSTOMER LIST IS {customers_balance}" )
            removePlus()
        else:
            print("INVALID TOKEN DIGITS")
            remove()
    else:
        print("CUSTOMER DOES NOT EXIST")
        remove()


def login():
    ent = input("ENTER USER NAME: ")
    if ent in admin:
        token = random.randint(1000, 9999)
        print(token)
        try:
            code = int(input("ENTER TOKEN CODE: "))
        except ValueError:
            print("ENTER CORRECT CODE")

        else:

            if token == code:
                user_login.append(ent)
                token_used.append(code)
                home()
            else:
                print("ENTER VALID TOKEN CODE")
                print("Please wait for 5 seconds before retrying")
                time.sleep(5)
                login()
                login()

    else:
        print("ENTER VALID USERNAME")
        login()


def customer_details():
    pow = input("ENTER CUSTOMER NAME: ")
    if pow in customers_balance:
        print(f"{pow}, HAS AN ACCOUNT BALANCE OF N{customers_balance[pow]}")
        back()
    else:
        print("ENTER VALID CUSTOMER")
        customer_details()


def transfer():
    global bank_coffers

    while True:

        sel = input("ENTER NAME OF ACCOUNT YOU WANT TO TRANSFER FROM: ")
        if sel in customers_balance:

            pick = input("ENTER NAME OF ACCOUNT YOU WANT TO TRANSFER TO: ")
            if pick in customers_balance:
                amt = int(input("ENTER AMOUNT TO TRANSFER: "))
                commission = (amt * 1) / 100

                if customers_balance[sel] + commission > amt:
                    customers_balance[sel] = (customers_balance[sel] - amt) - commission
                    customers_balance[pick] = customers_balance[pick] + amt
                    global bank_coffers
                    bank_coffers += commission
                    print(f"TRANSFER OF N{amt}, FROM {sel} to {pick} SUCCESSFUL")
                    print(f"BANK CHARGES: N{commission}, AVAILABLE BALANCE: N{customers_balance[sel]}")

                    file = open("flipped.py", "a")
                    file.write(f"TOTAL CUSTOMER LIST AND BALANCE: {customers_balance}" + "\n")
                    file.write(f"TRANSFER OF N{amt}, FROM {sel} TO {pick}" + "\n")
                    file.write(f"COMMISSION OF ONE PERCENT ON TRANSFER: N{commission}" + "\n")
                    file.write(f"TOTAL COMMISSION ACCRUED: N{bank_coffers}" + "\n")
                    file.close()

                    another()
                else:
                    print("INSUFFICIENT BALANCE")

            else:
                print("ENTER CORRECT NAME")
                transfer()
        else:
            print("ENTER CORRECT NAME")
            transfer()


def summary():
    file = open("flipped.py", "r")
    readfile = file.read()
    file.close()
    print(readfile)
    file = open("flipped.py", "w")
    file.write(readfile)
    file.close()
    back()


def quit():
    print("""
ARE YOU SURE YOU WANT TO LOG-OUT?

1 - BACK TO HOME
2 - LOG-OUT""")
    try:
        command = int(input(">: "))
    except ValueError:
        print("INVALID COMMAND")
    else:

        if command == 1:
            home()

        elif command == 2:
            print("THANK YOU FOR USING THIS SERVICE. GOODBYE!!!")
            login()

        else:
            print("INVALID COMMAND")
            quit()


def home():
    while True:
        print("""
    WELCOME TO BEAR BEAR COMMUNITY BANK
    PRESS 1 PERFORM A TRANSFER
    PRESS 2 TO PRINT CUSTOMER BALANCE  
    PRESS 3 TO PRINT BANK PROFIT AND BREAKDOWN
    PRESS 4 TO ADD CUSTOMER
    PRESS 5 TO REMOVE CUSTOMER
    PRESS 6 CLEAR BREAKDOWN PAGE
    PRESS 7 TO VIEW CUSTOMER LIST AND ACCOUNT BALANCE
    PRESS 8 TO LOGOUT
    """)
        try:
            press = int(input(">: "))
        except ValueError:
            print("INVALID COMMAND")
        else:
            if press == 1:
                transfer()

            elif press == 2:
                customer_details()

            elif press == 3:
                if path.exists("flipped.py"):
                    summary()
                else:
                    print("NO DATA ENTRIES")
                    back()

            elif press == 4:
                add()

            elif press == 5:
                remove()

            elif press == 6:
                if path.exists("flipped.py"):
                    os.remove("flipped.py")
                    print("BREAKDOWN PAGE HAS BEEN CLEARED SUCCESSFULLY")
                    back()
                else:
                    print("FILE DOES NOT EXIST")
                    back()


            elif press == 7:
                for client in customers_balance:
                    print(client, ":", customers_balance[client])

                back()

            elif press == 8:
                quit()


login()
