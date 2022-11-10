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
    