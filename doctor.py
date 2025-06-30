from data.support import load_data, save_data

file_path = "/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/patients.json"
def view_critical():# only outputs the critical patients
    patients = load_data(file_path)
    print("Critical patients: ")
    found = False
    for i,value in patients.items():
        if value["status"] == "critical":
            print(f"[{i}] Patient name: {value['name']},Room No [{value['room']}]  - Responsible doctor is Dr. {value['doctor']}")
            found = True
        if not found:
            print("No critical cases yet. All patients are stabled")



def view_patient():
    patients = load_data(file_path)
    id = input("Please enter patient id: ")
    
    if id not in patients:
        print("Patient not found")
        return
    print("Patient Information: ")
    print(f"Name: {patients[id]['name']}")
    print(f"Age: {patients[id]['age']}")
    print(f"Blood Type: {patients[id]['blood']}")
    print(f"Doctor: {patients[id]['doctor']} - Nurse: {patients[id]['nurse']}")
    print(f"Status: {patients[id]['status']} Room No[{patients[id]['room']}]")
    print(f"Last alert by :  {patients[id]['last_alertby']}")
    
    print("Notes: ")
    if patients[id]['notes']:
        for note in patients[id]['notes']:
            print(f"-{note}")
            
    else:
        print("No notes yet")
    
    print("Patient History: ")
    for value in patients[id]['history']:
        print(f"{value['date'] }, Status : {value['status']}, Note: {value['note']}")
    

def add_note(drname):
    patients = load_data(file_path)
    
    id = input("Please enter patient ID: ")
    
    if id not in patients:
        print("Patient not found")
        return
    
    note = input("Write a note: ")
    fullnote = f"{note} (by Dr. {drname})"
    patients[id]['notes'].append(fullnote)
    save_data(file_path,patients)
    print(f"Dr {drname}'s Note Added")
    
    
    