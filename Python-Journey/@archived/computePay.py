# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

def computepay(h, r):
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. 
    if hours<=40:
        return (hours*ratesPerHour)
    else:
        return ((40*ratesPerHour)+(hours-40)*(1.5*ratesPerHour))

# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
hrs = input("Enter Hours: ")

# You should use input to read a string and float() to convert the string to a number.
try:
    hours = float(hrs)
except:
    print("Please enter hours in Numerals only without commas");
    quit()

rps = input("Input Rates per hour: ")

try:
    ratesPerHour = float(rps)
except:
    print("Please enter Rates Per Hour in Numerals only without commas");
    quit()

# print("Pay",computepay(hours,ratesPerHour));
print("Hello","World");
print("Hello"+"World");


