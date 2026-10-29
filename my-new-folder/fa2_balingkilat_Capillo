'''
Zach Radix P. Capillo  9-Balingkilat
'''
class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_bill_amount(self) -> float:
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float):
        if bill_amount > 0:
            self.__bill_amount = bill_amount
        else:
            print("Bill amount must be positive")

    def calculate_bill(self) -> float:
        return self.__bill_amount


class SeniorPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self) -> float:
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self) -> float:
        return self.get_bill_amount() * 0.85


if __name__ == "__main__":
    patient_regular = Patient("Juan Dela Cruz", 15000.0)
    patient_senior = SeniorPatient("Maria Santos", 15000.0)
    patient_philhealth = PhilHealthPatient("Pedro Reyes", 15000.0)

    print("Hospital Billing System\n\n")
    print("-----------------------\n\n")
    print(f"Regular Patient: {patient_regular.get_name()}")
    print(f"Original Bill: ₱{patient_regular.get_bill_amount()}")
    print(f"Final Bill: ₱{patient_regular.calculate_bill():.2f}\n")
    print(f"Senior Patient: {patient_senior.get_name()}")
    print(f"Original Bill: ₱{patient_senior.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient_senior.calculate_bill():.2f}\n")
    print(f"PhilHealth Patient: {patient_philhealth.get_name()}")
    print(f"Original Bill: ₱{patient_philhealth.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient_philhealth.calculate_bill():.2f}\n")
