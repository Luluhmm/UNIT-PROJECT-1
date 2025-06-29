from data.support import load_data, save_data
from myalert import send_alert
file_path = "/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/patients.json"

def view_patients():
    patients = load_data(file_path)
    if not patients:
        print("No patients stored yet")
    else:
        print("Patient List:")
        for i, value in patients.items(): 
            print(f"[{i}] {value['name']} - Status: {value['status']}")
  
        
def add_patient():
    patients = load_data(file_path)
    
    name = input("Please enter patient name: ") 
    id = str(max([int(i) for i in patients.keys()],default=0) + 1) # this will take max number of pid and store the next patient in max+1 to sequntial, if there is no patient sotred the default is zero so 0+1 >1 (first patient)
    
    patients[id] = {
        "name":name,
        "status":"stable",
        "notes":[],
        "alerted":False
    }
    
    save_data(file_path,patients) # will dump or write 'w' the python into my json file
    print(f"Patient {name} added with ID {id}")
  
    
def update_status():
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
    
    #if status is valid
    patients[id]["status"] = status
    
    #if the status is critical, this will automatically send an alert
    if status == "critical" and not patients[id]['alerted']:
        msg = f"Yaqeth Alert \n Patient ID {id}\nName: {patients[id]["name"]}\n Status: Critical! \n Please check immediately"
        send_alert(msg)
        patients[id]['alerted'] = True
        print("Telegram alert sent to Dr")
        
    save_data(file_path,patients)
    print(f"Patient {id} status updated to {status}")  


def triggeralert():
    patients = load_data(file_path)
    
    id = input("Please enter patient id to trigger alert at any status: ")
    
    if id not in patients:
        print("Patient not found")
        return
    if patients[id]["alerted"]:
        print("Alert already sent for this patient")
        return
    
    msg = f"Yaqeth Alert \n Patient ID {id}\nName: {patients[id]["name"]}\n Status: {patients[id]['status']} \nManual Alert triggered"
    send_alert(msg)
    patients[id]["alerted"] = True
    save_data(file_path,patients)
    print("Manual alert was sent to doctor")
        
    
    
         