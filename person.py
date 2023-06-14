import name_gen as ng
import age_gen as ag
import gender_gen as gg
import income_gen as ig
import status_gen as sg




class Person():
    def __init__(self):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.income = income
        self.status = status
    
    def create_person():
        x = Person()
        x.fname, x.lname = ng()
        x.age = ag()
        x.gender = gg()
        x.income = ig()
        x.staus = sg()