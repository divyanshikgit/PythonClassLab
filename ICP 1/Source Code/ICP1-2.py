# Take two numbers from user and perform arithmetic operations on them.

num1 = input("Please Enter your 1st Number")          #Taking input from the user
num2 = input("Please Enter your 2nd Number")          #Taking input from the user

print("Below are the Arithmetic operations ")
A = int(num1)
B = int(num2)            #Assign them to a different int variable
print("Addition of ",A, "and" ,B,"is",A+B)          #Printing the output with the operation
print("Multiplication of",A," and ",B,"is",A*B)
print("Subtraction of ",A, "and" ,B,"is",A-B)
print("Division of ",A, "and" ,B,"is",A/B)