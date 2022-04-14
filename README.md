# catanDice

This program will simulate **probabilistically even rolls** for a pair of dice, with the intended use for the board game *Settlers of Catan*.

This means that in every 36 rolls there will be exactly six 7s, five 8s and 6s, four 5s and 9s, three 4s and 10s, two 3s and 11s, and one 2 and 12. Of course, the order in which these appear in the game is still random and unpredictable, but *over time* the rolls will be unbiased. With regular die rolls it is possible to have very unbalanced games, where some likely numbers (8s, 5s...) are rarely thrown, and unlikely numbers (3s, 12s...) come up frequently. This script reduces the chance of that happening.

## So how does it work?
Every possible combination of two dice is put into an array. It looks like this:

[2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 11, 7, 8, 9, 10, 11, 12]

When **Enter** is pressed, a random number is removed from this list and presented as the dice roll for that turn. When the list is empty, it is repopulated as above and the process continues. This ensures that every number appears exactly the expected number of times in every 36 turns of the game. Naturally the average game does not last an exact multiple of 36 turns, so there is still an element of randomness, but it removes the possibility of a disproportionate occurrence of any one number.

In order to avoid people making a note of how many rolls have occurred and using the set of 36 rolls to their advantage, the program starts the game at a random point in a cycle/set (making  a list of 36 combinations and removing some at random), so the point at which a new cycle starts is not determinable but the probabilities are still close to expected. The combinations that are removed are later replaced so the expected number of each roll after 72 is the same as if it had been two complete sets.

## Problems with the current solution
Some would argue that this goes against the fundamental idea of probability: with this program, when a 6 is rolled, the next roll is statistically less likely to be a 6. While this follows natural human inclination, it is not accurate to the laws of probability - with two real dice, after a 6, the next roll is still 5/36 likely to be a 6, regardless of previous rolls. However, the purpose of this program is to remove some of the bias in dice rolling which makes games like Catan so annoying in the long run, making this qualm a rather moot point. Those wishing for probabilistic integrity should continue using real dice!

While complication has been added to prevent abuse of occurrence counting every 36 turns, this only offsets the predictability. The program resorts to cycles of 36 after 72 turns, so players intent on counting could attempt to use this to their advantage. However, this seems unlikely to happen, especially since most games of Catan do not last more than 72 turns.

## Todo list
- No scheduled improvements

## Update log
**[15/04/2022] Visual update**
- Added indication of when dice are rolled since sequential, identical rolls were previously indistinguishable. Dice now appear in one of three hard-coded locations.

**[14/04/2022] Functionality update**
- Removed turn counter information due to possible advantages
- Implemented staggered roll list formation: starting list of all possibilities is split in two, with **(n-x)** pairs used at the start and **x** pairs re-inserted after a complete cycle has been performed, to make it useless to count the rolls
- Added whitespace to hide previous rolls, imitating real dice rolls where old throws annot be seen unless remembered

**[13/04/2022] Visual update**
- Updated array to store pairs of numbers rather than sums, to allow for dice images
- Added dice face images for easier recognition on smaller screens
- Added turn counter so players know how far through the game they are
