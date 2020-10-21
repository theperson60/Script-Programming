#request input
hourlyWage = float(input("Enter hourly wage: "));
regularHours = float(input("Enter regular hours: "));
overtimeHours = float(input("Enter overtime hours: "));

#calculate pay
regularPay = hourlyWage * regularHours;
overtimePay = (hourlyWage * 1.5) * overtimeHours;
totalPay = regularPay + overtimePay;

#output
print("Weekly pay is: $" + str(totalPay));
