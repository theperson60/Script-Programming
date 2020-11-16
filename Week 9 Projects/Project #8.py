def printAll(seq):          #Lee's function definition
    if seq:                 #Until the last element of sequence
        print(seq[0])       #Print first element
        printAll(seq[1:])   #Call function with next element to last

printAll("asdfjkl;") #String
printAll((1, 2, 3, 4)) #Tuple
printAll([1, 2, 3, 4]) #List