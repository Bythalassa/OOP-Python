## 📝 Class

- **example one:** In the real World everything has descriptive Data. A Student has a Name and Age. Furthermore, a Student is able to do **actions** such as learn and eat. Now let's translate this to Python.

- **One Class :** We design a "Student". So "Student" is a Class in Python.

´´´

class Student :

´´´

This Class defines all the characteristics in **"Students"**. As well as, all actions involved with **"Students"**.


´´´

class Student :

    def  __init__ (self, name, age, subject, food):
        self.name = name
        self.age = age
        self.subject = subject
        self.food = food

    def  learn (self): 
        return f "Hi, I am {self.name}. I study {self.subject}."

    def  eat (self): 
        return f"Hi, I am hungry. I like to eat {self.food}."

´´´

The class Student becomes a blueprint. All Class elements designed act as individual blueprints.


## 📝 Method
A Method is a function inside a Class. All functions, in our example we use __init__, learn and eat as our Method 1, Method 2 and Method 3. Extra __init__ is a special Method it Initializes object attributes, while Method 2 and 3 define a behavior.


## 📝 Object

- **description** In this example Python uses the "Student" Class to create a real Object. The Object is "Alex". An Object holds actial Data and can perform actions.

´´´
alex = Student("Alex, 18, "Computer Science", "Nutella")
´´´

- **example actions** :

´´´

print(alex.learn())
print(alex.eat())

´´´


## 📝 Extra decomposition: Internal Data from Object "alex"

´´´

{'name': 'Alex', 'age': 18, 'subject': 'Computer Science', 'food': 'Nutella'}

´´´

