number_of_guests = int(input('Enter the number of guests:\n'))
if number_of_guests < 20:
    print('home')
elif number_of_guests > 50:
    print('restaurant')
else:
    print('cafe')
