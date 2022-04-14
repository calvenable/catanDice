import random

print("\n   Welcome to CatanDice! This program simulates die rolls so you don't have to!")
print("   All the possible rolls are shuffled into a deck with the right probabilities.")
print("  All you have to do is press Enter when you want a new roll, and a random one is")
print("    selected from the deck. Once all the possibilities are used up, the deck is")
print("  remade and you can continue playing, safe in the knowledge that every roll will")
print("turn up exactly the number of times you want it to within 36 turns. Happy settling!")
print("                       Type 'quit' to exit gracefully.\n")

# •, ⦾, and ⦿ are possibilities but not ASCII/Terminal friendly

diceImages = [
  [
    "|       |",
    "|   O   |",
    "|       |"
  ],
  [
    "| O     |",
    "|       |",
    "|     O |"
  ],
  [
    "|     O |",
    "|   O   |",
    "| O     |"
  ],
  [
    "| O   O |",
    "|       |",
    "| O   O |"
  ],
  [
    "| O   O |",
    "|   O   |",
    "| O   O |"
  ],
  [
    "| O   O |",
    "| O   O |",
    "| O   O |"
  ]
]

turnCounter = 1

def populateArrayWithPairs():
  arr = []
  for i in range(1,7):
    for j in range(1,7):
      arr.append([i,j])
  return arr

def populateArray():
  arr = []
  for i in range(1,7):
    for j in range(1,7):
      arr.append(i+j)
  return arr

def printDiceImage(die1, die2):
  print("\n   =======     ======= ")
  print("  " + diceImages[die1-1][0] + "   " + diceImages[die2-1][0])
  print("  " + diceImages[die1-1][1] + "   " + diceImages[die2-1][1])
  print("  " + diceImages[die1-1][2] + "   " + diceImages[die2-1][2])
  print("   =======     ======= \n")

def rollDicePair(dicePairArray):
  choice = random.choice(dicePairArray)
  sum = choice[0] + choice[1]

  printDiceImage(choice[0], choice[1])

  # Determine the correct determiner ('a' or 'an')
  if (sum == 8 or sum == 11):
    determiner = "an"
  else:
    determiner = "a"

  if turnCounter < 37:
    # Just print turnCounter
    print("[" + str(turnCounter) + "] You rolled " + determiner + " " + str(sum) + "\n")
  else:
    # Print turnCounter and current deck progress
    print("[" + str(turnCounter) + "/"+ str(37-dicePairArray.__len__()) + "] You rolled " + determiner + " " + str(sum) + "\n")
  dicePairArray.remove(choice)

def rollDice(diceArray):
  choice = random.choice(diceArray)
  print("You rolled: " + str(choice) + "\n")
  diceArray.remove(choice)



# Program start
remainingDieRolls = populateArrayWithPairs()
#print(remainingDieRolls)

while input("Press Enter to roll the dice...") != "quit":

  if (remainingDieRolls.__len__() > 0):
    # Regular roll
    rollDicePair(remainingDieRolls)

  else:
    # Reshuffle deck and roll
    print("Reshuffling the deck...")
    remainingDieRolls = populateArrayWithPairs()
    rollDicePair(remainingDieRolls)
  
  turnCounter += 1