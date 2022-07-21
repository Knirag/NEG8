
month = input("Input the month:")
print(month + ":")
if month == "February":
    print("28/29 Days")
elif month in ("April", "June", "September", "November"):
    print("30days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
    print("31 Days")
else:
    print("Invalid Month!")