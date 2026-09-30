from database import patients, medicines, lab_tests # type: ignore
from patient_module import recalculate_patient_bill # type: ignore


def add_medicine():
    if len(patients) == 0:
        print("No patients found")
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
    medicine_name = input("Enter medicine name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        print("Please enter valid quantity and price")
        return
    total = quantity * price
    medicine = {
        "patient_id": patient["id"],
        "patient_name": patient["name"],
        "medicine_name": medicine_name,
        "quantity": quantity,
        "price": price,
        "total": total
    }
    medicines.append(medicine)
    recalculate_patient_bill(patient)
    print("Medicine added successfully")
    print("Medicine charge:", total)


def view_medicines():
    if len(medicines) == 0:
        print("No medicines found")
        return
    print("----- MEDICINES -----")
    for medicine in medicines:
        print("Patient ID:", medicine["patient_id"])
        print("Patient name:", medicine["patient_name"])
        print("Medicine name:", medicine["medicine_name"])
        print("Quantity:", medicine["quantity"])
        print("Price:", medicine["price"])
        print("Total charge:", medicine["total"])
        print()


def add_lab_test():
    if len(patients) == 0:
        print("No patients found")
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
    test_name = input("Enter test name: ")
    test_fee = input("Enter test fee: ")
    test_result = input("Enter test result: ")
    try:
        test_fee = float(test_fee)
    except ValueError:
        print("Please enter a valid test fee")
        return
    lab_test = {
        "patient_id": patient["id"],
        "patient_name": patient["name"],
        "test_name": test_name,
        "test_fee": test_fee,
        "test_result": test_result
    }
    lab_tests.append(lab_test)
    recalculate_patient_bill(patient)
    print("Lab test added successfully")


def view_lab_tests():
    if len(lab_tests) == 0:
        print("No lab tests found")
        return
    print("----- LABORATORY TESTS -----")
    for lab_test in lab_tests:
        print("Patient ID:", lab_test["patient_id"])
        print("Patient name:", lab_test["patient_name"])
        print("Test name:", lab_test["test_name"])
        print("Test fee:", lab_test["test_fee"])
        print("Test result:", lab_test["test_result"])
        print()
