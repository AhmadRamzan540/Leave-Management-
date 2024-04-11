class Employee:
    def __init__(self, name, initial_balance):
        self.name = name
        self.leave_balance = initial_balance

    def apply_leave(self, days):
        if days <= self.leave_balance:
            self.leave_balance -= days
            print(f"{self.name} has taken {days} days leave. Remaining balance: {self.leave_balance}")
        else:
            print(f"Insufficient leave balance for {self.name}")

    def add_leave(self, days):
        self.leave_balance += days
        print(f"{days} days leave added for {self.name}. New balance: {self.leave_balance}")

# Example usage:
employee1 = Employee("Ali", 20)
employee2 = Employee("Haider", 15)

employee1.apply_leave(5)
employee2.apply_leave(10)

employee1.add_leave(3)
employee2.apply_leave(8)