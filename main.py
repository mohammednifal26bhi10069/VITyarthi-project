from patient_module import add_patient, display_patients, add_medical_records, search_medical_record, search_patient, generate_bill, discharge_patient # type: ignore
from doctor_module import add_doctor_details, display_doctors, book_appointment, view_appointments, cancel_appointment # type: ignore
from lab_pharmacy_module import add_lab_test, view_lab_tests, add_medicine, view_medicines # type: ignore


if __name__ == "__main__":
    while True:
        print("... HOSPITAL PATIENT MANAGEMENT SYSTEM... ")
        print("1. ADD PATIENT")
        print("2. DISPLAY PATIENT")
        print("3. ADD MEDICAL RECORDS")
        print("4. SEARCH MEDICAL RECORD")
        print("5. SEARCH PATIENT")
        print("6. GENERATE BILL")
        print("7. ADD DOCTOR DETAILS")
        print("8. DISPLAY DOCTOR DETAILS")
        print("9. BOOK AN APPOINTMENT")
        print("10. VIEW APPOINTMENTS")
        print("11. CANCEL APPOINTMENT")
        print("12. ADD LAB TEST")
        print("13. VIEW LAB TESTS")
        print("14. ADD MEDICINE")
        print("15. VIEW MEDICINES")
        print("16. DISCHARGE PATIENT")
        print("17. EXIT")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            display_patients()
        elif choice == "3":
            add_medical_records()
        elif choice == "4":
            search_medical_record()
        elif choice == "5":
            search_patient()
        elif choice == "6":
            generate_bill()
        elif choice == "7":
            add_doctor_details()
        elif choice == "8":
            display_doctors()
        elif choice == "9":
            book_appointment()
        elif choice == "10":
            view_appointments()
        elif choice == "11":
            cancel_appointment()
        elif choice == "12":
            add_lab_test()
        elif choice == "13":
            view_lab_tests()
        elif choice == "14":
            add_medicine()
        elif choice == "15":
            view_medicines()
        elif choice == "16":
            discharge_patient()
        elif choice == "17":
            print("Thank you")
            break
        else:
            print("Invalid choice. Please enter 1 to 17.")
