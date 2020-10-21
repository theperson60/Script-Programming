numberOfIterations = int(input("Enter the number of iterations: "));

piDividedFour = 0;
iterationCounter = 1;

for i in range(1, numberOfIterations + 1):
    if(i % 2 != 0):
        piDividedFour = piDividedFour + 1 / iterationCounter;
    else:
        piDividedFour = piDividedFour - 1 / iterationCounter;
    iterationCounter += 2;

pi = piDividedFour * 4;

print("The approximation of pi is", pi);
