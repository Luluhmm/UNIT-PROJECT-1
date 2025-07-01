# Yaqeth Alert System

## Overview

**Yaqeth** is a command-line based alert and monitoring system designed for hospitals and clinics. It helps **nurses** and **doctors** collaborate in real-time to monitor patient health, update their status, and trigger urgent alerts for critical cases.

This system ensures patients are always being tracked, especially when conditions become life-threatening. It helps nurses log and manage patient records and allows doctors to review patient history, respond to alerts, and add medical notes.

---

## Users & Their Roles

### As a Nurse, I can:
- Add a new patient with age, blood group, doctor, and room number.
- View all patients and their statuses.
- Update a patient's condition (stable, critical, or under observation).
- Manually trigger an alert to notify the doctor about any patient.

### As a Doctor, I can:
- View only the patients in **critical** condition.
- View full patient details and medical history.
- Add notes to a patient's file for nurses to follow.
- View a visual history chart (status over time ).

---

## How to Use Yaqeth

After running the program, you’ll be prompted to log in as a **Doctor** or **Nurse**.

### Nurse Commands:
- Add new patient > follow the prompts after selecting "Add Patient".
- Update status > enter patient ID and new condition.
- View patients > see all admitted patients in a table.
- Trigger alert > notify doctor manually for any status.

### Doctor Commands:
- View critical patients > displays patients marked as "critical".
- View patient details > enter patient ID to see full info.
- Add note > attach instructions or observations to the patient record.
- View patient history > see status updates over time.

---

## Technologies Used
- Python
- Rich (for CLI GUI design)
- Matplotlib (for optional charting)
- JSON files for data storage

--- 
## Why Lulwah Built This
Lulwah's passion for building medical tech tools has been there since her childhood, always fascinated by how technology can make healthcare smarter and more human. Yaqeth is a reflection of that passion. It’s a real-world tool designed to help healthcare professionals respond faster and smarter, while also being a chance to practice building a structured, modular Python CLI app that feels like a real product.

