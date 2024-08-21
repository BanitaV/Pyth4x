Home Work Task 3, 4, 5


### Task #3
- Explain the difference between the = operator and the == operator in Python.
  =  used for assignement -> assigns a value to a variable
a=5
print(a)
# o/p =  5

  == Comparision->equal to oprator to comparison two values

a=10
b=20
print (a==b, 'equal to')
# o/p =  False

- What does the ** operator do in Python, and how is it used?
  Python-> ** operator use for power

- What does the ^ operator do in Python, and in what context is it commonly used?
   Used to perform a bitwise XOR operation on the individual bits of two operands. The XOR operator returns 1
   if the corresponding bits in the two operands are different, and 0 if they are the same.


### Task #4
- Write a Python program to calculate the area of a circle given its radius using the formula
``` area=π×r^2``` ( Take pie as 3.14)
# 1-way
pi=3.141592653589793
radius = float(input("Enter the radius of the circle: "))
area= pi*radius*radius
print ( f"{area:.2f}")

# 2-way
pi= 3.141592653589793
radius = float(input("Enter the radius of the circle: "))
print (f"{pi * pow(radius,2):.2f}")



### Task #5
- Create a program that takes two numbers as input and prints whether
the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter the number = "))
num2 = int(input("Enter the number = "))

if num1 == num2:
    print("num1 value is equal to num2")
elif num1>num2:
    print("num1 value is greater than num2")
else:
    print("num1 value is less than num2")

### Task #6
- Develop a Python script that calculates the square and cube of a given number.

num = int(input("enter the number:\n"))
square = num ** 2
cube = num ** 3
print("The square is =", square)
print(f"The cube of {num} is: {cube}")

# 2 way
num = int(input("Enter the number: \n"))
print("Square of the", num, "is", num**2)
print("Cube of the", num, "is", num**3)

# Alternatively way -> Pow function

print("Square of the", num, "using pow function is", pow(num,2))
print("Cube of the", num, "using pow function is", pow(num,3))