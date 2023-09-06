
medsinstock = ["Acetaminofen","Vicbaporub", "Mata raton", "Paracetamol"]

class Annexes():
    def __init__(self, evonotes, diagnosticimg, examresults):
        self.diagnosticimg = diagnosticimg
        self.evonotes = evonotes
        self.examresults = examresults
    
    @staticmethod
    def sendannexes():
        print("\n--- ANNEXES ---\n")
        evonotes = input("Enter the evolution notes: ")
        x = int(input("There are diagnostic images in the clinical history? (Y = 1 / N = 2) "))
        if x == 1:
            diagnosticimg = input("Enter the diagnostic image: ")
        else:
            diagnosticimg = None

        x = int(input("There are examens results in the clinical history? (Y = 1 / N = 2) "))        
        if x == 1:
            examresults = input("Enter the exam results: ")
        else:
            examresults = None

        annexes = Annexes(evonotes, diagnosticimg, examresults)
        return annexes



class ClinicalHistory ():
    def __init__(self, arrived, reason, diagnosis, treatment, medicament, Annexes , doctor, departure):
        
        self.arrived = arrived
        self.reason = reason
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.medicament = medicament
        self.Annexes = Annexes
        self.doctor = doctor
        self.departure = departure

    @staticmethod
    def newclinicalhistory():
        print("\n--- CLINICAL HISTORY ---\n")
        
        arrived = input("Enter the arrival date: (DD MM AA) ")
        arrived = arrived.split(" ")
        reason = input("Enter the reason of the visit: ")    
        diagnosis = input("Enter the diagnosis: ")
        treatment = input("Enter the treatment: ")


        print("\n--- MEDICATION IN STOCK ---\n")
        c = 1
        for i in medsinstock:
            print(c,". ",medsinstock[c-1])
            c += 1
        
        x = int(input("Medication suplied : "))
        while (x < 0 or x > c):
            print("Invalid choice")
            x = int(input("Medication suplied : "))   
        medicament = medsinstock[x-1]


        annexes = Annexes.sendannexes()
        

        x = int(input("Being atended by a doctor in the moment (Y = 1 / N = 2) "))
        
        if x == 1:
            doctor = input("Enter the doctor name: ")
        else:
            doctor = None

        out= int(input("The patient is already out of the hospital? (Y = 1 / N = 2)"))
        if out == 1:
            departure = input("Enter the departure date: (DD MM AA) ")
            departure = departure.split(" ")
        else:
            departure = None
        
        recentclinicalhistory = ClinicalHistory(arrived, reason, diagnosis, treatment, medicament, annexes, doctor, departure) 
        return recentclinicalhistory
    
    @staticmethod
    def newclinicalhistory(arrived):
        print("\n--- NEW CLINICAL HISTORY ---\n")
        
        reason = input("Enter the reason of the visit: ")    
        diagnosis = input("Enter the diagnosis: ")
        treatment = input("Enter the treatment: ")


        print("\n--- MEDICATION IN STOCK ---\n")
        c = 1
        for i in medsinstock:
            print(c,". ",medsinstock[c-1])
            c += 1
        
        x = int(input("Medication suplied : "))
        while (x < 0 or x > c):
            print("Invalid choice")
            x = int(input("Medication suplied : "))   
        medicament = medsinstock[x-1]


        annexes = Annexes.sendannexes()
        

        x = int(input("Being atended by a doctor in the moment (Y = 1 / N = 2) "))
        
        if x == 1:
            doctor = input("Enter the doctor name: ")
        else:
            doctor = None

        out= int(input("The patient is already out of the hospital? (Y = 1 / N = 2) "))
        if out == 1:
            departure = input("Enter the departure date: (DD MM AA) ")
            departure = departure.split(" ")
        else:
            departure = None
        
        recentclinicalhistory = ClinicalHistory(arrived, reason, diagnosis, treatment, medicament, annexes, doctor, departure) 
        return recentclinicalhistory



    @staticmethod
    def send_medsinstock():
        return medsinstock

        