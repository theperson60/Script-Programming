import math

numberOfOrganisms = int(input("Enter the initial number of organisms: "))
growthRate = float(input("Enter the desired growth rate: "))
growthPeriod = float(input("Enter amount of time required to achieve growth rate in hours: "))
growthTime = float(input("Enter amount of time allowed to grow: "))

totalOrganisms = math.floor(numberOfOrganisms * growthRate ** (growthTime / growthPeriod))

print("Total number of organisms after", growthTime, "hours is: ", totalOrganisms)
