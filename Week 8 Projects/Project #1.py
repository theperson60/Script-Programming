def newton(x):
    tolerance = 0.000001
    estimate = 1.0

    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)

        if difference <= tolerance:
            break
    return estimate

def main():
    while True:
        try:
            x = int(input("Enter a positive number or press enter to quit: "))
            print("newton = %0.15f" % newton(x))
        except:
            return

main()
