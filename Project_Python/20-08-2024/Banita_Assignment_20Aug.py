Task #7
✅ Leap Year Checker:

img_1.png

Create a program that determines whether a given year is a leap year. A leap year is divisible by 4,
but not by 100 unless it is also divisible by 400. Use an if-else statement to make this determination.

leap_year = int(input("enter the year : "))
if leap_year % 4 ==0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    print(f"leap year -> {leap_year}")
else:
    print(f"not a leap year -> {leap_year}")



Task #8
✅ Triangle Classifier:

img.png

Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral
(all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.

side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

# Determine the type of triangle
if side1 == side2 and side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

Task #9
✅ FizzBuzz Test: Write a program that prints numbers from 1 to 100.
# Loop For However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5,
# print "FizzBuzz."
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)