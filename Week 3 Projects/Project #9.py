#takes input for number of kilometers
kilometers = float(input("Enter number of kilometers: "))

#calculates nautical miles
nMiles = (kilometers * 90 * 60) / 10000;

#output
print('%0.3f kilometers = %0.3f Nautical Miles' %(kilometers, nMiles))
