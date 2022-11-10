import mysql.connector

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
    elif(choice == 7):
        print("View Bill selected")
    elif(choice == 8):
        print("Exit")
        break
    