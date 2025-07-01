from nurse import *
from doctor import *
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from colorama import init, Fore, Style

init(autoreset=True)  # colorama init
console = Console()

def nursemenu(username):
    while True:
        table = Table(title="Nurse Menu", title_style="bold blue")
        table.add_column("Option", style="cyan")
        table.add_column("Operation", style="magenta")
        
        table.add_row("1", "View Patients ")
        table.add_row("2", "Add Patients ")
        table.add_row("3", "Update Patients Status ")
        table.add_row("4","Trigger Alert - Page Doctor ")
        table.add_row("5","Exit ")
        
        console.print(table)
        
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
            print(Fore.CYAN + "Goodbye Nurse!Thank you for your effort and joining yaqeth alert system!")
            break
        else :
            print("Invalid option")
            
def doctormenu(username):
    while True:
        table = Table(title="Doctor Menu",title_style="bold blue")
        table.add_column("Option", style="cyan")
        table.add_column("Operation", style="magenta")
        
        
        table.add_row("1", "View Critical Patients ")
        table.add_row("2", "View Pateint Details and history ")
        table.add_row("3", "Add Note to Nurse ")
        table.add_row("4", "View Patient History Chart")
        table.add_row("5", "Exit ")
        
        console.print(table)
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
            print(Fore.CYAN+ "Goodbye Dr!Thank you for your effort and joining yaqeth alert system!")
            break
           
        else :
            print("Invalid option")






if __name__ == "__main__":
    console.print(Panel("[bold blue]Welcome to Yaqeth Alert System[/bold blue]", expand=False, style="bold blue"))
    
    mainrole = input( "Are you a (Dr/Nurse)?  ").strip()
    if mainrole.lower() == "nurse":
        nurses = load_data("/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/nurses.json")
        
        while True:
            username = input("Nurse Username: ").strip()
            password = input("Password (PIN): ").strip()
    
            if username.isalpha() and password.isdigit():
                break
            else:
                print("Username must be Characters and Password must be PIN numbers only.")
         
        if username in nurses and nurses[username] == password:
            #print(f"Welcome Nurse {username}")
            console.print(f"[bold green]Welcome Nurse {username}![/bold green]")
            nursemenu(username)
        else:
            print("Invalid Nurse Credentials")
            
 #--------------------------------------------------------------------------------------------------------------      
    elif mainrole.lower() == "dr":
        doctors = load_data("/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/doctors.json")
        
        while True:
            drname = input("Doctor Username: ").strip()
            drpassword = input("Password (PIN): ").strip()
            if drname.isalpha() and drpassword.isdigit() :
                break
            else:
                print("Username must be Characters and Password must be PIN numbers only.")
                
                
        if drname in doctors and doctors[drname] == drpassword:
            #print(f"Welcome Dr. {drname}")
            console.print(f"[bold green]Welcome Dr. {drname}![/bold green]")
            doctormenu(drname)
        else:
            print("Invalid Doctor Credentials")
    else:
        print("Invalid Role. Yaqeth accepts Nurses & Doctors only ")