total = 0.0
i = 0

while True:
    print("Press enter with no number to end.")
    data = input("Enter a number: ")

    if data == '':
        break

    number = float(data)
    total = total + number
    i += 1

average = total / i

print("Sum is %d" %total)
print("Average is %d" %average)

