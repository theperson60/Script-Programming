def median(numbers):
    if len(numbers) == 0:
        return 0

    numbers.sort()

    midIndex = int(len(numbers) / 2)

    if len(numbers) % 2 == 1:
        return numbers[midIndex]
    else:
        return (numbers[midIndex] + numbers[midIndex - 1]) / 2

def mean(numbers):
    if len(numbers) == 0:
        return 0

    total = 0
    for x in numbers:
        total += x

    return total / len(numbers)
    

def mode(numbers):
    if len(numbers) == 0:
        return 0

    numberDict = {}
    for digit in numbers:
        number = numberDict.get(digit, None)
        if number == None:
            numberDict[digit] = 1
        else:
            numberDict[digit] = number + 1

    maxValue = max(numberDict.values())
    modeList = []
    for key in numberDict:
        if numberDict[key] == maxValue:
            modeList.append(key)

    return modeList

def main():
    numbers = [37, 12, 10, 19, 21, 27, 14, 13, 6, 14, 7, 3, 41, 36, 12]

    print(median(numbers))
    print(mean(numbers))
    print(mode(numbers))

main()
