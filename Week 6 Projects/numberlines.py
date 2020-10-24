inputFilename = input("Enter input file name: ")
outputFilename = input("Enter output file name: ")

inputFile = open(inputFilename, 'r')
outputFile = open(outputFilename, 'w')

count = 1
for line in inputFile:
    outputFile.write("{:>4}> {}".format(count, line))
    count += 1

inputFile.close()
outputFile.close()
