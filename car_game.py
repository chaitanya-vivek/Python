command = ""
started = False
while True:
    command = input("> ").lower()    
    if command == "start":
        if started:
            print("Car is already started !")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped !")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start = to start the car in the race.
stop = to stop the car in the race.
quit = to quit the race.
help = to view all the commands used in the race.
        """)

    elif command == "quit":
        print("I am quiting")
        break
    else:
        print("Sorry, I dont' understand that!")