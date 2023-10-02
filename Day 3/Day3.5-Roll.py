bill=0
height = int(input("What is your Height in cm ? "))
if height >=120:
    print("welcomet")
    age = int(input("What is your age? "))
    if age <=12:
        bill=5
        print ("Your ticket is $5.")
    elif age <= 18:
        bill=8
        print("Your ticket is $7.")
    else:
        print("Your ticket is $12.")
        bill=12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill+=3
        #photo price is $3
    print(f"your final bill is {bill}")
else:
    print ("Sorry, you have to grow taller")