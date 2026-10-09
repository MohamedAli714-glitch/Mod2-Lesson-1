units=input('How many units of elecricity did you use this month? ')
units=int(units)

if units<50:
    amount=units*2.60
    surcharge=25

elif units<100:
    amount=units*3.25
    surcharge=35

elif units<200:
    amount=units*4.00
    surcharge=45

elif units<300:
    amount=units*4.50
    surcharge=55

else:
    amount=units*35.00
    surcharge=75

total=amount+surcharge
print(f"Total amount to be paid: ${total:.2f}")