from database import patients, lab_tests, medicines # type: ignore


def add_patient():
    patient_id = input("Enter patient ID: ")
    for patient in patients:
        if patient["id"] == patient_id:
            print("Patient ID already exists")
            return
    name = input("Enter the name: ")
    gender = input("Enter the gender: ")
    phone = input("Enter the phone number: ")
    address = input("Enter the address: ")
    age = input("Enter the age: ")
    disease = input("Enter the disease: ")
    doctor = input("Enter the doctor name: ")
    patient = {
        "id": patient_id,
        "name": name,
        "gender": gender,
        "phone": phone,
        "address": address,
        "age": age,
        "disease": disease,
        "doctor": doctor,
        "diagnosis": "",
        "symptoms": "",
        "prescription": "",
        "test_results": "",
        "treatment_details": "",
        "doctor_fee": 0,
        "administrative_fee": 0,
        "other_charges": 0,
        "lab_bill": 0,
        "pharmacy_bill": 0,
        "medicine_charges": 0,
        "bill": 0,
        "status": "admitted"
    }
    patients.append(patient)
    print("Patient added successfully")


def display_medical_record(patient):
    print("Diagnosis:", patient["diagnosis"])
    print("Symptoms:", patient["symptoms"])
    print("Prescription:", patient["prescription"])
    print("Test results:", patient["test_results"])
    print("Treatment details:", patient["treatment_details"])


def display_patients():
    if len(patients) == 0:
        print("No patients found")
        return
    print("----- PATIENT DETAILS -----")
    for patient in patients:
        print("ID:", patient["id"])
        print("Name:", patient["name"])
        print("Gender:", patient["gender"])
        print("Phone:", patient["phone"])
        print("Address:", patient["address"])
        print("Age:", patient["age"])
        print("Disease:", patient["disease"])
        print("Doctor name:", patient["doctor"])
        print("Status:", patient["status"])
        display_medical_record(patient)
        print()


def add_medical_records():
    choice = input("Enter id or name: ")
    if choice == "id":
        search_value = input("Enter the ID: ")
        for patient in patients:
            if patient["id"] == search_value:
                patient["diagnosis"] = input("Enter diagnosis: ")
                patient["symptoms"] = input("Enter symptoms: ")
                patient["prescription"] = input("Enter prescription: ")
                patient["test_results"] = input("Enter test results: ")
                patient["treatment_details"] = input("Enter treatment details: ")
                print("Medical record added successfully")
                return
        print("Patient not found")
    elif choice == "name":
        search_value = input("Enter the name: ")
        for patient in patients:
            if patient["name"] == search_value:
                patient["diagnosis"] = input("Enter diagnosis: ")
                patient["symptoms"] = input("Enter symptoms: ")
                patient["prescription"] = input("Enter prescription: ")
                patient["test_results"] = input("Enter test results: ")
                patient["treatment_details"] = input("Enter treatment details: ")
                print("Medical record added successfully")
                return
        print("Patient not found")
    else:
        print("Invalid choice. Enter id or name")


def search_medical_record():
    choice = input("Enter id or name: ")
    if choice == "id":
        search_value = input("Enter patient ID: ")
        for patient in patients:
            if patient["id"] == search_value:
                print("ID:", patient["id"])
                print("Name:", patient["name"])
                display_medical_record(patient)
                return
    elif choice == "name":
        search_value = input("Enter patient name: ")
        for patient in patients:
            if patient["name"] == search_value:
                print("ID:", patient["id"])
                print("Name:", patient["name"])
                display_medical_record(patient)
                return
    else:
        print("Invalid choice")
        return
    print("Patient not found")


def show_patient(patient):
    print("----- PATIENT FOUND -----")
    print("ID:", patient["id"])
    print("Name:", patient["name"])
    print("Gender:", patient["gender"])
    print("Phone:", patient["phone"])
    print("Address:", patient["address"])
    print("Age:", patient["age"])
    print("Disease:", patient["disease"])
    print("Doctor name:", patient["doctor"])
    print("Status:", patient["status"])
    display_medical_record(patient)


