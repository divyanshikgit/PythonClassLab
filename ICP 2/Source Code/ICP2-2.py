
# Input is taken from user
inputnumber = int(input("Enter the number for the steps to reduce it to zero"))
num = inputnumber
even = " is even; divide by 2 and obtain"
odd = " is odd; subtract 1 and obtain"
steps = 1
while num > 0:
    if num % 2 == 0:                # If the number is even then divide it by 2
        print("\nstep", steps)      # To print the step
        print(num, even, num/2)
        num = num/2
    else:                           # If number is odd then subtract it by 1
        print("\nstep", steps)      # To print the step
        print(num, odd, num-1)
        num = num-1
    steps = steps+1







