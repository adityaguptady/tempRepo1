# print("Hello world")
#
# #This is comment
#
# '''This is
# also an example
# of multi-line comment'''
#
#
# print("statement 1")
# print("statement 2")
# print("statement 3")
# print("statement 4")
# print("statement 5")
#
# age = 4
# print(age)
# age = "Four"
# print(age)

# name = "Aditya"
# profession = "Software developer"
# experience = 10
# print("Hello, I am",name,". I am a ", profession, " professionally. And I have around ", experience, " with it!")

# name = input("Please enter your name: ")
# print("Hello ", name)

# x = input("Enter first value for sum: ")
# y = input("Enter second value for sum: ")
# z = int(x) + int(y)
# print("Sum: ",z)

#x = 5
#print("Type of x is: ", type(x))
# Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

# largest_number = max(number1, number2, number3)
# lowest_number = min(number1, number2, number3)

# Print the result.
# print("The largest number is:", largest_number)
# print("The lowest number is:", lowest_number)

# for counter in range(10):
#     print("The value of counter is currently", counter)
# print("-------")
# for counter in range(2, 8):
#     print("The value of counter is currently", counter)
# print("-------")
# for counter in range(2, 8, 3):
#     print("The value of counter is currently", counter)
# print("-------")

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    print("day[11]: ", day[11])
    print("day: ", day)
    print("len(day): ", len(day))
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)
