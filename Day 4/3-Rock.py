rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock,paper,scissors]
choose = int(input("What do you choose? Tybe 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if choose >= 3 or choose <0:
    print ("You typed an invalid number, you lose!")
else:
    print(game_images[choose])
    computer_c = random.randint(0,2)
    print("Computer Choose: ")
    print(game_images[computer_c])

    if choose ==0 and computer_c == 2:
        print("You Wins!")
    elif choose ==2 and computer_c == 0:
        print("You Loss")
    elif computer_c > choose:
        print (f" You Loss")
    elif choose > computer_c:
        print ("You Win!!")    
    elif computer_c == choose:
        print ("It's a Draw")