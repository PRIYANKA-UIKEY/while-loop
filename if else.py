month=(input("enter the month...."))
if month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december":
    print("31")
elif month=="april" or month=="june" or month=="september" or month=="november":
    print("30")
elif month=="february":
    print("28 29")