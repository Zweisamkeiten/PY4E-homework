largest = None
smallest = None

while (True):
    sn = input("Enter number:")
    if (sn == "done"):
        break
    try:
        xn = int(sn)
        if(largest == None or smallest == None):
            largest = xn
            smallest = xn
        if xn > largest:
            largest = xn
        if xn < smallest:
            smallest = xn
    except:
        print("Invalid number")

print("Maximum is", largest)
print("Minimum is", smallest)
