import random

print("📘 MATH BATTLE!")
print("Answer math facts correctly to win. \nGet them wrong and perish!")

score = 0

while True:
    dif = input("addidtion and subtraction, multiplication and division, or both?(1, 2, 3)")


    if dif == "1":


        for i in range(5):
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            

            if random.randint(1, 2) == 1:
                guess = int(input(f"{a} + {b} = "))
                answer = a + b
            else:
                guess = int(input(f"{a} - {b} = "))
                answer = a - b
                
            if guess == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The answer was {answer}.")

        print(f"\nYour final score: {score}/5")
        break
    elif dif == "2":
        for i in range(5):

            if random.randint(1, 2) == 1:
                
                a = random.randint(1, 12)
                b = random.randint(1, 12)
                
                guess = int(input(f"{a} * {b} = "))
                answer = a * b

            else:
                a = random.randint(1, 5)
                b = a * random.randint(1, 5)
                guess = int(input(f"{b} ÷ {a} = "))
                answer = float(b/a)
                
            if float(guess) == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The answer was {answer}.")

        print(f"\nYour final score: {score}/5")
        break

    elif dif == "3":
        

        for i in range(5):
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            

            if random.randint(1, 4) == 1:
                guess = int(input(f"{a} + {b} = "))
                answer = a + b
            elif random.randint(1, 4) == 2:
                guess = int(input(f"{a} - {b} = "))
                answer = a - b
            elif random.randint(1, 4) == 2:
                guess = int(input(f"{a} * {b} = "))
                answer = a * b
            else:
                a = random.randint(1, 5)
                b = a * random.randint(1, 5)
                
                guess = int(input(f"{b} ÷ {a} = "))
                answer = float(b/a)
                
            if guess == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The answer was {answer}.")
                
        print(f"\nYour final score: {score}/5")
        break
    
    else:
        print("please select a valid option.\n\tOr...\n\t\tThe Hookster might get you...")


