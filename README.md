# catanDice

This program will simulate **probabilistically even rolls** for a pair of dice, with the intended use for the board game *Settlers of Catan*.

This means that in every 36 rolls there will be exactly six 7s, five 8s and 6s, four 5s and 9s, three 4s and 10s, two 3s and 11s, and one 2 and 12. Of course, the order in which these appear in the game is still random and unpredictable, but *over time* the rolls will be unbiased. With regular die rolls it is possible to have very unbalanced games, where some likely numbers (8s, 5s...) are rarely thrown, and unlikely numbers (3s, 12s...) come up frequently. This script reduces the chance of that happening.

## So how does it work?
Every possible combination of two dice is put into an array. It looks like this:

[2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 11, 7, 8, 9, 10, 11, 12]

When **Enter** is pressed, a random number is removed from this list and presented as the dice roll for that turn. When the list is empty, it is repopulated as above and the process continues. This ensures that every number appears exactly the expected number of times in every 36 turns of the game. Naturally the average game does not last an exact multiple of 36 turns, so there is still an element of randomness, but it removes the possibility of a disproportionate occurrence of any one number.

## Problems with the current solution
While complication has been added to prevent abuse of occurrence counting every 36 turns, this only offsets the predictability. The program resorts to cycles of 36 after 72 turns, so players intent on counting could attempt to use this to their advantage. However, this seems unlikely to happen.

## Todo list
- No improvements scheduled

## Update log
**[14/04/2022] Functionality update**
- Removed turn counter information due to possible advantages
- Implemented staggered roll list formation: starting list of all possibilities is split in two, with **(n-x)** pairs used at the start and **x** pairs re-inserted after a complete cycle has been performed, to make it useless to count the rolls
- Added whitespace to hide previous rolls, imitating real dice rolls where old throws annot be seen unless remembered

**[13/04/2022] Visual update**
- Updated array to store pairs of numbers rather than sums, to allow for dice images
- Added dice face images for easier recognition on smaller screens
- Added turn counter so players know how far through the game they are
