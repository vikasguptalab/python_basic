#!/usr/bin/python

class Car:

    owner = "vikas.gupta"
    location = "bhopal"

    def __init__(self,modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname,self.year, self.owner, self.location)


c = Car("Tata", 2010)
c.display();

try:
    del c.year;
    c.display();
except AttributeError:
    print("Some data is missing")
except:
    print("Next time")