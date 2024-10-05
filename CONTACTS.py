def checkNumber(num):
    for c in contacts:
            if number!=c :
                print("CONTACT Number doesn't EXIST")
                return True
    return False




contacts = {'123':'abcd','345':'defg','567':'ghij'}

while True:
    ch= int(input("\n\nEnter CHOCE:\n1.Add new contact\n2.Update a contact\n3.Delete a contact\n4.Show all contacts\n5.Exit"))
    if ch == 1:
        number = input("Enter a number to Add:")
        name = input("Enter Name to Add:")
        contacts[number]= name
        print("CONTACT ADDED SUCCESSFULLY!!")
    elif ch == 2:
        number = input("Enter Number to Update:")
        name = input("Enter New Name:")
        contacts.update({number:name})
        print("CONTACT UPDATED SUCCESSFULLY!!")
    elif ch == 3:
        number = input("Enter Number to Delete:")
        if checkNumber(number):
            print("Number isn't Found")
        else:
         contacts.pop(number)
         print("CONTACT DELETED SUCCESSFULLY!!")
               
    elif ch == 4:
        print("NAME\tNUMBER")
        for tu in contacts.items():
            print(tu[1],"\t",tu[0])
            
    elif ch == 5:
        print("EXITING!!!")
        break
    else:
        print("INVALID CHOICE!!!!!")

            
