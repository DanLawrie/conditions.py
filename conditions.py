temp = 0
x = 0
while x == 0:
    temp = float(input("Please enter the current tempature "))
    if temp == 999:
        x = x+1
    elif temp > 90:
        print("Wear shorts")
    elif temp > 70:
        print("Short Sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay Inside")

