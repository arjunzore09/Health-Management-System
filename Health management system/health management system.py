import datetime
def getdate():
    now= datetime.datetime.now()
    formatted_now=now.strftime("%Y-%m-%d %I:%M:%S:%p")
    return formatted_now
id=["Virat","Rohit","Rahul"]
password=[12,34,56]
x=int(input("Press the number you have to following name:\n(1) For Virat\n(2) For Rohit\n(3) For Rahul\n"))
if x==1:
    user = input("Enter the valid id: ")
    userpass = int(input("Enter the valid password:"))
    if user == id[0] and userpass == password[0]:
        s=str(input("What do you want Virat food list or exercise list??\n"))
        if s.capitalize() =="Food" :
            y = str(input("What do you want to write or read??\n"))
            if y.capitalize() =="Write":
                print("[", getdate(), "]")
                f=open("Virat_food.txt","a")
                print("What you eat:")
                d=input()
                f.write(f" {getdate()} {d} \n")
                print("You have succesfully eneter.")
            elif y.capitalize() =="Read":
                print("[", getdate(), "]")
                f = open("Virat_food.txt")
                r = f.read()
                print(r)
            else:
                print("Invalid,please try again.")
        elif s.capitalize() =="Exercise":
            z = str(input("What do you want to write or read??\n"))
            if z.capitalize() =="Write":
                print("[",getdate(),"]")
                f=open("Virat_exersice.txt","a")
                d=input("What do you do today:")
                f.write(f" {getdate()} {d} \n")
                print("You have succesfully eneter.")
            elif z.capitalize() =="Read":
                print("[",getdate(),"]")
                f=open("Virat_exersice.txt")
                r=f.read()
                print(r)
            else:
                print("invalid,please try again.")
        else:
            print("invalid,please try again.")
    else:
        print("Invalid details")
elif x==2:
    user = input("Enter the valid id: ")
    userpass = int(input("Enter the valid password:"))
    if user == id[1] and userpass == password[1]:
        s=str(input("What do you want Rohit food list or exersice list??\n"))
        if s.capitalize() =="Food":
            y = str(input("What do you want to write or read??\n"))
            if y.capitalize() =="Write":
                print("[", getdate(), "]")
                f=open("Rohit_food.txt","a")
                d=input("What you eat??\n")
                f.write(f" {getdate()} {d} \n")
                print("You have succesfully eneter.")
            elif y.capitalize() =="Read":
                print("[", getdate(), "]")
                f = open("Rohit_food.txt")
                r = f.read()
                print(r)
            else:
                print("Invalid,please try again.")
        elif s.capitalize() =="Exersice":
            z = str(input("What do you want to write or read??\n"))
            if z.capitalize() =="Write":
                print("[",getdate(),"]")
                f=open("Rohit_exersice.txt","a")
                d=input("What do you do today:")
                f.write(f" {getdate()} {d} \n")
                print("You have succesfully eneter.")
            elif z.capitalize() =="Read":
                print("[",getdate(),"]")
                f=open("Rohit_exersice.txt")
                r=f.read()
                print(r)
            else:
                print("invalid,please try again.")
        else:
            print("invalid,please try again.")
    else:
        print("Invalid details")

elif x==3:
    user = input("Enter the valid id: ")
    userpass = int(input("Enter the valid password:"))
    if user == id[2] and userpass == password[2]:
        s=str(input("What do you want Rahul food list or exersice list??\n"))
        if s.capitalize() =="Food":
            y = str(input("What do you want to write or read??\n"))
            if y.capitalize() =="Write":
                print("[", getdate(), "]")
                f=open("Rahul_food.txt","a")
                print("What you eat:")
                d=input()
                f.write(f" {getdate()} {d} \n")
                print("You have succesfully eneter.")
            elif y.capitalize() =="Read":
                print("[", getdate(), "]")
                f = open("Rahul_food.txt")
                r = f.read()
                print(r)
            else:
                print("Invalid,please try again.")
        elif s.capitalize() =="Exersice":
            z = str(input("What do you want to write or read??\n"))
            if z.capitalize() =="Write":
                print("[",getdate(),"]")
                f=open("Rahul_exersice.txt","a")
                d=input("What do you do today:")
                f.write(f" {getdate()} {d} \n")
                print("You have succesfully eneter.")
            elif z.capitalize() =="Read":
                print("[",getdate(),"]")
                f=open("Rahul_exersice.txt")
                r=f.read()
                print(r)
            else:
                print("invalid,please try again.")
        else:
            print("invalid,please try again.")
    else:
        print("Invalid details!")
else:
    print("invalid, Please press the correct number.")
print("THANKS FOR USING:\nBY@ARJUN ZORE")