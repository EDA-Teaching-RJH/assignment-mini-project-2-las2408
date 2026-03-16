#Superclass
class CrewMember:
    def __init__(self, name, staff_id):
        #Ensuring name entered isn't empty so the system has a record
        if not name:
            raise ValueError("Name cannot be empty")
        
        self.name = name
        self.staff_id = staff_id

    def __str__(self):
        #Returns names and ID's in a clean format
        return f"Name: {self.name} | ID: {self.staff_id}"

#Sub-Class for Pilots
class Pilot(CrewMember): #Using inheritance stops duplicate code
    def __init__(self, name, staff_id, flight_hours):
        #Sends the common info back to the CrewMember class
        super().__init__(name, staff_id)
        self.flight_hours = flight_hours

    #Protecting Data - Stops people from putting in impossible numbers breaking the code
    @property
    def flight_hours(self):
        return self._flight_hours 

    @flight_hours.setter
    def flight_hours(self, value):
        #This ensures people can't break the system via negative flight hours
        if int(value) < 0:
            raise ValueError("Flight hours cannot be negative!")
        self._flight_hours = value

    def __str__(self):
        #Assigns the staff member role and flight hours to the printout
        return super().__str__() + f" | Role: Pilot ({self.flight_hours} hours)"

#Sub-Class for Engineers
class Engineer(CrewMember): #Inherits from the main CrewMember class
    def __init__(self, name, staff_id, department):
        super().__init__(name, staff_id)
        self.department = department

    def __str__(self):
        #Shows the specific department for the Engineer
        return super().__str__() + f" | Role: Engineer ({self.department})"