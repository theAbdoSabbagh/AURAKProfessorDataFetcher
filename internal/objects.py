class Professor:
    def __init__(
        self,
        name: str,
        role: str,
        room: str,
        phone_number: str,
        department: str
    ):
        self.name = name
        self.role = role
        self.room = room
        self.phone_number = phone_number
        self.department = department
    
    def __str__(self):
        text = f"Name: {self.name}\nDepartment: {self.department}\nRole: {self.role}"
        if self.room: # Sometimes room number is not available
            text += f"\nRoom number: {self.room}"

        if self.phone_number: # Sometimes phone number is not available
            text += f"\nPhone number: {self.phone_number}"
        
        return text
