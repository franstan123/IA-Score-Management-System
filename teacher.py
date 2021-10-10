import details as dt
from prettytable import PrettyTable
import app

def after_login():
    data = ["1.View All Student Details" "2.Update Student Marks" "3.Log Out"]
    table =dt.get_pretty_table(data)
    print(table)
    ch=input("Enter Choice: ")
    if ch==1 :
        View_All_Students()
    elif ch==2:
        Update_Student_Marks()
    elif ch==3:
        main_function()


def View_All_Students():
    f = open("student_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    X = PrettyTable()
    X.field_names = [ "USN" , "Name" , "D.O.B." , "Phone Number","Math","English","Hindi","Science","Social" ]
    for l in li:
        li2 = l.split('|')  
        X.add_row(li2)
    print(X)
    after_login()

def Update_Student_Marks():
    ans='y'
    while(ans=='y' or 'Y'):
        usn = input("Enter the USN: ")
        result = dt.get_student_by_usn(usn)
        if len(result) == 0:
            print("Student Details Not Found. ")
            main_function()
        else:
            X = PrettyTable()
            X.field_names = ["USN","Name" , "D.O.B.","Phone" , "Math" , "English" , "Hindi","Science","Scoial"]
            X.add_row(result)
            print(X)
            data = ["1.Update Math","2.Update English" ,"3.Update Hindi", "4.Update Science", "5.Update Social"]
            table =dt.get_pretty_table(data)
            print(table)
            ch= int(input("Enter your Choice:"))
            if ch == 1:
                math= input("Enter Math Mark:")
                result[4] = math
            elif ch == 2:
                eng = input("Enter English Mark:")
                result[5]= eng
            elif ch == 3:
                hin = input("Enter Hindi Mark: ")
                result[6] = hin
            elif ch == 4:
                sci = input("Enter Science Mark: ")
                result[7] = sci
            elif ch == 5:
                soc = input("Enter Social Mark: ")
                result[8] = soc
            f = open("student_record.txt","r")
            data = f.read()
            f.close()
            res_lst = []
            li = data.split('$')
            li.pop()
            for l in li:
                li2 = l.split('|')
                if usn == li2[1]:
                    res_lst.append('|'.join(result))
                else:
                    res_lst.append(1)
            book = '$'.join(res_lst) + '$'
            file = open("student_record.txt", "w")
            file.write(book)
            file.close()
            ans=input("Are there more Students to Update?(Y/N)")
    after_login()


def sign_in():
    name = input("Enter you Name:")
    tid = input("Enter your USN:")
    match_tid = dt.get_tid(tid)
    match_tname = dt.get_tname(name)
    if name == match_tname and tid == match_tid:
        print("Welcome ", name)
        after_login()
    else:
        print("Sorry! Student Account Not Found")
        main_function()


def main_function():
    print("-------Welcome Teacher-------\n1.Sign In\n2.Exit")
    choice = int(input("Enter Choice:"))
    if choice == 1:
        sign_in()
    elif choice == 2:
        app.main_function()
    else:
        print("Invalid Choice")
        exit()
