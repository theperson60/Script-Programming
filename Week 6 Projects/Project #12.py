filename = input("Enter input file name: ")

print("\n%-15s%-10s%-10s"%("Name", "Hours", "Total Pay"))
for line in open(filename):
    line = line.strip()

    if line != "":
        (name, wage, hours) = line.split()

        wage = float(wage)
        hours = int(hours)
        pay = wage * hours

        print("%-15s%-10d%-10.2f"%(name, hours, pay))
