# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
    The most difficult of tic-tac-toe was getting started. I was not sure how I would start by constructing the board, but by asking AI, I realized that I was overcomplicating the task. Once I was able to construct the board and understand it as a list but displayed as a string broken up, it was a lot easier to understand how to manipulate different sections of the grid. Another difficulty I had was understanding how to use different variables in a function, such as "players" or "position". It was confusing to keep track of each variable and what they did. Some functions I had trouble writing, such as has_won. The win combinations were a little tedious to write, but I wouldn't have been able to complete the function if it weren't for this line of code that ChatGPT wrote: return any(all(self.board[i] == player for i in combo) for combo in wins).

2. Explain how you would add a computer player to the game.
    To add a computer to the game, I would make it so as the computer tracks which player is taking their turn, the computer would be a player and choose at random what space to go to out of the unoccupied spaces. I would also give the player an option to let the computer be X or O, and then have the code act accordingly.

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
    I would make a list of the best responses to each move in the game, or I could add a function which can analyze the position of the players on the board and then perform some mathmatical calculation in order to know what the best move is. That way, the computer can recognize patterns in different positions, cutting down on the need to code for every position since the computer still knows what to do. For example, a position that is rotated 90 degrees would still be the same. 