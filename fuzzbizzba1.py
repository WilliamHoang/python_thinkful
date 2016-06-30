import sys

if len(sys.argv) <= 1 or (not isinstance( sys.argv[1], int )):
    print ("You didn't enter a limit as an argument to the fizzbuzz program")
    while True:
        try:
            my_input = int(input("Enter a numerical limit: "))
            break
        except (NameError, TypeError):
            print("Oops!  That was no valid number.  Try again...")
    limit = int(my_input)
    print(limit)
else:
    limit = int(sys.argv[1])
    print (limit)

for x in range(1,limit):
    if (x % 3 == 0) and (x % 5 == 0):
        print ("FizzBuzz")
    elif (x % 3 == 0) and (x % 5 != 0):
        print ("Fizz")
    elif (x % 3 != 0) and (x % 5 == 0):
        print ("Buzz")
    else:
        print (x)