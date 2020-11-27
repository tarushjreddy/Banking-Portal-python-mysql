import mysql.connector as connector
from DataBaseConnect import DatabaseConnector


def intro():
    while True:
        print("\t\t\t\t**************************************************************************************************************")
        print("\t\t\t\t\t\t\t\t\t\tBANK MANAGEMENT SYSTEM")
        print("\t\t\t\t**************************************************************************************************************")

        print("\t\t\t\tA Project by Tarush..")
        print("\t\t\t\t")
        print("\tMAIN MENU")
        print("\t1. CREATE NEW ACCOUNT")
        print("\t2. VIEW DETAILS OF THE YOUR ACCOUNT")
        print("\t3. DELETE YOUR ACCOUNT")
        print("\t4. BALANCE ENQIRY")
        print("\t5. DEPOSITE OR WITHDRAW AMOUNT FROM YOUR ACCOUNT")
        print("\t6. ENTER ADMIN PORTAL ONLY OFFICALS")
        print("\t7. VIEW YOUR TRANSACTION")

        print("\t8. EXIT BANK PORTAL")

        print("\tPlease enter your option from the following..")
        ch = int(input())
        print(f"The choice which you have entered is {ch}")

        if (ch <= 7):
            return ch
        elif (ch == 8):

            print("Thank You Please Visit Next Time...")
            break
        elif (ch >= 9):

            print("enter valid option")
            continue

        else:
            print("please refresh the portal\n")


option = intro()

if (option == 1):
    helper = DatabaseConnector()
    input("You have choose option 1 that is to Create a new account")
    accountnumber = input(
        "Enter your personalized account number\n")

    firstname = input("Enter your First Name")
    lastname = input("Enter your Last Name")
    DOB = input("Enter your DOB (YYY-MM-DD)")
    Contact = input("Enter your Contact Number")
    Amount = input("Enter the initial amount")
    Atm = input("please set your atm pin")
    Address = input("Enter your State")
    todadate = input("Enter the present day Date")
    PIN = input("Enter your PIN Code")
    Profession = input("Enter your Profession")
    helper.insertValues(accountnumber, firstname, lastname,
                        DOB, Contact, Address, todadate, Amount, Atm, PIN, Profession)

elif (option == 2):
    helper = DatabaseConnector()
    accountnumber = input(
        "Enter your personalized account number\n")
    helper.GetDetails(accountnumber)

elif (option == 3):
    helper = DatabaseConnector()
    accountnumber = input(
        "Enter your personalized account number\n")
    helper.deleteAccount(accountnumber)
    print("Thank You please visit again")

elif (option == 4):

    helper = DatabaseConnector()
    accountnumber = input(
        "Enter your personalized account number\n")
    helper.BalanceEnquiry(accountnumber)

elif (option == 6):

    helper = DatabaseConnector()
    print("**You have entered Admin Portal**\n")
    print("**Please enter your password**\n")
    passs = input()
    if (passs == "Sachin"):
        helper.DataReterival()

elif (option == 5):
    helper = DatabaseConnector()
    accountnumber = input(
        "Enter your personalized account number\n")
    helper.depositeWith(accountnumber)
elif (option == 7):
    helper = DatabaseConnector()
    accountnumber = input(
        "Enter your personalized account number\n")
    helper.Trasacz(accountnumber)
