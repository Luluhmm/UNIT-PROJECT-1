from data.support import load_data, save_data
from myalert import send_alert
from datetime import datetime

file_path = "/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/patients.json"
doctorsfile = "/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/doctors.json"

def view_patients():
    patients = load_data(file_path)
    if not patients:
        print("No patients stored yet")
    else:
        print("Patient List:")
        for i, value in patients.items(): 
            print(f"[{i}] {value['name']} - Status: {value['status']} - Responsible Doctor: {value['doctor']}")
            
            print("Doctor Notes: ")
            if value['notes']:
                for note in value['notes']:
                    print(f"- {note}")
            else:
                print("No doctor notes yet")
            
  
        
def add_patient(username):
    patients = load_data(file_path)
    doctors = load_data(doctorsfile)
    exisitingRooms = [patient["room"] for patient in patients.values()]
    
    name = input("Please enter patient name: ") 
    age = input("Please enter patient age: ")
    blood = input("Please enter patient blood group(eg. A+, O-): ")
    
    #room input
    while True:
        room = input("Enter room number: ")
        if room in exisitingRooms:
            print(f"Room {room} is alread assigned to another patient, please enter another room number ")
        else:
            break
        
    #doctor input
    while True:
        doctor = input("Please enter responsible doctor name : ")
        if doctor in doctors:
            break
        else:
            print("Doctor not found or unavailable. Please assign a valid doctor")
      
    
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
    print(f"Patient {name} added with ID {id} and assigned to Dr. {doctor}")
  
    
def update_status(username):
    patients = load_data(file_path)   
    
    id = input("Please enter patient ID: ")  #validation  
    if id not in  patients:
        print("Patient not Found")
        return
    #if patient found enter the status
    status = input("Enter patient status : ( stable / critical / under observation ): ").strip().lower()
    if status not in ["stable" , "critical" , "under observation"]:
        print("Invalid status")
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
    print(f"Patient {id} status updated to {status}")  


def triggeralert(username):
    patients = load_data(file_path)
    
    id = input("Please enter patient id to trigger alert at any status: ")
    
    if id not in patients:
        print("Patient not found")
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
    print("Manual alert was sent to doctor")
    
    
        
    
    
         