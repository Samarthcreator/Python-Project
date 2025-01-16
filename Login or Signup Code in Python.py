choice = "y"
Name=[]
ul = []
pl = []
sqans=[]
mnumber = []
while choice[0] =="y":
    num = int(input("Enter 1. for Signup and 2. for Sign in "))
    if num ==2:
        username = input("Enter the your username")
        for i in range(len(ul)):
            if username==ul[i]:
                password = input("Enter your password")
                if password==pl[i]:
                    print("Successfully logged in")
                    break
                else:
                    print("Invali Password")
                    temp = input("do you want to forget passwor, type yes or no:").upper()
                    if temp[0]=="Y":
                        sq =input("What is your nickname").lower()
                        if sq==sqans[i]:
                            password =input("Enter your new password")
                            pl.insert(i,password)
                            break
                        else:
                            print("Wrong answer")
                            break
            elif len(ul)==i+1:
                print("Invalid username")

    elif num ==1:
        name = input("Enter your name")
        Name.append(name)
        point1 =1
        while point1==1:
            username = input("Enter the your username")
            if username in ul:
                print("already exist username")
            else:
                point1=0
        point2, point3, point4=0,0,0
        point1 =0
        while point1==0:
            password = input("Enter your password")
            if len(password)>=8:
                for i in password:
                    if i.isupper():
                        point1=1
                    if i.islower():
                        point2=1
                    if i in "123456789":
                        point3=1
                    if i in "!@#$%^&*?":
                        point4=1
            if point1==point2==point3==point4==1:
                ul.append(username)
                pl.append(password)
                point1=1
            else:
                print("Your Password is weak")
        point1=0
        while point1<0 or point1>10:
            number = input("Enter your 10 digit mobile number")
            if len(number)==10:
                for j in number:
                    if j in "0123456789":
                        point1=point1+1
            if point1==10:
                mnumber.append(number)
            else:
                print("Wrong Number Re enter again")
        sq = input("What is your nickname").lower()
        sqans.append(sq)
        print("Successfully Signed in")
    else:
        print("Invalid choices or input")
        continue
    choice = input("Do you want to login or signup again, type yes or no").lower()