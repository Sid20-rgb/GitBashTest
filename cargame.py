''' Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
          >start
           Car had already started!!
        > stop
          Car stopped..
          >stop
           Car had already stopped!!
        > quit'''

print("help")

print('''start - to start the car
stop - to stop the car
quit - to exit"))

if a == "start":
    print("Car Started... Ready to go!!")
elif a == "stop":
    print("Car stopped..")
elif a == "quit":
    exit()
else:
    print("I don't understand this")

b = str(input("Enter:"))

if b == "start":
    print("Car had already started!!")

elif b == "stop":
    print("Car had already stopped!!")

elif b == "quit":
    exit()
else:
      print("I dont understand this")