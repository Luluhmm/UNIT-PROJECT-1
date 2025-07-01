from data.support import load_data, save_data
import matplotlib.pyplot as plt
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()


file_path = "/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/data/patients.json"
def view_critical():# only outputs the critical patients
    '''
    This function will filter and print the critical patients only
    '''
    patients = load_data(file_path)
    
    table = Table(title="Critical Patients", box=box.SIMPLE_HEAVY)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Name", style="bold")
    table.add_column("Room", style="bold")
    table.add_column("Doctor", style="bold")
    
    
    #print("Critical patients: ")
    found = False
    for i,value in patients.items():
        if value["status"] == "critical":
            table.add_row(i, value["name"], value["room"], value["doctor"])
            found = True
            
    if found:
        console.print(table)
    else:
        console.print("[green] No critical cases. All patients are stable.[/green]")


def view_patient():
    '''
    This function will output the whole history and information for the specified patient (based on patient id)
    '''
    patients = load_data(file_path)
    id = input("Please enter patient id:")
    
    if id not in patients:
        console.print("[red] Patient not found.[/red]")
        return
    
    console.print(f"\n[bold blue]Patient Information (ID {id})[/bold blue]")
    info_table = Table(box=box.SIMPLE)
    info_table.add_column("Attribute", style="cyan", no_wrap=True)
    info_table.add_column("Details", style="bold")
    
    info_table.add_row("Name", patients[id]['name'])
    info_table.add_row("Age", patients[id]['age'])
    info_table.add_row("Blood", patients[id]['blood'])
    info_table.add_row("Doctor", patients[id]['doctor'] )
    info_table.add_row("Nurse", patients[id]['nurse'])
    info_table.add_row("Status", patients[id]['status'])
    info_table.add_row("Room", patients[id]['room'])
    info_table.add_row("Last alert by", patients[id]['last_alertby'] or "N/A")
    console.print(info_table)
    
    console.print("\n[bold yellow]Doctor Notes:[/bold yellow]")
    if patients[id]['notes']:
        for note in patients[id]['notes']:
            console.print(f"• {note}")
            
    else:
        console.print("[dim]No notes available yet.[/dim]")
    
    history_table = Table(title="Status History", box=box.SIMPLE)
    history_table.add_column("Date", style="dim")
    history_table.add_column("Status", style="bold")
    history_table.add_column("Note", style="bold")
    
    for value in patients[id]['history']:
        history_table.add_row(value['date'], value['status'], value['note'])
    console.print(history_table)

def add_note(drname):
    '''
    This function will allow the Dr to add a note to any patient, the function takes the dr name as an argument
    '''
    patients = load_data(file_path)
    
    id = input("Please enter patient ID: ")
    
    if id not in patients:
        console.print("[red] Patient not found.[/red]")
        return
    
    note = input("Write a note: ")
    fullnote = f"{note} (by Dr. {drname})"
    patients[id]['notes'].append(fullnote)
    save_data(file_path,patients)
    print(f"Dr {drname}'s Note Added")
    
    
    
def plotHistory():
    '''
    This function will show the history in a chart to help the doctors observe patient progress.
    Matplot library is used to visualize the data stored in my jason, y axis are my diffrent status levels(stable,critical..)
    and x axix are the dates in my history to see full progress through patients journey
    
    '''
    patients = load_data(file_path)
    id = input("Enter patient id to view History Plot Progress: ")

    if id not in patients:
        print("Patient not found.")
        return

    history = patients[id]["history"]
    if not history or len(history) < 2:
        print("Not enough history to plot patient progress.")
        return

    dates = []
    statusvalues = []
    statusmap = {"stable": 1, "under observation": 2, "critical": 3}

    for value in history:
        dates.append(datetime.strptime(value["date"], "%Y-%m-%d %H:%M:%S"))
        statusvalues.append(statusmap.get(value["status"],0)) # return zero if there is no status found

    plt.figure(figsize=(8, 4))
    plt.plot(dates, statusvalues, marker='*')
    plt.yticks([1, 2, 3], ["Stable", "Under Obs.", "Critical"])
    plt.xlabel("Date")
    plt.ylabel("Status Level")
    plt.title(f"History Plot for the patient {patients[id]['name']}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    