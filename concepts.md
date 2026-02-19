# 📝 Class

- **example one:** In the real world, everything has descriptive data. A Student, our **Subject** in this example, has a Name and Age. A Student is able to do **actions** such as learn and eat.

Now let's translate this to Python.

- **One Class:** We design a Student. So Student is a Class in Python.

```python
class Student:
    pass
```

This Class defines what characteristics all **"Students"** own and what actions they are able to do.

```python
class Student:
    def __init__(self, name, age, subject, food):
        self.name = name
        self.age = age
        self.subject = subject
        self.food = food

    def learn(self):
        return f"Hi, I am {self.name}. I study {self.subject}."

    def eat(self):
        return f"Hi, I am hungry. I like to eat {self.food}."
```

The Class Student becomes a blueprint. All Class elements designed act as individual blueprints.

---

# 📝 Method

A Method is a function inside a Class.  
In our example we use:

- `__init__` → Method 1  
- `learn` → Method 2  
- `eat` → Method 3  

`__init__` is a **special method**: it initializes object attributes, while the other methods define behaviors.

---

# 📝 Object

- **description:** In this example Python uses the "Student" Class to create a real Object. The Object is "Alex". An Object holds actual data and can perform actions.

```python
alex = Student("Alex", 18, "Computer Science", "Nutella")
```

- **example actions:**

```python
print(alex.learn())
print(alex.eat())
```

---

# 📝 Extra decomposition: Internal Data from Object "alex"

```python
{'name': 'Alex', 'age': 18, 'subject': 'Computer Science', 'food': 'Nutella'}
```
