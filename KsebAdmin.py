import mysql.connector
from datetime import datetime
import random
from tabulate import tabulate

try:
    mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'ksebdb')
except mysql.connector.Error as e:
    print(e)
mycursor = mydb.cursor()

while(True):
    print("Kseb Consumer Management")
    print("Select your option")
    print("1. Add Consumer")
    print("2. Search Consumer")
    print("3. Delete Conumer")
    print("4. Update Consumer")
    print("5. View all Consumer")
    print("6. Generate Bill")
    print("7. View Bill")
    print("8. Top two high bill paying customer")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if(choice == 1):
        print("Add consumer selected")
        consumerCode = input("Enter the consumer code: ")
        consumerName = input("Enter the consumer name: ")
        consumerPhone = input("Enter the consumer phone: ")
        consumerEmail = input("Enter the consumer email id: ")
        consumerAddress = input("Enter the consumer address: ")
        try:
            sql = "INSERT INTO `consumer`(`consumerCode`, `consumerName`, `consumerPhone`, `consumerEmail`, `consumerAddress`) VALUES (%s,%s,%s,%s,%s)"
            data = (consumerCode,consumerName,consumerPhone,consumerEmail,consumerAddress)
            mycursor.execute(sql,data)
            mydb.commit()
        except mysql.connector.Error as e:
            print(e)
        print("Data inserted successfully")
    elif(choice == 2):
        print("Search Consumer selected")
        searchOption = input("Enter the Consumer Code/Name/Phone to search: ")
        try:
            sql = "SELECT `consumerCode`, `consumerName`, `consumerPhone`, `consumerEmail`, `consumerAddress` FROM `consumer` WHERE `consumerCode` ='"+searchOption+"'  OR `consumerName`='"+searchOption+"' OR `consumerPhone` ='"+searchOption+"' "
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            print(e)

        print(tabulate(result,headers=["ConsumerCode","ConsumerName","ConsumerPhone","ConsumerEmail","ConsumerAddress"],tablefmt="psql"))
    elif(choice == 3):
        print("Delete Consumer Selected")
        consumerCode = input("Enter the consumer code to delete: ")
        try:
            sql = "DELETE FROM `consumer` WHERE `consumerCode` = "+consumerCode
            mycursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as e:
            print(e)
        print("Data deleted successfully.")
    elif(choice == 4):
        print("Update Consumer selected")
        consumerCode = input("Enter the consumer code to update consumer: ")
        consumerName = input("Enter the consumer name to update: ")
        consumerPhone = input("Enter the consumer phone to update: ")
        consumerEmail = input("Enter the consumer email id to update: ")
        consumerAddress = input("Enter the consumer address to update: ")
        try:
            sql = "UPDATE `consumer` SET `consumerName`='"+consumerName+"',`consumerPhone`='"+consumerPhone+"',`consumerEmail`='"+consumerEmail+"',`consumerAddress`='"+consumerAddress+"' WHERE `consumerCode` = "+consumerCode
            mycursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as e:
            print(e)
        print("Data updated successfully")
    elif(choice == 5):
        print("View All Consumer selected")
        try:
            sql = "SELECT `consumerCode`, `consumerName`, `consumerPhone`, `consumerEmail`, `consumerAddress` FROM `consumer` "
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
        print(tabulate(result,headers=["ConsumerCode","ConsumerName","ConsumerPhone","ConsumerEmail","ConsumerAddress"],tablefmt="psql"))
    elif(choice == 6):

        print("Generate Bill selected")

        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        currentMonth = str(currentMonth)
        currentYear = str(currentYear)
        try:
            sql = "DELETE FROM `bill` WHERE `month` ='"+currentMonth+"'  AND `year` ='"+currentYear+"'"
            mycursor.execute(sql)
            mydb.commit()
        except mysql.connector.Error as e:
            print(e)
        print("Previous data deleted.")
        try:
            sql = "SELECT `id` FROM `consumer`"
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            print(e)

        for i in result:
            conId = str(i[0])
            try:
                sql = "select SUM(`unit`) from usages where month(datetime) = '"+currentMonth+"' AND year(datetime) = '"+currentYear+"' AND `consumerid` ="+conId
                mycursor.execute(sql)
                result = mycursor.fetchone()
                sumOfUnit = result[0]
            
                totalAmount = int(sumOfUnit)*5
            
                invoice = random.randint(10000,100000)

            
                sql = "INSERT INTO `bill`(`consumerid`, `month`, `year`, `bill`, `paidstatus`, `billdate`, `totalunit`, `duedate`, `invoice`) VALUES (%s,%s,%s,%s,%s,now(),%s,now()+ interval 14 day,%s)"
                data = (conId,currentMonth,currentYear,totalAmount,'0',sumOfUnit,invoice)
                mycursor.execute(sql,data)
                mydb.commit()
            except mysql.connector.Error as e:
                print(e)
        print("Data inserted successfully")  
     
            
    elif(choice == 7):
        print("View Bill selected")
        try:
            sql = "SELECT  b.`consumerid`, b.`month`, b.`year`, b.`bill`, b.`paidstatus`, b.`billdate`, b.`totalunit`, b.`duedate`, b.`invoice`,c.consumerCode,c.consumerName FROM `bill` b JOIN consumer c ON b.consumerid=c.id"
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
        print(tabulate(result,headers=["ConsumerID","Month","Year","Bill","PaidStatus","BillDate","TotalUnit","DueDate","Invoice","ConsumerCode","ConsumerName"],tablefmt="psql"))
        
    elif(choice == 8):
        print("Top two high amount bill paying consumers")
        try:
            sql = "SELECT c.consumerName,c.consumerAddress,b.`totalunit`, b.`bill` FROM bill b JOIN consumer c ON b.consumerid = c.id GROUP BY `bill` ORDER BY `bill` DESC LIMIT 0,2"
            mycursor.execute(sql)
            result = mycursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
        print(tabulate(result,headers=["ConsumerName","Address","TotalUnit","Amount"],tablefmt="psql"))
    elif(choice == 9):
        print("Exit")
        break
    