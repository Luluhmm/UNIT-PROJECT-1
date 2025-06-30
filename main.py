from nurse import *
from doctor import *


def nursemenu(username):
    while True:
        print("Availabe Operations: ")
        print("1. View Patients ")
        print("2. Add Patients ")
        print("3. Update Patients Status ")
        print("4. Trigger Alert - Page Doctor ")
        print("5. Exit ")
        choice = input("Please enter your choice from the menu shown and type '5' to quit:  ")
        
        if choice == "1":
            view_patients()
            
        elif choice == "2":
            add_patient(username)
        
        elif choice == "3":
            update_status(username)
            
        elif choice == "4":
            triggeralert(username)
           
        elif choice == "5":
            print("Goodbye Nurse!Thank you for your effort and joining yaqeth alert system!")
            break
        else :
            print("Invalid option")
            
def doctormenu(username):
    while True:
        print("Availabe Operations: ")
        print("1. View Critical Patients ")
        print("2. View Pateint Details and history ")
        print("3. Add Note to Nurse ")
        print("4. View Patient History Chart")
        print("5. Exit ")
        choice = input("Please enter your choice from the menu shown and type '5' to quit:  ")
        
        if choice == "1":
            view_critical()
            
        elif choice == "2":
            view_patient()
        
        elif choice == "3":
            add_note(drname)
        
        elif choice == "4":
            plotHistory()
            
        elif choice == "5":
            print("Goodbye Dr!Thank you for your effort and joining yaqeth alert system!")
            break
           
        else :
            print("Invalid option")






if __name__ == "__main__":
    mainrole = input("Welcome to Yaqeth Alert System! \n Are you a (Dr/Nurse)?  ")
    if mainrole.lower() == "nurse":
        nurses = load_data("/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/nurses.json")
        
        while True:
            username = input("Nurse Username: ").strip()
            password = input("Password :").strip()
    
            if username.isalpha() and password.isdigit():
                break
            else:
                print("Username must be Characters and Password must be PIN numbers only.")
         
        if username in nurses and nurses[username] == password:
            print(f"Welcome Nurse {username}")
            nursemenu(username)
        else:
            print("Invalid Nurse Credentials")
            
 #--------------------------------------------------------------------------------------------------------------      
    elif mainrole.lower() == "dr":
        doctors = load_data("/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/doctors.json")
        
        while True:
            drname = input("Doctor Username: ").strip()
            drpassword = input("Password: ").strip()
            if drname.isalpha() and drpassword.isdigit() :
                break
            else:
                print("Username must be Characters and Password must be PIN numbers only.")
                
                
        if drname in doctors and doctors[drname] == drpassword:
            print(f"Welcome Dr. {drname}")
            doctormenu(drname)
        else:
            print("Invalid Doctor Credentials")
    else:
        print("Invalid Role. Yaqeth accepts Nurses & Doctors only ")