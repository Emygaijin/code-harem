def name(Firstname="Emeka", Surname="Ehibudu", Account=1239094764):
    print(Firstname, Surname, "\nAccount Number - ", Account)


def transfer():
    print("""
SELECT A BANK

1 > ACCESS BANK
2 > FIRST BANK
2 > GT BANK
4 > UNION BANK
5 > FIDELITY BANK""")

    send = int(input("> :"))
    if send == 1:
        access()
    elif send == 2:
        first_bank()
    elif send == 3:
        gtb()
    elif send == 4:
        union()
    elif send == 5:
        fidelity()
    else:
        invalid()
        transfer()


def new_send():
    print("""
WOULD YOU LIKE TO MAKE ANOTHER TRANSFER?

1 > TRANSFER
2 > MAIN MENU
3 > EXIT""")
    another = int(input("> "))
    if another == 1:
        transfer()
    elif another == 2:
        menu()
    elif another == 3:
        quit()
    else:
        invalid()
        new_send()


def account():
    account_number = input("ENTER ACCOUNT NUMBER: ")
    if len(account_number) == 10:
        money = int(input("ENTER AMOUNT: "))
        if money >= 1000 and money <= 5000000:
            passcode = input("Enter password: ")
            if len(passcode) == 4:
                print(f"TRANSFER OF N{money} TO ACCOUNT NUMBER {account_number} SUCCESSFUL")
                new_send()
        else:
            print("TRANSFER LIMIT BETWEEN N1000 AND N5000000")
            account()
    else:
        print("ENTER CORRECT ACCOUNT NUMBER")
        account()


def access():
    account()


def gtb():
    account()


def first_bank():
    account()


def fidelity():
    account()


def union():
    account()


def details():
    print("""
ACCOUNT NAME   > ADEMOLA ADEMULEGUN
ACCOUNT NUMBER > 4659098765""")
    back()


def cable():
    print("""
1 - DSTV
2 - GOTV
3 - STARTIMES""")
    point = int(input("> : "))
    if point == 1:
        dstv()
    elif point == 2:
        gotv()
    elif point == 3:
        startimes()
    else:
        invalid()
        cable()


def amount():
    print("""
1 > 1,000
2 > 5,000
3 > 10,000
4 > 20,000
5 > CANCEL""")
    choose = ""
    choose = int(input("> "))
    if choose == 1:
        cash()
        back()
    elif choose == 2:
        cash()
        back()
    elif choose == 3:
        cash()
        back()
    elif choose == 4:
        cash()
        back()
    elif choose == 5:
        back()
    else:
        invalid()
        back()


def cash():
    print("TAKE YOUR CASH")


def withdrawal():
    print("""
1 - SAVINGS
2 - CURRENT
3 - CREDIT""")
    pull = int(input("> "))
    if pull == 1:
        amount()

    elif pull == 2:
        amount()
    elif pull == 3:
        amount()
    else:
        invalid()
        withdrawal()


def invalid():
    print("Invalid command")


def airtime():
    print("""
CHOOSE A NETWORK PROVIDER

1 - MTN
2 - GLO
3 - AIRTEL
4 - ETISALAT""")
    choose = int(input(">: "))
    if choose == 1:
        mtn()
    elif choose == 2:
        glo()
    elif choose == 3:
        airtel()
    elif choose == 4:
        etisalat()
    else:
        invalid()
        airtime()


def mtn():
    print("Recharge successful")
    back()


def glo():
    print("Recharge successful")
    back()


def airtel():
    print("Recharge successful")
    back()


def etisalat():
    print("Recharge successful")
    back()


def back():
    print("""
1 - BACK TO MAIN MENU
2 - QUIT""")
    press = int(input(">: "))
    if press == 1:
        menu()
    elif press == 2:
        quit()
    else:
        invalid()
        back()


def quit():
    print("""
ARE YOU SURE YOU WANT TO EXIT?

1 - BACK TO MAIN MENU
2 - EXIT""")
    command = int(input(">: "))

    if command == 1:
        menu()
    elif command == 2:
        print("REMOVE YOUR CARD")

    else:
        invalid()
        quit()


def biller():
    print("""
1 - CABLE TV
2 - AIRTIME RECHARGE
3 - SPORTS BETTING""")
    sel = int(input(">: "))
    if sel == 1:
        cable()
    elif sel == 2:
        airtime()
    elif sel == 3:
        sportsbetting()
    else:
        invalid()
        biller()


def sportsbetting():
    print("This service is experiencing a downtime")
    back()


def cable():
    print("""
1 - DSTV
2 - GOTV
3 - STARTIMES""")
    point = int(input("> : "))
    if point == 1:
        dstv()
    elif point == 2:
        gotv()
    elif point == 3:
        startimes()
    else:
        invalid()
        cable()


def dstv():
    smart_card = input("Enter your 12 digit smart card number : ")
    if len(smart_card) == 12:
        pin = input("Enter your 4 digit pin: ")
        if len(pin) == 4:
            print("Your subsription has been extended")
            back()
        else:
            print("""
INCORECT PIN

""")
            dstv()

    else:
        print("""
ENTER CORRECT SMARTCARD NUMBER

    """)
        dstv()


def gotv():
    card = input("Enter your 10 digit card number: ")
    if len(card) == 10:
        code = input("Enter your 3 digit passcode: ")
        if len(code) == 3:
            print("Your subsription has been extended: ")
            back()
        else:
            print("invalid code")
            gotv()

    else:
        print("Enter valid card number")
        gotv()


def startimes():
    print("This service has not been enabled")
    back()


def bvn():
    print("Your BVN is, 127874647")
    back()


def menu():
    print("""
1 - ACCOUNT NUMBER
2 - RETRIEVE BVN
3 - BILL PAYMENT
4 - WITHDRAWAL
5 - TRANSFER
6 - EXIT""")
    pick = int(input("- "))
    while True:
        if pick == 1:
            name()
            back()

            break


        elif pick == 2:
            bvn()
            break


        elif pick == 3:
            biller()
            break

        elif pick == 4:
            withdrawal()

            break

        elif pick == 5:
            transfer()
            break
        elif pick == 6:
            quit()
            break
        else:
            invalid()
            menu()


def welcome():
    passcode = "1234"
    print("""
                WELCOME TO APTECH BANK      
                     ENTER PIN
                     
                     """)
    enter = ""
    enter = input("> ")
    if enter == passcode:
        menu()
    else:
        print("INCORRECT PIN")
        welcome()


welcome()


def startimes():
    print("ERROR 104")
    cable()
