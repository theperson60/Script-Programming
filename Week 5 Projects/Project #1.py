sideOne = float(input("Enter the length of side 1: "))
sideTwo = float(input("Enter the length of side 2: "))
sideThree = float(input("Enter the length of side 3: "))

if (sideOne == sideTwo):
    if(sideTwo == sideThree):
        print("Triangle is an equilateral triangle.")
    else:
        print("Triangle is not an equilateral triangle.")
else:
    print("Triangle is not an equilateral triangle.")
