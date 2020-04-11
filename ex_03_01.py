xh = input("Enter hours:")
xr = input("Enter rates:")
hours = float(xh)
rates = float(xr)
if (hours < 40):
    pay = hours * rates
else:
    pay = 40 * rates + (hours - 40) * rates * 1.5
print("Pay:", pay)

