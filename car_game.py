car = input('What would you like the car to do (start,stop,exit)? ')

if car.lower == 'start':
    car_state = 'moving'
    print(f"The car is now {car_state}.")
elif car.lower == 'stop':
    car_state = 'stopped'
    print(f"The car is now {car_state}.")
elif car.lower == 'exit':
    print('You have exited the car.')

