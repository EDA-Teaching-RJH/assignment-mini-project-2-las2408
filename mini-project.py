#Libraries
from superclass_crew import Pilot, Engineer
from id_checker import is_valid_id

#Regular Expressions
def main():
    print("--- Starship Crew Management System ---")
    
    #A list to hold the crew
    fleet = []

    while True:
        print("\n1. Add Pilot\n2. Add Engineer\n3. View Fleet\n4. Exit")
        choice = input("Select an option: ") #Creating the option menu

        if choice == "4":
            print("Shutting down system...")
            break
        
        if choice in ["1", "2"]:
            name = input("Enter Name: ")
            id_code = input("Enter Staff ID (e.g., SS-1234): ")

            #Using our custom library to check the ID
            if is_valid_id(id_code):
                if choice == "1":
                    hrs = input("Enter Flight Hours: ")
                    new_member = Pilot(name, id_code, hrs)
                else:
                    dept = input("Enter Department: ")
                    new_member = Engineer(name, id_code, dept)
                
                fleet.append(new_member)
                print("Crew member added successfully!")
            else:
                print("Error: Invalid ID format. Use XX-0000.")

        elif choice == "3":
            print("\n--- Current Fleet Manifest ---")
            for member in fleet:
                print(member) #This uses the __str__ I made

if __name__ == "__main__":
    main()
#Testing

#File I/O

#Object Orientated Programming

#Above and Beyond