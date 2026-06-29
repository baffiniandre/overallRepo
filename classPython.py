class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def getPersonInfo(self): #self here is needed because the method accesses the instance/Object of the class.
        info = {"Name":self.name, "Age": self.age, "Sex": self.sex}
        #info = {"Name":name, "Age": age, "Sex": sex}
        return info
    
    @staticmethod #annotation needed for statis methods.
    def underAge(age):
        return age<18

    @classmethod #A class method might need to interact with the classitseld, not the instance that is created. for this, intead of self, we use cls
    def createNewBorn(cls, name, sex):
        return cls(name, age=0, sex=sex)


person1 = Person("Andre", 29, "male")
print(person1.getPersonInfo())

person1.name

person1.underAge(person1.age)

person2 = Person.createNewBorn("Sam", "Male")
