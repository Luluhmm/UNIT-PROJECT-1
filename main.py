from nurse import *

def nursemenu():
    while True:
        print("Availabe Operations: ")
        print("1. View Patients ")
        print("2. Add Patients ")
        print("3. Exit ")
        choice = input("Please enter your choice from the menu shown and type 'exit' to quit:  ")
        
        if choice == "1":
            view_patients()
            
        elif choice == "2":
            add_patient()
        
        elif choice == "3":
            update_status()
            
        elif choice == "4":
            triggeralert()
           
        elif choice == "5":
            print("Goodbye Nurse!Thank you for your effort and joining yaqeth alert system!")
            break
        else :
            print("Invalid option")


if __name__ == "__main__":
    mainrole = input("Welcome to Yaqeth Alert System! \n Are you a (Dr/Nurse)?  ")
    if mainrole.lower() == "nurse":
        nursemenu()
    else:
        print("not a nurse")