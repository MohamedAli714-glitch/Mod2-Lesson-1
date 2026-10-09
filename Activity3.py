print('select your ride')
print('1. bike 2. car')

choice=int(input('Enter your choice: '))

if choice==1:
    print('You have selected bike you have 2 options')
    print('1. scooty 2. scooter')

    choice2=int(input('Enter your choice: '))
    if choice2==1:
        print('You have selected scooty')
    else:
        print('You have selected scooter')


elif choice==2:
    print('You have selected car you have 2 options')
    print('1.4x4 2. sedan')

    choice3=int(input('Enter your choice: '))
    if choice3==1:
        print('You have selected 4x4')
    else:
        print('You have selected sedan')

else:
    print('Invalid choice')