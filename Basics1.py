#Variables - name dont start with a number
name='mike'
print(name)

n=input("Enter username:")
print("welcome",n)

#Data Types - int, float, str and boolean - Case sensitive cap T and F
emp_id=121126
org='Microsoft'
sal=3400000.99
fte=True
print(type(emp_id))
print(type(org))
print(type(sal))
print(type(fte))

#TypeCasting: Change data type
print(float(100))
print(int(100.99))
print(int("121"))

#print(int("121.88")) -- ERROR
print(str(200))
print(int(True))
print(int(False))
print(float(True))
print(float(False))
print(bool(1))
print(bool(0))
#print(type(name))

#Arithmetic operators
#Operator precedence rule>> https://docs.python.org/3.7/reference/expressions.html#operator-precedence
a = 4+(8**2)-3**2%1 
print(a)

b = 4%(1+ 9)**2 - 60//(7+2)
print(b)