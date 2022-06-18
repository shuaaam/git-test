'''' This file with all classes in our project '''


class Person:
    def __init__(self, fullname, phone, age, location):
        self.fullname = fullname
        self.phone = phone
        self.age = age
        self.location = location


class Work:
    def __init__(self, position, department, salary):
        self.position = position
        self.department = department
        self.salary = salary
