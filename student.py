import details as dt
import prettytable as pt
import app 

def after_login(usn):
    
    print("---------Login Success-------")
    f = open("students.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    X = pt.PrettyTable()
    for l in li:
        li2 = l.split('|')
        if usn == li2[0]:
             value=li2
        else: print("Record Not Found.")
    X.field_names = [ "USN" , "Name" , "D.O.B." , "Phone Number","Math","English","Hindi","Science","Social" ]
    X.add_row(value)
    print(X)
    ch=("Do you want to Sign Out?(Y/N)")
    if(ch=='Y' or ch=='y'):
        main_function()
    else:
        pass
        

def sign_in():
    name = input("Enter you Name:")
    usn = input("Enter your USN:")
    match_usn = dt.get_usn(usn)
    match_name = dt.get_name(name)
    if name == match_name and usn == match_usn:
        print("Welcome ", name)
        after_login(usn)
    else:
        print("Sorry! Student Account Not Found")
        main_function()


def main_function():
    print("-------Welcome Student-------\n1.Sign In\n2.Exit")
    choice = int(input("Enter Choice:"))
    if choice == 1:
        sign_in()
    elif choice == 2:
        app.main_function()
    else:
        print("Invalid Choice")
        exit()


