from data.support import load_data, save_data
from myalert import send_alert
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

console = Console() # this is an object to have more control over terminal using rich library
file_path = "/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/patients.json"
doctorsfile = "/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/doctors.json"

def view_patients():
    '''
    This function will give a high level overview about all patients stored and there status
    '''
    patients = load_data(file_path)
    if not patients:
        Console.print("[bold red]No patients stored yet.[/bold red]")
        #print("No patients stored yet")
        return
    else:
        table = Table(title="Patient List:",box=box.SIMPLE_HEAVY)
        table.add_column("ID",style="cyan",justify="center")
        table.add_column("Name",style="bold")
        table.add_column("Status",style="bold")
        table.add_column("Doctor",style="bold")
        
        
        for i, value in patients.items(): 
            table.add_row(
                i,
                value["name"],
                value["status"].capitalize(),
                value["doctor"]
            )
            #print(f"[{i}] {value['name']} - Status: {value['status']} - Responsible Doctor: {value['doctor']}")
        console.print(table)  
          
        for i,value in patients.items():
            console.print(f"\n[bold underline]Doctor Notes for Patient ID {i}:[/bold underline]")
            
            if value['notes']:
                for note in value['notes']:
                    console.print(f"• [italic yellow]{note}[/italic yellow]")
            else:
                console.print("[dim]No doctor notes yet[/dim]")
            
  
        
def add_patient(username):
    '''
    This function will allow the nurse to add new patients to the system
    '''
    patients = load_data(file_path)
    doctors = load_data(doctorsfile)
    exisitingRooms = [patient["room"] for patient in patients.values()]
    
    console.print("\n[bold blue] Add New Patient[/bold blue]")
    name = input("Name: ") 
    age = input("Age: ")
    blood = input("Blood Group (eg. A+, O-): ")
    
    #room input
    while True:
        room = input("Room Number: ")
        if room in exisitingRooms:
            console.print(f"[red]Room {room} is alread assigned to another patient, please enter another room number [/red]")
        else:
            break
        
    #doctor input
    while True:
        doctor = input("Responsible Doctor: ")
        if doctor in doctors:
            break
        else:
            console.print("[red]Doctor not found. Please enter a valid name.[/red]")
      
    
    id = str(max([int(i) for i in patients.keys()],default=0) + 1) # this will take max number of pid and store the next patient in max+1 to sequntial, if there is no patient sotred the default is zero so 0+1 >1 (first patient)
    
    patients[id] = {
        "name":name,
        "age":age,
        "blood":blood,
        "doctor":doctor,
        "room":room,
        "status":"stable",
        "notes":[],
        "alerted":False,
        "last_alertby":"",
        "nurse":username,
        "history":[{
            "status":"stable",
            "note":f"Initial status set by Nurse {username}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }]
       
          
    }
    
    save_data(file_path,patients) # will dump or write 'w' the python into my json file
    console.print(f"[green] Patient {name} (ID: {id}) added and assigned to Dr. {doctor}[/green]")
  
    
def update_status(username):
    '''
    This function will help the nurse to update patient status if needed , if status is crticial > an alert will be sent to the doctor
    '''
    patients = load_data(file_path)   
    console.print("\n[bold blue]Update Patient Status[/bold blue]")
    
    id = input("Please enter patient ID: ")  #validation  
    if id not in  patients:
        console.print("[red]Patient not found.[/red]")
        return
    #if patient found enter the status
    status = input("Enter patient new status : ( stable / critical / under observation ): ").strip().lower()
    if status not in ["stable" , "critical" , "under observation"]:
        console.print("[red]Invalid status.[/red]")
        return
    
    #if status is valid update it
    patients[id]["status"] = status
    
    patients[id]["history"].append({
            "status":status,
            "note":f"Updated to {status} by Nurse {username}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    if status in ["stable","under observation"]:
        patients[id]['alerted'] = False
        
    #if the status is critical, this will automatically send an alert
    if status == "critical" and not patients[id]['alerted']:
        msg = f"Yaqeth Alert \nPatient ID {id}\nName: {patients[id]["name"]}\nRoom No : {patients[id]['room']}\nStatus: {patients[id]["status"].upper()}! \nSent by nurse {username} - Please check immediately"
        send_alert(msg)
        patients[id]['alerted'] = True
        patients[id]['last_alertby'] = username
        #print("Telegram alert sent to The Doctor")
        
    save_data(file_path,patients)
    console.print(f"[yellow]Patient {id} status updated to: {status.upper()}[/yellow]")  


def triggeralert(username):
    ''' 
    This function will help the nurse to trigger an alert manually not automatically. For example if the patient status is under observation: alert can be still send to the doctor
    '''
    patients = load_data(file_path)
    
    console.print("\n[bold blue]Trigger Manual Alert[/bold blue]")
    
    id = input("Please enter patient id to trigger alert at any status: ").strip()
    
    if id not in patients:
        console.print("[red]Patient not found.[/red]")
        return
    
    msg = f"Manual Yaqeth Alert \nPatient ID {id}\nName: {patients[id]["name"]}\nRoom No : {patients[id]['room']}\nStatus: {patients[id]['status'].upper()} \nManual Alert triggered by nurse {username}"
    send_alert(msg)
    
    patients[id]["alerted"] = True
    patients[id]["last_alertby"] = username
    patients[id]["history"].append({
            "status":patients[id]["status"],
            "note":f"Manual alert triggered by Nurse {username}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    save_data(file_path,patients)
    console.print(f"[yellow]Manual alert sent for Patient {id} to doctor.[/yellow]")
    
    
        
    
    
         