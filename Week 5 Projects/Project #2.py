sideOne = float(input("Enter the length of side 1: "))
sideTwo = float(input("Enter the length of side 2: "))
sideThree = float(input("Enter the length of side 3: "))

if((sideOne ** 2) == ((sideTwo ** 2) + (sideThree ** 2))):
    print("Triangle is a right triangle.")
elif((sideTwo ** 2) == ((sideThree ** 2) + (sideOne ** 2))):
    print("Triangle is a right triangle.")
elif((sideThree ** 2) == ((sideOne ** 2) + (sideTwo ** 2))):
    print("Triangle is a right triangle.")
else:
    print("Triangle is not a right triangle.")
