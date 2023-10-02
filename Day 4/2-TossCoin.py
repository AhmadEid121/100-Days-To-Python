import random
coin = ["Heads","Tails"]
toss = random.choice(coin)
selection = input("Heads or Tails: ")
if selection == toss:
    print (f" {toss} Correct!")
    print('''  .-------.
 /         \
|           |
|    o o    |
|           |
 \         /
  '-------' ''')
else:
    print(f"{toss} Wrong!")
    
