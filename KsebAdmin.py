import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'ksebdb')

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
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if(choice == 1):
        print("Add consumer selected")
        consumerCode = input("Enter the consumer code: ")
        consumerName = input("Enter the consumer name: ")
        consumerPhone = input("Enter the consumer phone: ")
        consumerEmail = input("Enter the consumer email id: ")
        consumerAddress = input("Enter the consumer address: ")
        sql = "INSERT INTO `consumer`(`consumerCode`, `consumerName`, `consumerPhone`, `consumerEmail`, `consumerAddress`) VALUES (%s,%s,%s,%s,%s)"
        data = (consumerCode,consumerName,consumerPhone,consumerEmail,consumerAddress)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data inserted successfully")
    elif(choice == 2):
        print("Search Consumer selected")
        searchOption = input("Enter the Consumer Code/Name/Phone to search: ")
        sql = "SELECT `consumerCode`, `consumerName`, `consumerPhone`, `consumerEmail`, `consumerAddress` FROM `consumer` WHERE `consumerCode` ='"+searchOption+"'  OR `consumerName`='"+searchOption+"' OR `consumerPhone` ='"+searchOption+"' "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice == 3):
        print("Delete Consumer Selected")
        consumerCode = input("Enter the consumer code to delete: ")
        sql = "DELETE FROM `consumer` WHERE `consumerCode` = "+consumerCode
        mycursor.execute(sql)
        mydb.commit()
        print("Data deleted successfully.")
    elif(choice == 4):
        print("Update Consumer selected")
        consumerCode = input("Enter the consumer code to update consumer: ")
        consumerName = input("Enter the consumer name to update: ")
        consumerPhone = input("Enter the consumer phone to update: ")
        consumerEmail = input("Enter the consumer email id to update: ")
        consumerAddress = input("Enter the consumer address to update: ")
        sql = "UPDATE `consumer` SET `consumerName`='"+consumerName+"',`consumerPhone`='"+consumerPhone+"',`consumerEmail`='"+consumerEmail+"',`consumerAddress`='"+consumerAddress+"' WHERE `consumerCode` = "+consumerCode
        mycursor.execute(sql)
        mydb.commit()
        print("Data updated successfully")
    elif(choice == 5):
        print("View All Consumer selected")
        sql = "SELECT `consumerCode`, `consumerName`, `consumerPhone`, `consumerEmail`, `consumerAddress` FROM `consumer` "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice == 6):
        print("Generate Bill selected")
        consumerCode = input("Enter the consumer code: ")
        sql = "SELECT `id` FROM `consumer` WHERE `consumerCode` = "+consumerCode
        mycursor.execute(sql)
        result = mycursor.fetchone()
        consumerId = result[0]

        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        currentMonth = str(currentMonth)
        currentYear = str(currentYear)

        sql = "select SUM(`unit`) from usages where month(datetime) = '"+currentMonth+"' AND year(datetime) = '"+currentYear+"' AND `consumerid` ="+str(consumerId)
        mycursor.execute(sql)
        result = mycursor.fetchone()
        sumOfUnit = result[0]
        print("Total Unit used : ",sumOfUnit)
        totalAmount = int(sumOfUnit)*5
        print("Total amount: ",totalAmount)


        sql = "INSERT INTO `bill`(`consumerid`, `month`, `year`, `bill`, `paidstatus`, `billdate`, `totalunit`) VALUES (%s,%s,%s,%s,%s,now(),%s)"
        data = (consumerId,currentMonth,currentYear,totalAmount,'0',sumOfUnit)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Bill inserted successfully.")

            
    elif(choice == 7):
        print("View Bill selected")
    elif(choice == 8):
        print("Exit")
        break
    