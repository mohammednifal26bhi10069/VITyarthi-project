from database import doctors, patients, appointments # type: ignore


def add_doctor_details():
    doctor_name = input("Enter doctor name: ")
    for doctor in doctors:
        if doctor["name"] == doctor_name:
            print("Doctor already exists")
            return
    doctor_information = input("Enter doctor information: ")
    department = input("Enter department: ")
    consultation_fee = input("Enter consultation fee: ")
    try:
        consultation_fee = float(consultation_fee)
    except ValueError:
        print("Please enter a valid fee")
        return
    doctor = {
        "name": doctor_name,
        "information": doctor_information,
        "department": department,
        "consultation_fee": consultation_fee
    }
    doctors.append(doctor)
    print("Doctor details added successfully")


def display_doctors():
    if len(doctors) == 0:
        print("No doctors found")
        return
    print("----- DOCTOR DETAILS -----")
    for doctor in doctors:
        print("Doctor name:", doctor["name"])
        print("Doctor information:", doctor["information"])
        print("Department:", doctor["department"])
        print("Consultation fee:", doctor["consultation_fee"])
        print()


def book_appointment():
    if len(patients) == 0:
        print("No patients found")
        return
    if len(doctors) == 0:
        print("No doctors found")
        return
    patient_id = input("Enter patient ID: ")
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
    print("----- AVAILABLE DOCTORS -----")
    for doctor in doctors:
        print(doctor["name"])
    doctor_name = input("Enter doctor name: ")
    doctor = None
    for saved_doctor in doctors:
        if saved_doctor["name"] == doctor_name:
            doctor = saved_doctor
            break
    if doctor is None:
        print("Doctor not found")
        return
    appointment = {
        "id": str(len(appointments) + 1),
        "patient_id": patient["id"],
        "patient_name": patient["name"],
        "doctor_name": doctor["name"],
        "date": input("Enter appointment date: "),
        "time": input("Enter appointment time: "),
        "status": "booked"
    }
    appointments.append(appointment)
    print("Appointment booked successfully")
    print("Appointment ID:", appointment["id"])


def view_appointments():
    if len(appointments) == 0:
        print("No appointments found")
        return
    print("----- APPOINTMENTS -----")
    for appointment in appointments:
        print("Appointment ID:", appointment["id"])
        print("Patient ID:", appointment["patient_id"])
        print("Patient name:", appointment["patient_name"])
        print("Doctor name:", appointment["doctor_name"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("Status:", appointment["status"])
        print()


def cancel_appointment():
    if len(appointments) == 0:
        print("No appointments found")
        return
    appointment_id = input("Enter appointment ID to cancel: ")
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            if appointment["status"] == "cancelled":
                print("Appointment is already cancelled")
            else:
                appointment["status"] = "cancelled"
                print("Appointment cancelled successfully")
            return
    print("Appointment not found")
