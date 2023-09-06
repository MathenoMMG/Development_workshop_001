import currentstatus
import clinicalhistory

from datetime import date
x = date.today()
today =  [str(x.day),str(x.month),str(x.year)]

#patient list
patient_list = []



class Patient(currentstatus.Status, clinicalhistory.ClinicalHistory):
    def __init__(self, document, name, sex, birthdate, blood_type, chronicd , Status , Clinicalhistory):
        self.document = document
        self.name = name
        self.sex = sex
        self.birthdate = birthdate
        self.blood_type = blood_type
        self.chronicd = chronicd
        self.Status = Status
        self.Clinicalhistory = Clinicalhistory


    @staticmethod   
    def showPatient():
        search_bydoc = int(input("Enter the document: "))
        found_patient = None
        
        for Patient in patient_list:
            if Patient.document == search_bydoc:
                found_patient = Patient

                print("Patient found \n")
                
                Patient.patientmenu(found_patient)                
        
        if found_patient is None:
            print("Patient not found")


    @staticmethod   
    def AddPatient():
        print("--- PATIENT DATA ---")
        document = int(input("Enter the document: "))

        for Newpatient in patient_list:
            while Newpatient.document == document:
                print("Patient already exists")
                document = int(input("Enter the document: "))

        name = input("Enter the name: ")
        sex = int(input("1.Male  -  2. Female: "))
        while (sex <1 or sex>2):
            print("Invalid choice")
            sex = int(input("1.Male  -  2. Female: "))
        birthdate = input("Enter the birthdate: (DD MM AA) ")
        birthdate = birthdate.split(" ")
        blood_type = input("Enter the blood type: ")
        
        chronicd = int(input("The patient suffers from chronic diseases: (Y = 1 / N = 2) "))
        if chronicd !=1:
            chronicd = None


        while not (blood_type == "A+") or (blood_type == "A-") or (blood_type == "B+") or (blood_type == "B-") or (blood_type == "AB+") or (blood_type == "AB-") or (blood_type == "O+") or (blood_type == "O-"):
            print("Invalid blood type")
            blood_type = input("Enter the blood type: ")
        
        status = currentstatus.Status.newstatus()
        clinicalhistory = clinicalhistory.ClinicalHistory.newclinicalhistory()
        

        Newpatient = Patient(document, name, sex, birthdate, blood_type, chronicd, status, clinicalhistory )
        print("Patient added succesfully")
        patient_list.append(Newpatient)


        patient_list.sort(key=lambda x: x.Patient.Clinicalhistory.arrival  , reverse=False)
    
     
    
    @staticmethod
    def patientmenu(found_patient):
        print("\n--- PATIENT MENU ---\n")
        print("Current date: ", today)
        

        if (found_patient.Clinicalhistory.departure == None):
            print("Document: ", found_patient.document, " - Name: ", found_patient.name, " - In the hospital: ", "Yes")
            
            print("\nIf the patient is still in the hospital, you can´t make a new clinical history, you need to close the last one first\n")
            print("1. Show patient")
            print("2. Exit")
            
            choice = int(input("Enter your choice: "))
            while (choice < 1 or choice > 2):
                print("Invalid choice")
                choice = int(input("Enter your choice: "))
            
            if choice == 1:
                Patient.showdata(found_patient)
            else:
                print("Exiting\n")
            
            
            print("\nThe patient is still in the hospital, close the current clinical history at date ", today , " ?")
            choose =int(input( "(Y = 1 / N = 2) "))
            
            if choose == 1:
                found_patient.Clinicalhistory.departure = today
                print("Clinical history closed")
            
            else:
                print("Clinical history still open")


        else :
            print("Document: ", found_patient.document, " - Name: ", found_patient.name, " - In the hospital: ", "No")

            print("1. Show patient")
            print("2. Edit patient")
            print("3. Exit")
            
            choice = int(input("Enter your choice: "))
            while (choice < 1 or choice > 3):
                print("Invalid choice")
                choice = int(input("Enter your choice: "))
            
            if choice == 1:
                Patient.showdata(found_patient)
            elif choice == 2:
                Patient.editpatient(found_patient)
            else:
                print("Exiting\n")
        
    @staticmethod
    def showdata(found_patient):
        print("\nDocument: ", found_patient.document)
        print("Name: ", found_patient.name)
        if found_patient.sex == 1:
            print ("Sex: Male")
        if found_patient.sex == 2:
            print("Sex: Female")
        print("Birthdate: ", found_patient.birthdate)
        print("Blood type: ", found_patient.blood_type)

        if found_patient.chronicd != None:
            print("Chronic diseases: Yes")
        else:
            print("Chronic diseases: ", found_patient.chronicd)

        print("Temperature: ", found_patient.Status.temperature)
        print("O2sat: ", found_patient.Status.o2sat)
        print("Respiratory rate: ", found_patient.Status.respiratory_rate)
        print("Score: ", found_patient.Status.score)

        
        print("\n---Clinical History - Last entry---\n")
        print("Arrival date: ", found_patient.Clinicalhistory.arrived)
        print("Reason of the visit: ", found_patient.Clinicalhistory.reason )
        print("Diagnosis: ", found_patient.Clinicalhistory.diagnosis)
        print("Treatment: ", found_patient.Clinicalhistory.treatment)
        print("Medicament: ", found_patient.Clinicalhistory.medicament)
        print("Doctor: ", found_patient.Clinicalhistory.doctor)
        print("Departure date: ", found_patient.Clinicalhistory.departure)        

        print("\n---Annexes---\n")
        print("Evolution notes: ", found_patient.Clinicalhistory.Annexes.evonotes)
        print("Diagnostic image: ", found_patient.Clinicalhistory.Annexes.diagnosticimg)
        print("Exam results: ", found_patient.Clinicalhistory.Annexes.examresults)
        
    @staticmethod
    def editpatient(found_patient):
        print("\n--- EDIT PATIENT ---\n")
        print("You can only edit opening a new clinical history")
        print("Opening new clinical history with today's date ", today)
        
        found_patient.Status = currentstatus.Status.newstatus()
        found_patient.Clinicalhistory = clinicalhistory.ClinicalHistory.newclinicalhistory(today)
        
        print("\n---Clinical history edited succesfully---\n")

    

    @staticmethod
    def send_patient_list():
        return patient_list


patient_list.append(Patient(321, "Juan", 1, ['12','12','2003'], "A+", 1, currentstatus.Status(234, 32.3, 95, 23, 4), clinicalhistory.ClinicalHistory(['10', '8' ,'2023'], "Fever", "Flu", "Paracetamol", "Paracetamol" , clinicalhistory.Annexes("Se tomo el paracetamol pero no mejora, la vaina ta pelua", None, "Está bien maluco") ,"Dr. Joao", None )) )         
patient_list.append(Patient(123, "Mathew", 1, ['17','12','2003'], "A+", None, currentstatus.Status(150, 35.5, 99, 14, 2), clinicalhistory.ClinicalHistory(['5','9','2023'], "Se sentia maluco", "Esta maluco", "Acetaminofen y pa la casa", "Acetaminofen", clinicalhistory.Annexes("Se tomo la vaina y ya esta bacano", None, None) ,  "Dr. Joselui", ['5','9','2023'])) )          



        