def search_patient():
    choice = input("Enter id or name: ")
    if choice == "id":
        search_value = input("Enter the patient ID to search: ")
        for patient in patients:
            if patient["id"] == search_value:
                show_patient(patient)
                return
    elif choice == "name":
        search_value = input("Enter the patient name to search: ")
        for patient in patients:
            if patient["name"] == search_value:
                show_patient(patient)
                return
    else:
        print("Invalid choice")
        return
    print("Patient not found")


def recalculate_patient_bill(patient):
    lab_bill = 0
    for lab_test in lab_tests:
        if lab_test["patient_id"] == patient["id"]:
            lab_bill = lab_bill + lab_test["test_fee"]
    medicine_charges = 0
    for medicine in medicines:
        if medicine["patient_id"] == patient["id"]:
            medicine_charges = medicine_charges + medicine["total"]
    pharmacy_bill = medicine_charges
    doctor_fee = patient["doctor_fee"]
    administrative_fee = patient["administrative_fee"]
    other_charges = patient["other_charges"]
    total = doctor_fee + lab_bill + pharmacy_bill
    total = total + administrative_fee + other_charges
    patient["lab_bill"] = lab_bill
    patient["pharmacy_bill"] = pharmacy_bill
    patient["medicine_charges"] = medicine_charges
    patient["bill"] = total
    return total


def generate_bill():
    choice = input("Enter id or name: ")
    patient = None
    if choice == "id":
        search_value = input("Enter patient ID: ")
        for saved_patient in patients:
            if saved_patient["id"] == search_value:
                patient = saved_patient
                break
    elif choice == "name":
        search_value = input("Enter patient name: ")
        for saved_patient in patients:
            if saved_patient["name"] == search_value:
                patient = saved_patient
                break
    else:
        print("Invalid choice")
        return
    if patient is None:
        print("Patient not found")
        return
    print("----- BILL DETAILS -----")
    if patient["doctor_fee"] == 0:
        doctor_fee = input("Enter the doctor fee: ")
        try:
            patient["doctor_fee"] = float(doctor_fee)
        except ValueError:
            print("Please enter a valid doctor fee")
            return
    else:
        print("Permanent doctor fee:", patient["doctor_fee"])
    administrative_fee = input("Enter the administrative fee: ")
    other_charges = input("Enter the other charges: ")
    try:
        patient["administrative_fee"] = float(administrative_fee)
        patient["other_charges"] = float(other_charges)
    except ValueError:
        print("Please enter valid amounts")
        return
    recalculate_patient_bill(patient)
    print("----- HOSPITAL BILL -----")
    print("ID:", patient["id"])
    print("Name:", patient["name"])
    print("Gender:", patient["gender"])
    print("Phone:", patient["phone"])
    print("Address:", patient["address"])
    print("Age:", patient["age"])
    print("Disease:", patient["disease"])
    print("Doctor name:", patient["doctor"])
    print("Doctor fee:", patient["doctor_fee"])
    print("Lab bill:", patient["lab_bill"])
    print("Pharmacy bill:", patient["pharmacy_bill"])
    print("Medicine charges:", patient["medicine_charges"])
    print("Administrative fee:", patient["administrative_fee"])
    print("Other charges:", patient["other_charges"])
    print("Total bill:", patient["bill"])
    print("Bill generated successfully")


def discharge_patient():
    if len(patients) == 0:
        print("No patients found")
        return
    patient_id = input("Enter patient ID to discharge: ")
    patient = None
    for saved_patient in patients:
        if saved_patient["id"] == patient_id:
            patient = saved_patient
            break
    if patient is None:
        print("Patient not found")
        return
    if patient["status"] == "discharged":
        print("Patient is already discharged")
        return
    print("----- FINAL BILL -----")
    print("ID:", patient["id"])
    print("Name:", patient["name"])
    if patient["bill"] > 0:
        print("Doctor fee:", patient["doctor_fee"])
        print("Lab bill:", patient["lab_bill"])
        print("Pharmacy bill:", patient["pharmacy_bill"])
        print("Administrative fee:", patient["administrative_fee"])
        print("Other charges:", patient["other_charges"])
        print("Total bill:", patient["bill"])
    else:
        print("Bill has not been generated")
    patient["status"] = "discharged"
    print("Patient discharged successfully")
