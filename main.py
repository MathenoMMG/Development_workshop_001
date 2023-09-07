from patient import Patient
from hospital import Hospital 

from datetime import date
x = date.today()
today = [str(x.day), str(x.month), str(x.year)]


class main():
    # This is the main class with a menu for the clinical software

    def menu(self):
        # This is the menu

        while True:
            print("\n--- CLINICAL SOFTWARE MENU ---\n")
            print("Current date: ", today)
            print("1. Check patient ")
            print("2. Add patient")
            print("3. Hospital menu")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                Patient.showPatient()
            elif choice == 2:
                Patient.AddPatient()
            elif choice == 3:
                Hospital.hospitalMenu()
            elif choice == 4:
                print("Finishing program")
                break
            else:
                print("Invalid choice")
                self.menu()


main().menu()
