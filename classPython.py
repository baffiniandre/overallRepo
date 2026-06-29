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


/* important note:

Unbreakable rule in Python: **Positional arguments cannot follow keyword arguments.**

When you pass information into a function (or into a class, like `cls()`), Python lets you do it in two ways:

1. **Positional arguments:** Just passing the value directly (e.g., `name` or `sex`). Python figures out where they go based strictly on the *order* you provide them.
2. **Keyword arguments:** Explicitly stating the name of the parameter (e.g., `age=0` or `sex=sex`).

The rule is that once you use a keyword argument, **every single argument after it must also be a keyword argument.**

### Why the second one fails

If you write `return cls(name, age=0, sex)`, here is how Python reads it from left to right:

1. `name` — Positional argument. (Everything is fine)
2. `age=0` — Keyword argument. (Everything is fine)
3. `sex` — Positional argument. **(Crash!)**

Because `sex` is just a value sitting there without an `=` sign, it is a positional argument. But because it comes *after* `age=0`, Python gets confused and throws a `SyntaxError`.

### Two ways to write it correctly

**1. Make everything after `age` a keyword argument (What you did)**
By writing `sex=sex`, you turn that last piece of data into a keyword argument. Because keyword arguments are allowed to follow other keyword arguments, this works perfectly:

```python
return cls(name, age=0, sex=sex)

```

*(Note: `sex=sex` might look weird, but it just means "assign the parameter named `sex` the value of the variable `sex` that was passed into the method.")*

**2. Make them ALL positional arguments**
Because your `__init__` method expects the order to be `(self, name, age, sex)`, you can just pass the values in that exact order without naming any of them. Since `0` is the second thing you pass, Python automatically knows it belongs to `age`:

```python
return cls(name, 0, sex)

```
*/
