# MINI PROJECT [QUIZ GAME]

print("Welcome to my computer quiz")
playing=input("Do you wnat to play ?")
if playing.lower()!="yes":
    quit()

print("Okay! Let's Play :")
score=0

answer=input("What does CPU stands for ?")
if answer.lower()=="central processing unit":
    print("CORRECT!  Well Done")
    score+=1
else:
    print("INCORRECT  Better Luck Next Time")
    print("Correct answer is Central Processing Unit")

answer=input("What does GPU stands for ?")
if answer.lower()=="graphics processing unit":
    print("CORRECT! Hurray")
    score+=1
else:
    print("INCORRECT  Sorry! Try Again")
    print("Correct answer is Graphics Processing Unit")

anwer=input("Which is the hottest planet in our solar system ?")
if answer.lower()=="venus":
    print("CORRECT! WOW")
    score+=1
else:
    print("INCORRECT Try Next!")
    print("Correct answer is Venus.")
    
answer=input("What does PSU stands for ?")
if answer.lower()=="power supply":
    print("CORRECT! Nice")
    score+=1
else:
    print("INCORRECT  Ohh No!")
    print("Correct answer is Power Supply")

answer=input("What does UPI stands for ?")
if answer.lower()=="unified payments interface":
    print("CORRECT! Nice")
    score+=1
else:
    print("INCORRECT  You Loss!")
    print("Correct answer is Unified Payments Interface ")

answer=input("Who is the richest person in the world ?")
if answer.lower()=="alon musk":
    print("CORRECT! Well Played")
    score+=1
else:
    print("INCORRECT Qiuz Over!")
    print("Correct answer is Alon Musk")

print("You Got" + " "+ str(score) +" " + "Questions Correct!")
print("You Got" + " "+ str((score/6)*100) + "%")


    
