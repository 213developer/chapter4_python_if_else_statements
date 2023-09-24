# LargeSmall.py - This program calculates the largest and smallest of three integer values.
# Declare and initialize variables here
largest = None
smallest = None

# Prompt the user to enter 3 integer values

firstNumber = input("type first number")
secondNumber = input("type second number")
thirdNumber = input("type third number")


# Write assignments, and necessary if else statements here as appropriate

# Here I'm getting the largest
if firstNumber > secondNumber:
    if firstNumber > thirdNumber:
     largest = firstNumber
elif secondNumber > thirdNumber:
    if secondNumber > firstNumber:
        largest = secondNumber
else:
    largest = thirdNumber


if firstNumber < secondNumber:
    if firstNumber < thirdNumber:
     smallest = firstNumber
elif secondNumber < thirdNumber:
    if secondNumber < firstNumber:
        smallest = secondNumber
else:
    smallest = thirdNumber



# Output largest and smallest number.
print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))
