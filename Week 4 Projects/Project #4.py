height = int(input("Enter the height from which the ball is dropped: "));
bouncinessIndex = float(input("Enter the bounciness index of the ball: "));
numberOfBounces = int(input("Enter the number of times the ball is allowed to bounce: "));

distance = 0;

while numberOfBounces > 0:
    distance = distance + height;
    height = height * bouncinessIndex;
    distance = distance + height;
    numberOfBounces -= 1;

print("Total distance traveled is:", distance, "units.")
