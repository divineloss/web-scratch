import name_gen as ng
import age_gen as ag
import gender_gen as gg
import income_gen as ig
import status_gen as sg

class Person():
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = None
        self.income = 0.0
        self.status = None