import prettytable as pt


def get_student_by_usn(usn):
    f = open("student_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if usn == li2[0]:
            return li2
    return []

def get_teacher_by_id(id):
    f = open("teacher_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if id == li2[0]:
            return li2
    return []

def get_usn(usn):
    f = open("student_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if usn == li2[0]:
            return usn
    return []

def get_name(name):
    f = open("student_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if name == li2[1]:
            return name
    return []

def get_tid(tid):
    f = open("teacher_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if tid == li2[0]:
            return tid
    return []

def get_tname(name):
    f = open("teacher_record.txt", "r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if name == li2[1]:
            return name
    return []


def get_pretty_table(li):
    table = pt.PrettyTable()
    table.field_names = ["Enter your choice:"]
    for i in li:
        table.add_row([i])
    return table


def delete_student_by_usn(usn):
    f = open("student_record.txt", "r")
    data = f.read()
    f.close()
    res_lst = []
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if usn == li2[0]:
            continue
        res_lst.append('|'.join(li2))
        udata = '$'.join(res_lst) + '$'
    file = open("student_record.txt", "w")
    file.write(udata)
    file.close()

def delete_teacher_by_tid(tid):
    f = open("teacher_record.txt", "r")
    data = f.read()
    f.close()
    res_lst = []
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if tid == li2[0]:
            continue
        res_lst.append('|'.join(li2))
        if res_lst==[]:
            udata=""
        else:
            udata = '$'.join(res_lst) + '$'
    file = open("teacher_record.txt", "w")
    file.write(udata)
    file.close()

