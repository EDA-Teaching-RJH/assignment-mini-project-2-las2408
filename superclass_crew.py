#Superclass
class CrewMember:
    def __init__(self, name, staff_id):
        #Ensuring name entered isn't empty

        if not name:
            raise ValueError("Name cannot be empty")
        
        self.name = name
        self.staff_id = staff_id

    def __str__(self):
        return f"Name: {self.name} | ID: {self.staff_id}"

#Sub-Class
class Pilot(CrewMember):
    def __init__(self, name, staff_id, flight_hours):
        super().__init__(name, staff_id)
        self.flight_hours = flight_hours

    def __str__(self):
        return super().__str__() + f" | Role: Pilot ({self.flight_hours} hours)"

class Engineer(CrewMember):
    def __init__(self, name, staff_id, department):
        super().__init__(name, staff_id)
        self.department = department

    def __str__(self):
        return super().__str__() + f" | Role: Engineer ({self.department})"

#Protecting Data        
@property
def flight_hours(self):
    return self._flight_hours

@flight_hours.setter
def flight_hours(self, value):
    if int(value) < 0:
            raise ValueError("Flight hours cannot be negative!")
        self._flight_hours = value