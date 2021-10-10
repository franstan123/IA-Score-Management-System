import getpass
import details as dt
import prettytable  as pt
import app

def Add_Student():
    Name = input("Enter the Name:")
    usn = input("Enter USN:")
    dob=input("Enter D.O.B.:")
    phone = input("Enter Phone No.:")
    math=0
    english=0
    hindi=0
    science=0
    social=0
    result = usn + '|' + Name + '|' + dob + '|' + str(phone) + '|' +str(math)+'|'+str(english)+'|'+str(hindi)+'|'+str(science)+ '|'+str(social)+ '$'
    file = open("student_record.txt", "a")
    file.write(result)
    file.close()
    print("---Added Successfully---")
    after_login()

def Add_Teacher():
    Name = input("Enter the Teacher Name:")
    Id = input("Enter the Teacher ID:")
    dob = input("Enter D.O.B.:")
    phone = input("Enter Phone Number:")
    subject = input("Enter Faculty Subject: ")
    result =  Id + '|' + Name +'|' + dob + '|' + str(phone) + '|' + subject + '$'
    file = open("teacher_record.txt", "a")
    file.write(result)
    file.close()
    after_login()


def View_All_Students():
    f = open("student_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    X = pt.PrettyTable()
    X.field_names = [ "USN" , "Name" , "D.O.B." , "Phone Number","Math","English","Hindi","Science","Social" ]
    for l in li:
        li2 = l.split('|')  
        X.add_row(li2)
    print(X)
    after_login()

def View_All_Teachers():
    f = open("teacher_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    X = pt.PrettyTable()
    X.field_names = [ "ID" , "Name" , "D.O.B." , "Phone Number" , "Subject" ]
    for l in li:
        li2 = l.split('|')  
        X.add_row(li2)
    print(X)
    after_login()

def Update_Teacher():
    tID = input("Enter the Teacher ID: ")
    result = dt.get_teacher_by_id(tID)
    if len(result) == 0:
        print("Teacher Details Not Found. ")
    else:
        X = pt.PrettyTable()
        X.field_names = ["ID","Name" , "D.O.B.", "Phone" , "Subject" ]
        X.add_row(result)
        print(X)
        data = ["1.Update ID","2. Update Name" , "3.Update D.O.B.", "4.Update Phone" , "5.Update Subject" ]
        table =dt.get_pretty_table(data)
        print(table)
        ch= int(input("Enter your Choice:"))
        if ch == 1:
            id = input("Enter New id:")
            result[0] = id
        elif ch == 2:
            name = input("Enter New Name:")
            result[2]= name
        elif ch == 3:
            dob = input("Enter New DOB: ")
            result[3] = dob
        elif ch == 4:
            phone = input("Enter New Phone No.:")
            result[4] = phone
        f = open("teacher_record.txt","r")
        data = f.read()
        f.close()
        res_lst = []
        li = data.split('$')
        li.pop()
        for l in li:
            li2 = l.split('|')
            if tID == li2[1]:
                res_lst.append('|'.join(result))
            else:
                res_lst.append(1)
        book = '$'.join(res_lst) + '$'
        file = open("Book_Details.txt", "w")
        file.write(book)
        file.close()
        after_login()


def Update_Student():
    usn = input("Enter the USN: ")
    result = dt.get_student_by_usn(usn)
    if len(result) == 0:
        print("Student Details Not Found. ")
    else:
        X = pt.PrettyTable()
        X.field_names = ["USN","Name" , "D.O.B.","Phone" , "Math" , "English" , "Hindi","Science","Scoial"]
        X.add_row(result)
        print(X)
        data = ["1.Update USN","2.Update Name" ,"3.Update D.O.B.", "4.Update Phone"]
        table =dt.get_pretty_table(data)
        print(table)
        ch= int(input("Enter your Choice:"))
        if ch == 1:
            usnn= input("Enter New USN:")
            result[0] = usnn
        elif ch == 2:
            name = input("Enter New Name:")
            result[2]= name
        elif ch == 3:
            phone = input("Enter New Phone No.: ")
            result[3] = phone
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
        after_login()

def Delete_Student():
    usn=str(input("Enter USN:"))
    dt.delete_student_by_usn(usn)
    f = open("student_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    X = pt.PrettyTable()
    X.field_names = ["USN" , "Name" , "D.O.B." ,"Phone Number" , "Math" , "English" , "Hindi" , "Science","Social"]
    for l in li:
        li2 = l.split('|')  
        X.add_row(li2)
    print(X)
    ch=input("Continue?(Y/N")
    if ch=='Y' or 'y':
        after_login()
    else:
        pass
    
def Delete_Teacher():
    tid=str(input("Enter Teacher's ID:"))
    dt.delete_student_by_usn(tid)
    f = open("teacher_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    X = pt.PrettyTable()
    X.field_names = ["ID" , "Name" , "D.O.B." ,"Phone Number" , "Subject"]
    for l in li:
        li2 = l.split('|')  
        X.add_row(li2)
    print(X)
    after_login()

def main_function():
    username=input("Enter you Username:")
    password = getpass.getpass("Enter your Password:")
    if username == "admin" and password == "admin":
        print("--------Welcome Admin----------")
        after_login()
    else:
        print("Sorry! Invalid Password")
        main_function()

def after_login():
    data = ["1.Add Student","2.Add Teacher" , "3.View Students", "4.View Teachers",  "5.Delete Student", "6.Delete Teacher", "7.Update Teacher","8.Update Student","9.LogOut"]
    table= dt.get_pretty_table(data)
    print(table)
    ch = int(input("Enter your Choice:"))
    if ch == 1:
        Add_Student()
    elif ch == 2:
        Add_Teacher()
    elif ch == 3:
        View_All_Students()
    elif ch == 4:
        View_All_Teachers()
    elif ch == 5:
        Delete_Student()
    elif ch == 6:
        Delete_Teacher()
    elif ch==7:
        Update_Teacher()
    elif ch==8:
        Update_Student()
    elif ch == 9:
        app.main_function()


