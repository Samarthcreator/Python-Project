flag = True
total_points=0
sums = 0
medicine1 = ["Crocin", 10]
medicine2 = ["Paracetamol", 100]
medicine3 = ["Metxl", 450]
medicine4 = ["Pantakind", 110]
medicine5 = ["Rabekind", 1000]
again = "y"
while flag and (again=="y" or again=="Y"):
    visit = int(input("Enter the visit"))
    while flag:
        print("1.Rabekind -Rs.100 for 10")
        print("2.Paracetamol -Rs.10 for 10")
        print("3.Metxl - Rs.45 for 10")
        print("4.Pantakind - Rs. 100 for 10")
        print("5.Crocin -Rs. 5 for 10")
        num = input("Enter number for medicine you want or type n for total bill: ")
        if visit>=1:
            if num =="1":
                sums = sums+medicine5[1]
            elif num =="2":
                sums = sums+medicine2[1]
            elif num =="3":
                sums = sums+medicine3[1]
            elif num =="4":
                sums = sums+medicine4[1]
            elif num =="5":
                sums = sums+medicine1[1]
            if num == "N" or num == "n":
                if sums<1000:
                    print("your total bill is", sums, "you get no point")
                    flag = False
                if sums >=1000:
                    point = (sums-1000)//100
                    total_points = total_points+point
                    print("your total bill is ", sums, "you get ", total_points, "point")
                    if visit>1 and total_points>=10:
                        y=input("do you want to redeem points: ")
                       
                        if (y =="y" or y=="Y")  :
                            redeem=int(input("Enter points"))
                            if redeem<=total_points:
                                sums = sums - redeem*10
                                total_points = total_points-redeem
                                print("your total bill is ", sums, "you have remaining", total_points, "point")
                                
                            else:
                                print("Please enter valid number")   
                        if (y=="n" or y=="N"): 
                            print("your total bill is ", sums, "you have remaining", total_points, "point")
                    again=input("Do you want to continue:")
                    if again[0]=="y":
                        visit = int(input("Enter the visit"))
                        sums =0
                    else:
                        flag = False