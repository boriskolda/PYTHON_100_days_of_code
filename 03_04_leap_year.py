year = int(input("Which year do you want to check if it is a leap year? "))

if (year % 4 ) > 0:
    print("Not leap year")
else:
   if (year % 100) > 0:
        print("Leap year")
   else:
    if (year % 400) > 0:
        print("Not leap year")
    else:
        print("Leap year")
