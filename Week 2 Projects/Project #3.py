newCount = int(input("Enter amount of new videos rented: "))
oldCount = int(input("Enter amount of old videos rented: "))
cost = "${:,.2f}".format((newCount * 3) + (oldCount * 2))
print("The total cost is: ", cost)
