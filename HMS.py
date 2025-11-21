class Patient:
    def __init__(self, name, condition):
        self._name = name   #private
        self.__condition = condition #protected

    #use of the getter method
    def get_condition(self):
        return self.__condition
    
    #setter for private 
    def set_condition(self, new_condition):
        self.__condition = new_condition

    #public method
    def display(self):
        print(f"Patient Name: {self._name}, Condition: {self.__condition}")


class Inpatient(Patient):
    def __init__(self, name, condition, room_number):
        super().__init__(name, condition)
        self.room_number = room_number      #public

    def display(self):
        super().display()  # prints patient info
        print(f"Room Number: {self.room_number}")


class Outpatient(Patient):
    def __init__(self, name, condition, appointment_date):
        super().__init__(name, condition)
        self._appointment_date = appointment_date

    def display(self):
        super().display()
        print(f"Appointment Date: {self._appointment_date}")


# Objects
p1 = Inpatient("mark allan", "cold", 2001)
p2 = Outpatient("lisa ray", "flu", "2024-07-15")

# Display info
p1.display()
print()
p2.display()

print("\nUpdating conditions...\n")
p1.set_condition("recovered")

p1.display()
