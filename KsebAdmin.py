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
    elif(choice == 3):
        print("Delete Consumer Selected")
    elif(choice == 4):
        print("Update Consumer selected")
    elif(choice == 5):
        print("View All Consumer selected")
    elif(choice == 6):
        print("Generate Bill selected")
    elif(choice == 7):
        print("View Bill selected")
    elif(choice == 8):
        print("Exit")
        break
    