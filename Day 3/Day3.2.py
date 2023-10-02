height = int(input("What is your Height in cm ? "))
if height >=120:
    print("welcomet")
    age = int(input("What is your age? "))
    if age <=12:
        print ("Your ticket is $5.")
    elif age <= 18:
        print("Your ticket is $7.")
    else:
        print("Your ticket is $12.")
else:
    print ("you can't")