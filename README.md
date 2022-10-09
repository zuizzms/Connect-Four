# Connect-Four
Connect Four Game that can be played with two human players, one player vs. an AI player, or AI Player vs. AI player!


Connect Four is a variation of tic-tac-toe played on a 6x7 rectangular board:

![image](https://user-images.githubusercontent.com/50706134/194736547-94b81173-a448-440a-990b-5af3993e6fa9.png)


The game is played by two players, and the goal is to place four checkers in a row vertically, horizontally, or diagonally. The players alternate turns and add one checker to the board at a time. However, because the board stands vertically, a checker cannot be placed in an arbitrary position on the board. Rather, a checker must be inserted at the top of one of the columns, and it “drops down” as far as it can go – until it rests on top of the existing checkers in that column, or (if it is the first checker in that column) until it reaches the bottom row of the column.

HOW TO PLAY

To play with two human players, enter the following command:

connect_four(Player('X'), Player('O'))

To play against an "unintelligent" AI player, enter the following command:

connect_four(Player('X'), RandomPlayer('O'))

To play against an intelligent AI player, enter the following command (increasing the last parameter for the AIPlayer will make the AI player smarter - this value represents how many moves the AI looks ahead into when planning its move. A lower value will make the AI player less intelligent. For example, a lookahead of 5 will make the AI Player look at the next 5 possible moves in order to evaluate possible moves. Note that higher values may take more time to process):

connect_four(Player('X'), AIPlayer('O', 'RANDOM', 5))




