#Guess Number
"""Will guess what number the user is thinking of"""

#import math module for log calculation
import math

#Initialise empty list of numbers
number_list = []

#Make function that gets user input for lowest & highest number
def get_numbers():
    print("Think of a range of numbers")
    print()
    print("Type the lowest number in the range:")
    low_number = int(input())
    print()
    print("Type the highest number in the range:")
    high_number = int(input())
    print()

    return low_number, high_number

#Make function that makes list of numbers in a range
def make_number_list(low_number, high_number):

    """Makes a consecutive list of numbers given the lowest and highest"""
    
    for i in range(low_number, high_number + 1):
        number_list.append(i)


#Make binary search function
def binary_search(list):
    
    """Performs a binary search on a list of consecutive integers, guessing what the user
    is thinking of"""

    #low is first element, high is last
    low = 0
    high = len(list) - 1

    #create attempt counter
    attempts = 0

    print("Now think of a number and I will try and guess it.")
    print("Press 1 if it's too low, 2 if it's too high, and 3 if I'm right.")

    while True:

        #increase attempts
        attempts = attempts + 1

        print()

        #mid is median of remaining possibilities rounded down
        mid = (low + high) // 2
        print(f"My guess is {number_list[mid]}.")
        print("Is it too low (1), too high (2), or correct (3)?")
        user_input = input()
        
        #If guess is too low, update low
        if user_input == '1':
            low = mid + 1
        
        #If guess is too high, update high
        elif user_input == '2':
            high = mid - 1

        #If guess is right, break out of loop
        elif user_input == '3':
            break
    print()
    print(f"Told you! It only took me {attempts} attempts!")

print()
print()

print("I will try and guess the number you are thinking of within a range.")
print()

low_number, high_number = get_numbers()

make_number_list(low_number, high_number)

#The maximum number of guesses are log n (base 2)
max_guesses = math.log(len(number_list), 2)
#round it up
max_guesses = math.ceil(max_guesses)
#turn it into an integer
max_guesses = int(max_guesses)

print(f"I bet I can guess your number in no more than {max_guesses} tries!")
print()

binary_search(number_list)
