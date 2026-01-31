import random
import sys

print("Think of a number.")
print("I, the AI, will try to guess it!")
guesser = input("Do YOU want to guess instead?(y, n)").lower()
dif = input("Choose difficulty:(1, 2, 3)")

if dif == "1":
    high = 20
    print("Think of a number between 1 and 20")
elif dif == "2":
    high = 100
    print("Think of a number between 1 and 100.")
elif dif == "3":
    high = 500
    print("Think of a number between 1 and 500")
else:
    print("You did not choose a difficulty. You difficulty will be set to 2")
    print("Think of a number between 1 and 100.")
low = 0
guesses = 0


if guesser == "n":
    while True:
        if random.randint(1,2) == 1:
            guess = random.randint(low, high)
        else:
            guess = ((low + high) // 2)
        print(f"My guess is: {guess}")
        guesses += 1

        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == "c":
            print(f"I guessed it in {guesses} tries!")
            sys.exit()
        elif feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print("Please type H, L, or C.")
elif guesser == "y":
    num = random.randint(low, high)
    print("Guess the Number!")
    while True:
        guess = input("Enter a number: ")
        guess = int(guess)
        if type(guess) == int:
                
            guesses += 1
                
            if guess == num:
                print(f"You got the number in {guesses} tries!")
                print("Hellllo!!!!!!")
                print("Me a tiny Berry with Hookster!")

                sys.exit()
                
            elif guess >= num:
                print("Too high!")
                    
            elif guess <= num:
                print("Too low!")
                
        else:
            print("Please enter a number.")
else:
    print("Enter 'y' or 'n' next time.")
    
