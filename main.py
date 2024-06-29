print("Welcome To the Python Quiz Game")

name = input("Please Enter your name : ")


playing = input(f"{name} Do You Want to play the Awesome Quiz Game? ")

score = 0


if (playing.lower() != "yes"):
  quit()

print(f"Ok {name} Lets Play The Game :) ")  
    
print("Your First Question---------")

answer = input("What is the capital city of Japan? ")

if(answer.lower() == "tokyo"):
    print("Hurray ! You are right")
    score+=1
else:
    print("So sad You are wrong :)")
    

print("Second Question---------")

answer = input("Who wrote “Romeo and Juliet”? ")

if(answer.lower() == "william shakespeare"):
    print("Hurray ! You are right")
    score+=1
    
else:
    print("So sad You are wrong :)")
    
print("Third Question---------")

answer = input("In which year did the Titanic sink? ")

if(answer.lower() == str(1912)):
    print("Hurray ! You are right")
    score+=1
    
else:
    print("So sad You are wrong :)")

print("Fourth Question---------")

answer = input("What is the largest planet in our solar system? ")

if(answer.lower() == "jupiter"):
    print("Hurray ! You are right")
    score+=1
    
else:
    print("So sad You are wrong :)")                    

print("Fifth Question---------")

answer = input("What is the currency of Australia? ")

if(answer.lower() == "australian dollar"):
    print("Hurray ! You are right")
    score+=1
    
else:
    print("So sad You are wrong :)")                        
    
print(f"{name} Your Score is {score} !")

if (score >2):
  print(f"Congratulations {name} You are Passed this Quiz")
else:
  print(f"Unfortunatly You are Fail Better Luck Next Time {name}")
    

 
    