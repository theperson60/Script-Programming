import functools

filename = input("Enter filename: ")

#Open file, put it into list, split list
file = open(filename, 'r').read().split()
file = list(map(int, file))
print(file)

#Print the average
print("\nThe average is", functools.reduce(lambda x, y: x + y / len(file), file, 0))