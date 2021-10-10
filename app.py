import student as st
import teacher as t
import admin as ad
import details as dt

def main_function():
    print("----------------Internal Assessment Score System-------------------")
    data=["1.Login as Administrator 2.Login as Teacher 3.Login as Student"]
    table =dt.get_pretty_table(data)
    print(table)
    choice=int(input("Choice:"))
    if choice==1:
        ad.main_function()
    elif choice==2:
        t.main_function()
    elif choice==3:
        st.main_function()
    else:
        print("Invalid Choice.")
        exit()

if __name__=="__main__":
    main_function()
 
 
