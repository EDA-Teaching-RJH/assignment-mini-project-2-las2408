#ID-Checker
import re #Bringing in the regex library

def is_valid_id(staff_id):
    #Checking for: 2 uppercase letters, a dash, then 4 digits.
    pattern = r"^[A-Z]{2}-\d{4}$"
    
    #re.match checks if the ID fits the pattern perfectly
    if re.match(pattern, staff_id):
        return True
    else:
        return False #If it doesn't match, we reject it