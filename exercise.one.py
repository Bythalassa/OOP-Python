# ============================================================
#  OOP Practice – Class, Method & Object
#  Clean modern Python (3.10+) style – 2026 edition
# ============================================================

#  improvements:
#   • @dataclass  → auto-generates __init__ for free (no boilerplate = repetitive code)
#   Also init was totally re written.
#   • __str__     → clean way to print an object's internal data

from dataclasses import dataclass, asdict


@dataclass
class Student:
    name:    str
    age:     int
    subject: str
    food:    str

    # ── METHOD 1 (special): handled automatically by @dataclass ──
    # __init__ is generated behind the scenes — no need to write it!

    # ── METHOD 2 ─────────────────────────────────────────────────
    def learn(self) -> str:
        return f"Hi, I am {self.name}. I study {self.subject}."

    # ── METHOD 3 ─────────────────────────────────────────────────
    def eat(self) -> str:
        return f"Hi, I am hungry. I like to eat {self.food}."

    # ── BONUS METHOD: internal data decomposition ─────────────────
    def data(self) -> dict:
        return asdict(self)   # converts the object to a dictionary


# ── 2. THE OBJECT (real instance built from the blueprint) ────

alex = Student(
    name    = "Alex",
    age     = 18,
    subject = "Computer Science",
    food    = "Nutella",
)


# ── 3. ACTIONS (calling the methods) ─────────────────────────

print(alex.learn())
print(alex.eat())


# ── EXTRA: internal data decomposition ───────────────────────

print(alex.data())


# ── PRACTICE ZONE ────────────────────────────────────────────
#  Try creating your own student below!
#
#  maria = Student(
#      name    = "Maria",
#      age     = 20,
#      subject = "Biology",
#      food    = "Sushi",
#  )
#  print(maria.learn())
#  print(maria.eat())
#  print(maria.data())
