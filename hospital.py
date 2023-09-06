import patient
import clinicalhistory

from datetime import date
x = date.today()
today =  [str(x.day),str(x.month),str(x.year)]



class Hospital(patient.Patient):
    def __init__(self, name, doctors, beds, chairs, medsinstock, patient_list):
        self.name = name
        self.doctors = doctors
        self.beds = beds
        self.chairs = chairs
        self.medsinstock = medsinstock
        self.patient_list = patient_list
    
    
    @staticmethod
    def hospitalstatus():

        patient_list= patient.Patient.send_patient_list()
        medsinstock = clinicalhistory.ClinicalHistory.send_medsinstock()

        NewHospital = Hospital("Hospital001", 500, 300, 700, medsinstock ,patient_list)

        print("\n--- HOSPITAL STATUS ---\n")
        print("Hospital name: ", NewHospital.name)

        bedsocupied = 0
        chairsocupied = 0
        doctorsocupied = 0

        
        patienttodayin = 0
        patienttodayout = 0

        patientsmonthin = 0
        patientsmonthout = 0


        for patient.Patient in patient_list:
            if ((patient.Patient.Clinicalhistory.departure == None)):

                if (patient.Patient.Status.score > 2):
                    bedsocupied += 1
                else:
                    chairsocupied += 1
            
                if (str(patient.Patient.Clinicalhistory.doctor) != None):
                    doctorsocupied += 1

                if (patient.Patient.Clinicalhistory.arrived == today):
                    patienttodayin += 1
                if (patient.Patient.Clinicalhistory.arrived[1] == today[1]):
                    patientsmonthin += 1
            else:
                if patient.Patient.Clinicalhistory.departure[1] == today[1]:
                    patientsmonthout += 1
                if patient.Patient.Clinicalhistory.departure == today:
                    patienttodayout += 1
                       

        fdoctors = (NewHospital.doctors - doctorsocupied)
        fbeds = (NewHospital.beds - bedsocupied)
        fchairs = (NewHospital.chairs - chairsocupied)



        print("Current number of doctors free: ", fdoctors)
        print("Number of patients in the hospital at the moment: ", (bedsocupied+chairsocupied))
        print("Number of beds free at the moment: ", fbeds)
        print("Number of chairs free at the moment: ", fchairs)
        print("Number of patients today in ", patienttodayin, "  - out ", patienttodayout)
        print("Number of patients in the current month in ", patientsmonthin , "  - out ", patientsmonthout)
        print("Number of patients that left the hospital in the current month: ")
        print("Hospital occupancy rate: ", ((bedsocupied+chairsocupied)/(NewHospital.beds+NewHospital.chairs))*100, "%")
        print("Medical supplies in stock: ", medsinstock)
    
  
    @staticmethod
    def hospitalpatients():
        patient_list= patient.Patient.send_patient_list()
        medsinstock = clinicalhistory.ClinicalHistory.send_medsinstock()

        NewHospital = Hospital("Hospital001", 500, 300, 700, medsinstock, patient_list)


        print("\n--- LIST OF HOSPITAL PATIENTS ---\n")
        
        x = 1
        print("Patients in total: ", len(patient_list))

        for Patient in patient_list:
            
            gone = "No"
            if ((Patient.Clinicalhistory.departure == None)):
                gone = "Yes"

            print(x, ". Document:", Patient.document," - Name: ", Patient.name, " - Sex: ",Patient.sex ," - BT: ", Patient.blood_type, " - Last Score: ", Patient.Status.score," - Last prescription: ", Patient.Clinicalhistory.medicament , " - Last Doctor: ", Patient.Clinicalhistory.doctor, " - In Hospital: ", gone)    
            x += 1
     
    @staticmethod
    def hospitalMenu():
        
        choice_1 = 0
        while choice_1 != 3:
            print("\n--- MENU ---\n")
            print("Current date: ", today)
            print("1. Hospital Status")
            print("2. Hospital Patients I/O list")
            print("3. Exit")
            choice_1 = int(input("Enter your choice: "))
            if choice_1 == 1:
                Hospital.hospitalstatus()
            elif choice_1 == 2:
                Hospital.hospitalpatients()
            elif choice_1 == 3:
                print("Exiting\n")
            else:
                print("Invalid choice")

