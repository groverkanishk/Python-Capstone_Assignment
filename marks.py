'''
Name: Kanishk Grover
Roll No: 2501060071
Program: BCA (AI & DS)
'''

# Base class - Person
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Derived class - Student (inherits from Person)
class student(person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        super().display()
        print(f"Course: {self.course}")

# Derived class - Exam (inherits from Student)
class exam(student):
    def __init__(self, name, age, course, mark1, mark2, mark3):
        super().__init__(name, age, course)
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def total(self):
        return self.mark1 + self.mark2 + self.mark3
    
    def display(self):
        super().display()
        print(f"Marks in subject 1: {self.mark1}")
        print(f"Marks in subject 2: {self.mark2}")
        print(f"Marks in subject 3: {self.mark3}")
        print(f"Total marks: {self.total()}")

# Instantiation with sample data
print("STDENT EXAM REPORT")
print("=" * 50)
student1 = exam("Aman Gupta", 20, "Computer Science", 85, 90, 88)
student1.display()

print("\n" + "=" * 50)

student2 = exam("Rohan Sharma", 19, "Business Management", 78, 83, 95)
student2.display()