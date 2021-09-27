import student as st
import teacher as t
import administrator as ad

def main_function():
    print("-----------Internal Assessment Score System-----------\n1.Login as Administrator\n4.Login as Teacher\n3.Login as Student")
    choice= int(input("Enter your choice:"))
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