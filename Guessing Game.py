import random 

number = random.randint(1,20) 
player_name = input ("Hello. Please input your name: ")
number_of_guesses = 0 
print ("Okay", player_name, "I am guessing a number between 1 and 20, guess the number: ")

while number_of_guesses < 5: 
    guess = int(input()) 
    number_of_guesses += 1
    print ("This is your", str(number_of_guesses), "guess.")

    if guess < number: 
        print ("This is less than the actual value")
    if guess > number: 
        print ("This is greater than the actual value")
    if guess == number: 
        break 

if guess == number: 
    print("Congrats!!")
else: 
    print("Sorry that's incorrect. The number is", number, "Please try again")

