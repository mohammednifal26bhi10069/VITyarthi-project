# Hospital Patient Management System

## 1. Project Overview

The **Hospital Patient Management System** is a menu-driven Python application for managing basic hospital information. It allows users to add and search patient records, maintain medical records, manage doctors, book and cancel appointments, record laboratory tests and medicines, generate patient bills, and discharge patients.

The project stores information in Python lists and dictionaries while the program is running.

## 2. Features

- **Patient Management**
  - Add new patient details.
  - Display all patient details.
  - Search for a patient by ID or name.
  - Track patient status as admitted or discharged.

- **Medical Records**
  - Add diagnosis, symptoms, prescription, test results, and treatment details.
  - Search and display a patient's medical record.

- **Doctor Management**
  - Add doctor information.
  - Store department and consultation fee.
  - Display available doctor details.

- **Appointment Management**
  - Book appointments for patients with available doctors.
  - View all appointments.
  - Cancel an appointment.

- **Laboratory Tests**
  - Add laboratory tests for patients.
  - Store test name, test fee, and test result.
  - View laboratory test details.

- **Medicine Management**
  - Add medicines for patients.
  - Store quantity and price.
  - Automatically calculate medicine charges.
  - View medicine details.

- **Billing**
  - Generate hospital bills using doctor fees, laboratory charges, pharmacy/medicine charges, administrative fees, and other charges.
  - Recalculate the patient's total bill when medicines or lab tests are added.

- **Patient Discharge**
  - Display the final bill information.
  - Change the patient's status to discharged.

## 3. Technologies / Tools Used

- **Python 3**
- Python built-in data structures:
  - Lists
  - Dictionaries
- Python standard `input()` and `print()` functions for the console interface.
- No external libraries or database systems are required.

## 4. Installation and Running the Project

### Prerequisites

Install **Python 3** on your computer.

You can verify the installation by opening a terminal or command prompt and running:

```bash
python --version
```

If your system uses `python3`, run:

```bash
python3 --version
```

### Installation

1. Download or copy the project file.
2. Save the Python program as:

```text
HPMS (1.1).py
```

3. Open a terminal/command prompt in the folder containing the Python file.
4. No additional packages need to be installed.

### Run the Project

On Windows:

```bash
python "HPMS (1.1).py"
```

On systems where Python 3 is invoked with `python3`:

```bash
python3 "HPMS (1.1).py"
```

After starting the program, the main menu is displayed.

## 5. Instructions for Testing

The application is a console-based program. Test the features through the numbered main menu.

### Basic Patient Test

1. Select **1. ADD PATIENT**.
2. Enter a unique patient ID and the requested patient information.
3. Select **2. DISPLAY PATIENT**.
4. Confirm that the entered patient details are displayed.

### Patient Search Test

1. Select **5. SEARCH PATIENT**.
2. Choose `id` or `name`.
3. Enter the corresponding patient information.
4. Confirm that the patient's details and medical record are displayed.

### Medical Record Test

1. Select **3. ADD MEDICAL RECORDS**.
2. Choose `id` or `name`.
3. Enter diagnosis, symptoms, prescription, test results, and treatment details.
4. Select **4. SEARCH MEDICAL RECORD**.
5. Confirm that the entered medical information is displayed.

### Doctor and Appointment Test

1. Select **7. ADD DOCTOR DETAILS** and add a doctor.
2. Select **8. DISPLAY DOCTOR DETAILS** to verify the doctor.
3. Add a patient if one has not already been created.
4. Select **9. BOOK AN APPOINTMENT**.
5. Enter the patient ID, doctor name, appointment date, and time.
6. Select **10. VIEW APPOINTMENTS** to verify the appointment.
7. Select **11. CANCEL APPOINTMENT** and enter the appointment ID.
8. View the appointments again to confirm that the status is cancelled.

### Laboratory Test

1. Select **12. ADD LAB TEST**.
2. Enter a valid patient ID.
3. Enter the test name, test fee, and test result.
4. Select **13. VIEW LAB TESTS**.
5. Confirm that the laboratory test information is displayed.

### Medicine and Billing Test

1. Select **14. ADD MEDICINE**.
2. Enter a patient ID, medicine name, quantity, and price.
3. Select **15. VIEW MEDICINES** to verify the medicine entry.
4. Select **6. GENERATE BILL**.
5. Enter the required doctor fee, administrative fee, and other charges.
6. Confirm that the bill includes laboratory and medicine/pharmacy charges where applicable.

### Discharge Test

1. Select **16. DISCHARGE PATIENT**.
2. Enter the patient ID.
3. Confirm the final bill information.
4. Verify that the patient's status changes to **discharged**.
5. Try booking an appointment or adding a medicine/lab test for the discharged patient and confirm that the program prevents the operation.

### Exit Test

Select **17. EXIT** and confirm that the program prints:

```text
Thank you
```

## 6. Main Menu

The program provides the following options:

| Option | Function |
|---|---|
| 1 | Add Patient |
| 2 | Display Patient |
| 3 | Add Medical Records |
| 4 | Search Medical Record |
| 5 | Search Patient |
| 6 | Generate Bill |
| 7 | Add Doctor Details |
| 8 | Display Doctor Details |
| 9 | Book an Appointment |
| 10 | View Appointments |
| 11 | Cancel Appointment |
| 12 | Add Lab Test |
| 13 | View Lab Tests |
| 14 | Add Medicine |
| 15 | View Medicines |
| 16 | Discharge Patient |
| 17 | Exit |

## 7. Screenshots

Screenshots are optional. For submission, screenshots of the following screens can be added here:

- Main menu
- Patient details
- Doctor details
- Appointment details
- Medical record
- Hospital bill
- Final patient discharge

Example:

```text
![Main Menu](screenshots/main-menu.png)
![Patient Details](screenshots/patient-details.png)
![Hospital Bill](screenshots/hospital-bill.png)
```

> Note: The screenshot paths above are examples. Add the actual screenshot files to the project before using these links.
