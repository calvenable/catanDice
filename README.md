# catanDice

This program will simulate probabilistically even rolls for a pair of dice, with the intended use for the board game *Settlers of Catan*.

This means that in every 36 rolls there will be exactly six 7s, five 8s and 6s, four 5s and 9s, three 4s and 10s, two 3s and 11s, and one 2 and 12. Of course, the order in which these appear in the game is still random and unpredictable, but *over time* the rolls will be unbiased. With regular die rolls it is possible to have very unbalanced games, where some likely numbers are rarely thrown, and unlikely numbers come up frequently. This script reduces the chance of that happening.

## So how does it work?
Every possible combination of two dice is put into an array. It looks like this:
[2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 11, 7, 8, 9, 10, 11, 12]
When **Enter** is pressed, a random number is removed from this list and presented as the dice roll for that turn. When the list is empty, it is repopulated as above and the process continues. This ensures that every number appears exactly the expected number of times in every 36 turns of the game. Naturally the average game does not last an exact multiple of 36 turns, so there is still an element of randomness, but it removes the possibility of a disproportionate occurrence of any one number.

## Problems with the current solution
It is possible to some degree to count the number of times each combination has been rolled, and an observant player could use this to their advantage. For example, if all four 9s have been pulled then a player may avoid putting the robber on a 9 until it becomes a possibility again. Similarly, if one player notices that after 30 turns there have been only two 8s, they may deliberately block another player's 8 production with the robber, or quickly build a settlement on an 8 hex.

This may be mitigated by starting with a list that has between 10 and 30 numbers *randomly removed*. If users do not know how many numbers are removed they will not be able to count and use this knowledge to their advantage. If the removed numbers are re-inserted later in the game, the probabilities would still even out provided the game lasts at least 72 turns.

## Todo list
- Add dice face images to make rolls clearer than a single number printed to the screen
- Implement starting list removal to reduce players' ability to game the cycles
