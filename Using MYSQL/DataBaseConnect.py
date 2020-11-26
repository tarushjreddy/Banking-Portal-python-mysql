import mysql.connector as connector


class DatabaseConnector:
    def __init__(self):
        self.test = connector.connect(host="localhost", port="3306", user="root",
                                      password="omsairam", database="pythontest")
        query = "CREATE TABLE IF NOT EXISTS CUSTOMERS(Acc_no int(30) NOT NULL, First_name varchar(30) NOT NULL, Last_name varchar(30) NOT NULL,DOB date NOT NULL, Contact_No bigint(12) NOT NULL,Address varchar(50) NOT NULL, Created_on date NOT NULL, Amount int(11) NOT NULL, ATM_NO bigint(20) NOT NULL, PIN int(11) NOT NULL, Emp_id varchar(30) NOT NULL, PRIMARY KEY(Acc_no),UNIQUE KEY ATM_NO(ATM_NO),KEY Emp_id(Emp_id) ) "
        queryone = "CREATE TABLE IF NOT EXISTS Transaction( Trans_id int(11) NOT NULL AUTO_INCREMENT, Date date NOT NULL, Acc_no1 int(11) DEFAULT NULL, Acc_no2 int(11) DEFAULT NULL, Remark varchar(30) NOT NULL, Amount int(11) NOT NULL, Emp_id varchar(30) NOT NULL, PRIMARY KEY(Trans_id), KEY Acc_no1(Acc_no1),KEY Emp_id(Emp_id), KEY Acc_no2(Acc_no2)) "
        cur = self.test.cursor()
        cur.execute(query)
        cur.execute(queryone)
        print("table is created")

    def insertValues(self, Acc_no, First_name, Last_name, DOB, Contact_No, Address, Created_on, Amount, ATM_NO, PIN, Emp_id):

        querytwo = "INSERT INTO CUSTOMERS(Acc_no, First_name, Last_name, DOB, Contact_No, Address, Created_on, Amount, ATM_NO, PIN, Emp_id) VALUES({}, '{}', '{}', '{}', {}, '{}', '{}', {}, {}, {}, '{}');".format(
            Acc_no, First_name, Last_name, DOB, Contact_No, Address, Created_on, Amount, ATM_NO, PIN, Emp_id)
        cuc = self.test.cursor()
        cuc.execute(querytwo)
        self.test.commit()

        print("the data is saved to DB!!")
        # helper.insertValues(1238153062, 'Ranbeer', 'Kapoor', '2002-02-03', 9421356821,
#                     'Punjab', '2014-11-03', 8001000, 4591996880438644, 1730, 'alex_banker')
# helper.insertValues(1237912995, 'Deepika', 'Padukone', '2003-03-03', 9421352012,
#                     'Bengaluru', '2014-11-03', 4003900, 4591720349994488, 5125, 'alex_banker')

    def DataReterival(self):

        querythree = "select * from CUSTOMERS"
        cuo = self.test.cursor()
        cuo.execute(querythree)
        print("Account NO" "\t" "")
        print(cuo)
        for row in cuo:

            print(str(row[0]) + "\t" + str(row[1]) + str(row[2]))
        #   "\t" + str(row[4]) + "\t" + str(row[5]) + "\t" + str(row[6]))
        #  str(row[4]) + "\t" + str(row[5]) + "\t" + str(row[6]) + "\t" str(row[7]) + "\t" str(row[8]) + "\t" + str(row[9]) + "\t" + str(row[10]) + "\t" + str(row[11]) + "\t")

    def GetDetails(self, Acc_no):
        queryfour = f"select * from CUSTOMERS WHERE Acc_no = {Acc_no} "
        deg = self.test.cursor()
        deg.execute(queryfour)
        for row in deg:
            for i in range(10):
                print(str(row[i]) + "\t" + str(row[i+1]))

    def deleteAccount(self, Acc_no):
        queryfive = f"DELETE from CUSTOMERS WHERE Acc_no = {Acc_no} "
        deg = self.test.cursor()
        deg.execute(queryfive)
        self.test.commit()

    def updateAccount(self, Acc_no):
        while True:
            print("Account Update Management System")
            print("\tMAIN MENU")
            print("\t1. First Name")
            print("\t2. Last Name")
            print("\t3. Date of Birth")
            print("\t4. Contact Number")
            print("\t5. Pin")
            print("\t6. Emp ID")
            print("\t7. Exit")

            ch = int(input("enter the option\n"))
            if (ch <= 6):
                return ch
                break
            elif (ch == 7):
                break
            else:

                print("enter valid option")
                continue

        if (ch == 1):
            First_name = input("enter thr first Name\n")
            queryfive = f"UPDATE CUSTOMERS SET First_name='{First_name}' WHERE Acc_no = {Acc_no} "
            deg = self.test.cursor()
            deg.execute(queryfive)
            self.test.commit()
