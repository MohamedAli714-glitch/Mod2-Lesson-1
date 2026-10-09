medical_note=input('Do you have a medical note? (y/n): ')

if medical_note=='y':
    print('You can take the test.')

else:
    atten=int(input('What is your attendance percentage? '))
    if atten>=50:
        print('You can take the test.')
    else:
        print('You cannot take the test.')
