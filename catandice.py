import random

print("""
          Welcome to CatanDice! This program simulates die rolls so you don't have to!
          All the possible rolls are shuffled into a deck with the right probabilities.
                Just press Enter when it's your turn to roll, and a random one is
          selected from the deck. Once all the possibilities are used up, the deck is
        remade and you can continue playing, safe in the knowledge that every roll will
       turn up exactly the number of times you want it to within 36 turns. Happy settling!
                              Type 'quit' to exit gracefully.
""")

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

diceArrangement = 1

def populateArrayWithPairs():
  arr = []
  for i in range(1,7):
    for j in range(1,7):
      arr.append([i,j])
  return arr

def moveRandomPairs(oldArray:list, newArray:list):
  """Move a random number of items from oldArray to newArray
  
  oldArray must have more than 10 members"""
  assert(oldArray.__len__() > 10), "moveRandomPairs - oldArray must have more than 10 members"

  numberToMove = random.choice(range(5, oldArray.__len__()-5))

  while numberToMove:
    choice = random.choice(oldArray)
    oldArray.remove(choice)
    newArray.append(choice)
    numberToMove -= 1


def printDiceImage(die1, die2):
  global diceArrangement
  if (diceArrangement == 1):
    # Print dice in line
    print("\n   =======     ======= ")
    print("  " + diceImages[die1-1][0] + "   " + diceImages[die2-1][0])
    print("  " + diceImages[die1-1][1] + "   " + diceImages[die2-1][1])
    print("  " + diceImages[die1-1][2] + "   " + diceImages[die2-1][2])
    print("   =======     ======= \n")
    diceArrangement = 2

  elif (diceArrangement == 2):
    # Print left die higher
    print("\n  =======")
    print(" " + diceImages[die1-1][0])
    print(" " + diceImages[die1-1][1] + "     =======")
    print(" " + diceImages[die1-1][2] + "    " + diceImages[die2-1][0])
    print("  =======     " + diceImages[die2-1][1])
    print("              " + diceImages[die2-1][2])
    print("               ======= \n")
    diceArrangement = 3

  elif (diceArrangement == 3):
    # Print right die higher
    print("\n                =======")
    print("    =======    " + diceImages[die2-1][0])
    print("   " + diceImages[die1-1][0] + "   " + diceImages[die2-1][1])
    print("   " + diceImages[die1-1][1] + "   " + diceImages[die2-1][2])
    print("   " + diceImages[die1-1][2] + "    =======")
    print("    ======= \n")
    diceArrangement = 1


def rollDicePair(dicePairArray):
  choice = random.choice(dicePairArray)
  sum = choice[0] + choice[1]

  printDiceImage(choice[0], choice[1])

  # Determine the correct determiner ('a' or 'an')
  if (sum == 8 or sum == 11):
    determiner = "an"
  else:
    determiner = "a"

  print("You rolled " + determiner + " " + str(sum) + "\n")
  dicePairArray.remove(choice)


# Program start
startingExtraRolls = populateArrayWithPairs()
startingRemovedRolls = []
moveRandomPairs(startingExtraRolls, startingRemovedRolls)

remainingDieRolls = populateArrayWithPairs()
#print(remainingDieRolls)

while input("Press Enter to roll the dice...") != "quit":
  print("\n"*30)

  if (startingExtraRolls):
    # Working our way through the extra starting set of N rolls
    rollDicePair(startingExtraRolls)

  elif (startingRemovedRolls and remainingDieRolls):
    # One regular cycle of 36 rolls after the starting set
    rollDicePair(remainingDieRolls)

  elif (startingRemovedRolls and not remainingDieRolls):
    # Re-insert the removed rolls from the starting set after the 1+N cycles
    rollDicePair(startingRemovedRolls)

  elif (remainingDieRolls):
    # After 72 turns the rolls return to normal sets of 36
    rollDicePair(remainingDieRolls)

  else:
    # Reshuffle the deck and roll as normal
    remainingDieRolls = populateArrayWithPairs()
    rollDicePair(remainingDieRolls)
