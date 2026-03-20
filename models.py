from datetime import datetime

class Patient:
    def __init__(self, name):
        # State (Attributes) - Satisfies OOP Requirement
        self.name = name
        # Standard API - Satisfies datetime Requirement
        self.timestamp = datetime.now().strftime("%H:%M:%S")

    def get_details(self):
        # Behavior (Method) - Satisfies OOP Requirement
        return f"{self.name} (Registered at: {self.timestamp})"