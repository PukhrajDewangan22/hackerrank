

class Person:
  def __init__(self, name, age):
    self.name = age
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
del p1
print(p1.age)