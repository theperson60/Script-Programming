import math

tolerance = 0.000001

x = float(input("Enter a number: "))

def newton(num, estimate = 1):
    estimate = (estimate + num / estimate) / 2
    difference = abs(num - estimate ** 2)

    if difference <= tolerance:
        return estimate
    else:
        return newton(num, estimate)

print("The program's estimate: ", newton(x))
print("Python's estimate: ", math.sqrt(x))
