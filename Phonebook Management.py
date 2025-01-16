# phone book management , add, search, update, dele
Run = "yes"
print("Welcome to Phone Book")
Names = []
Numbers = []

while Run[0] =="y":
    num =input("Please Enter any above number for your operation \n 1. Adding Contact \n 2. Updating Contact\n 3. Search Contact\n 4. Delete contact\n")
    count=0
    if num =="1":
        name = input("Enter the Name").lower()
        number = input("Enter the number")
        if len(number)==10 and name!= "":
            for i in number:
                if i in "0123456789":
                    count=count+1
            if count==10:
                Names.append(name)
                Numbers.append(number)
                print("Successfully Added")
            else:
                print("Number is not valid")
        else:
            print("Wrong input")
    elif num =="3":
        search =input("Enter number you want to search").lower()
        for i in range(0, len(Names)):
            if Numbers[i]==search:
                print("Name is", Names[i],"and Number is", Numbers[i])
            elif len(Names)==i+1:
                print("Not found")
    elif num=="2":
        search=input("Enter number you want to update")
        for i in range(len(Numbers)):
            if Numbers[i]==search:
                number=input("Enter new number")
                Numbers[i]=number
                print("Successfully Updated")
                break
            elif len(Names)==i+1:
                print("Not Found")
    elif num=="4":
        search=input("Enter the number you want to delete")
        for i in range(len(Numbers)):
            if Numbers[i]==search:
                Numbers.pop(i)
                Names.pop(i)
                print("Successfully Deleted")
                break
            elif len(Numbers)==i+1:
                print("Not Found")
    else:
        print("Invalid Input")
        continue
    Run = input("Do you want to repeat operation Type y for yes and n for no:").lower()