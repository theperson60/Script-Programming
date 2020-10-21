import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

count = int(math.ceil(math.log(larger + 1) / math.log(2)))
print("Maximum guesses is %d" %count)
i = 0
while(i < count):
    number = (smaller + larger) // 2
    
    print("%d %d" %(smaller, larger))
    print("Your number is %d" %number)
    
    choice = input("Enter =, <, or >: ")
    if(choice == '='):
        print("I got it in %d tries." %(i + 1))
        break
    elif(smaller == larger):
        print("You cheated.")
        break
    elif(choice == '<'):
        larger = number - 1
        i = i + 1
    elif(choice == '>'):
        smaller =number + 1
        i = i + 1
    if(i >= count):
        print("You cheated.")
