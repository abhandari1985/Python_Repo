# https://docs.python.org/3/tutorial/classes.html#class-definition-syntax


class student:  # class student
    def __init__(self, name, rollno, marks):  # class attributes name,rollno,marks
        self.name = name
        self.rollno = rollno
        self.marks = marks
        print("address of self: ", id(self))


obj = student("Rishaan", "28", "95")
student1 = student("nivaan", "21", "100")  # object student1
student2 = student("vivaan", "26", "97")  # object student2
print("address of class object: ", id(obj))
print("address of class object: ", id(student1))
print("address of class object: ", id(student2))

print(
    student1.name, student2.name
)  # print attributes of the object | object name.attribute name

# Questionaire
# self in Python class : Self represents instance(object) of the class. By using self we can access
# the attributes and methods of the class in Python. It binds attribute with given arguments
# self is not a keyword in Python. Self is just a parameter name used in instance methods to refer
# to the instance itself. It is a pointer to current object
# https://www.geeksforgeeks.org/self-in-python-class/
