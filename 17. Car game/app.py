is_playing = True
is_car_started = False

while is_playing:
    
    command = input(">").lower()
    if command == "start":
        if not is_car_started:
            is_car_started = True
            print("Car started...Ready to go")
        else:
            print("Car already started")
    elif command == "stop":
        if is_car_started:
            is_car_started = False
            print("car stopped")
        else:
            print("Car is stopped already")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """
        )
    elif command == "quit":
        print("You exit the game")
        is_playing = False
    else:
        print("Type 'help' to see the commands")