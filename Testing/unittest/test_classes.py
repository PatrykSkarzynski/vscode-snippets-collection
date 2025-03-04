import unittest


# class 'Person' that has a method introduction which gives welcome string:
class Person:
    def __init__(self, name, age):
        self. name = name
        self.age = age

    def introduction(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
# class 'Employee' that inherits from the class 'Person' and expands it and introduction with 'position':
class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def introduction(self):
        return super().introduction() + f" I work as a {self.position}"
    
# class that will test earlier classes and inherits from 'unittest.TestCase':
class PersonAndEmployeeTest(unittest.TestCase):
    # creating method 'setUp' to prepare context for every test, will be called before every test methods:
    def setUp(self):
        self.person = Person("John", 30)
        self.employee = Employee("Anna", 40, "Engineer")

    # creating method "tearDown" which will clear context after every test, will be called after every test method:
    def tearDown(self):
        del self.person
        del self.employee

    # creating test method 'test_person_introduction' which checks if 'introduction' method of class 'Person' works properly:
    def test_person_introduction(self):
        self.assertEqual(self.person.introduction(),
                         "My name is John and I am 30 years old.")
        
    # creating test method 'test_employee_introduction' which checks if 'introduction' method of class 'Employee' works properly:
    def test_employee_introduction(self):
        self.assertEqual(self.employee.introduction(),
                         "My name is Anna and I am 40 years old. I work as a Engineer")
        
# condition that checks whether the script was run directly and not imported as a module, if so then function 'unittest.main()' runs every test method defined in the class:
if __name__ == '__main__':
    unittest.main()



# Expected result when True in terminal:
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK