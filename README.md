# cse210-02
HiLow Game

In this game, you guess whether the next card will be higher or lower than the last card. You start with 300 points and get 100 if you're correct but lose 75 if you're incorrect. You lose when you reach 0 points.

Start the game from the __main__ file
type h or l to guess higher or lower
type y or n to say whether you want to continue guessing or not

Design:
main - starts the game
dealer - behaviors: start a game, get input from user, calculate new score, displays card dealt and the new score
         attributes: card dealt, last card dealt, score, total score, boolean of whether you're still playing or not
card - behaviors: flip to show numerical value
       attributes: value on card
