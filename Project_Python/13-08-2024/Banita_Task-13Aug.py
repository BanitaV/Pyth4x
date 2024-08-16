# ____________________________________________________Task 1

# Home Can you create a Program I will give you number(userinput and print table)
'''
f"{}" String format concept
User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10
'''
table=  int(input('enter the nuber='))

print(  f"{table}*1={table}")
print(  f"{table}*2={table*2}")
print(  f"{table}*3={table*3}")
print(  f"{table}*4={table*4}")
print(  f"{table}*5={table*5}")
print(  f"{table}*6={table*6}")
print(  f"{table}*7={table*7}")
print(  f"{table}*8={table*8}")
print(  f"{table}*9={table*9}")
print(  f"{table}*10={table*10}")


# ---------------------------------------------------Task 2

# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}


#a=10
#b=20

a= int(input('Enter number 1='))
b= int(input('Enter number 2='))
print (a+b)  #30
print (a-b)   #-10
print (a*b)  # 200
print (a/b)   #0.5

'''
result = max(10, 20)
print (result)
'''
a= int(input('Enter number 1='))
b= int(input('Enter number 2='))
print ('Maximum value is =', max( a,b))
print ('Power value is =', pow(a,b))



# a=31.24556
# formated_number= f"{a:.2f}"
# print (formated_number)

a= float(input('Enter number='))
formated_number= f"{a:.3f}"
print (formated_number)


