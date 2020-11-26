import mysql.connector as connector
from DataBaseConnect import DatabaseConnector


def intro():
    while True:
        print("\t\t\t\t**************************************************************************************************************")
        print("\t\t\t\t\t\t\t\t\t\tBANK MANAGEMENT SYSTEM")
        print("\t\t\t\t**************************************************************************************************************")

        print("\t\t\t\tA Project made by Tarush..")
        print("\t\t\t\t")
        print("\tMAIN MENU")
        print("\t1. NEW ACCOUNT")
        print("\t2. DEPOSIT AMOUNT")
        print("\t3. WITHDRAW AMOUNT")
        print("\t4. BALANCE ENQUIRY")
        print("\t5. ALL ACCOUNT HOLDER LIST")
        print("\t6. CLOSE AN ACCOUNT")
        print("\t7. MODIFY AN ACCOUNT")
        print("\t8. EXIT")
        print("\tPlease enter your option from the following..")
        ch = int(input())
        print(f"The choice which you have entered is {ch}")

        if (ch <= 6):
            return ch
        elif (ch == 7):

            print("Thank You Please Visit Next Time...")
            break
        elif (ch > 8):

            print("enter valid option")
            continue

        else:
            print("please refresh the portal\n")


option = intro()

if (option == "1"):
    helper = DatabaseConnector()
    input("You have choose option 1 that is to Create a new account")
    accountnumber = input(
        "Enter your personalized account number\n")

    firstname = input("Enter your First Name")
    lastname = input("Enter your Last Name")
    DOB = input("Enter your DOB (YYY-MM-DD)")
    Contact = input("Enter your Contact Number")
    Address = input("Enter your State")
    todadate = input("Enter the present day Date")
    PIN = input("Enter your PIN Code")
    Profession = input("Enter your Profession")
    helper.insertValues(accountnumber, firstname, lastname,
                        DOB, Contact, Address, todadate, PIN, Profession)
