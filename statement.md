# Hospital Patient Management System — Project Statement

## 1. Problem Statement

Managing hospital information manually can make it difficult to organize patient details, medical records, doctor information, appointments, laboratory tests, medicines, and billing information.

The **Hospital Patient Management System** is designed as a menu-driven Python program to provide a simple way to manage these hospital-related activities in one application. The system allows users to store and retrieve patient information, maintain medical records, manage doctors and appointments, record laboratory and medicine details, calculate bills, and discharge patients.

The program uses Python lists and dictionaries to store information while the application is running.

## 2. Scope of the Project

The scope of the project covers the basic management of hospital patient information and related activities.

The system includes:

- Adding and displaying patient information.
- Searching for patients using patient ID or name.
- Adding and searching medical records.
- Adding and displaying doctor details.
- Booking, viewing, and cancelling appointments.
- Adding and viewing laboratory tests and their results.
- Adding and viewing medicines and their charges.
- Calculating and generating hospital bills.
- Tracking doctor fees, laboratory bills, pharmacy/medicine charges, administrative fees, and other charges.
- Discharging patients and displaying final bill information.
- Maintaining patient status as admitted or discharged.

The project is a **console-based application** and stores data in memory using Python data structures. It does not include a database, graphical user interface, online access, or external services.

## 3. Target Users

The intended users of the system are people who need to manage basic hospital information through a simple console application, including:

- **Hospital administrative staff** — for managing patient details, doctors, appointments, and billing information.
- **Reception or front-desk staff** — for registering patients and managing appointments.
- **Hospital staff** — for viewing and maintaining patient-related medical, laboratory, and medicine information.
- **Students and learners** — for understanding how a Python-based hospital management system can be implemented using functions, lists, dictionaries, input/output, and basic validation.

## 4. High-Level Features

### Patient Management
- Add new patients with personal and medical information.
- Display all patient records.
- Search patients by ID or name.
- Track whether a patient is admitted or discharged.

### Medical Record Management
- Store diagnosis, symptoms, prescriptions, test results, and treatment details.
- Search and display medical records by patient ID or name.

### Doctor Management
- Add doctor information.
- Store department and consultation fee.
- Display available doctor details.

### Appointment Management
- Book appointments for existing patients with available doctors.
- Record appointment date and time.
- View all appointments.
- Cancel appointments.

### Laboratory Management
- Add laboratory tests for patients.
- Store test name, fee, and result.
- View laboratory test details.

### Medicine Management
- Add medicines for patients.
- Record medicine quantity and price.
- Automatically calculate medicine charges.
- View medicine details.

### Billing Management
- Generate hospital bills.
- Calculate laboratory and medicine/pharmacy charges.
- Include doctor fees, administrative fees, and other charges.
- Display the total hospital bill.

### Patient Discharge
- Display final bill information before discharge.
- Change the patient's status to discharged.
- Prevent certain operations, such as adding medicines or laboratory tests, for discharged patients.
