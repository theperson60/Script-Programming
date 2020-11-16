
#Checks is list is in ascending order
def isSorted(lyst):
    #Checks if length of list is 0 or 1
    if len(lyst) >= 0 and len(lyst) < 2:
        return True
    else:
        #Return false if position x is greater than x + 1
        for x in range(len(lyst) - 1):
            if lyst[x] > lyst[x + 1]:
                return False
        
        #Return true if above loop does not return False
        return True

def main():
    lyst = []
    print(isSorted(lyst))
    print(lyst, "\n")
    lyst = [1]
    print(isSorted(lyst))
    print(lyst, "\n")
    lyst = list(range(10))
    print(isSorted(lyst))
    print(lyst, "\n")
    lyst[9] = 3
    print(isSorted(lyst))
    print(lyst, "\n")

main()