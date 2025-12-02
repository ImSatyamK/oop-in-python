class Engineer:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return f"first name: {self.fname}, last name: {self.lname}"
    
class SoftwareEngineer(Engineer):
    def __init__(self, name, level, salary):
        fname, lname = name.split(" ")
        super().__init__(fname, lname)  # Calling the constructor of the parent class
        self.level = level
        self.salary = salary

    def welcome(self):
        return f"We welcome Mr. {self.full_name()} for the post of {self.level}."
    
    def salary_info(self):
        return f"{self.full_name()}'s salary is {self.salary} USD."
    
se1 = SoftwareEngineer("John Doe", "Senior Dev", 90000)
print(se1.full_name())        # Inherited method
print(se1.welcome())     # Child class method
print(se1.salary_info()) # Child class method