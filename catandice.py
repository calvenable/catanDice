import random

print("\n   Welcome to CatanDice! This program simulates die rolls so you don't have to!")
print("   All the possible rolls are shuffled into a deck with the right probabilities.")
print("  All you have to do is press Enter when you want a new roll, and a random one is")
print("    selected from the deck. Once all the possibilities are used up, the deck is")
print("  remade and you can continue playing, safe in the knowledge that every roll will")
print("turn up exactly the number of times you want it to within 36 turns. Happy settling!")
print("                       Type 'quit' to exit gracefully.\n")



def populateArray():
  arr = []
  for i in range(1,7):
    for j in range(1,7):
      arr.append(i+j)
  return arr

def rollDice(diceArray):
  choice = random.choice(diceArray)
  print("You rolled: " + str(choice) + "\n")
  diceArray.remove(choice)

# Program start
remainingDieRolls = populateArray()
#print(remainingDieRolls)

while input("Press Enter to roll the dice...") != "quit":

  if (remainingDieRolls.__len__() > 0):
    # Regular roll
    rollDice(remainingDieRolls)

  else:
    # Reshuffle deck and roll
    print("Reshuffling the deck...")
    remainingDieRolls = populateArray()
    rollDice(remainingDieRolls)



