# Zuizz Saeed
# zuizzms@bu.edu
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

class Player:
    """represent a player of the Connect Four game.
    """
    def __init__(self, checker):
        """
        constructs a new Player object by initializing:
        - an attribute checker – a one-character string that represents the
        gamepiece for the player
        - an attribute num_moves – an integer that stores how many moves the
        player has made so far.
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """
        returns a string representing a Player object. The string returned
        should indicate which checker the Player object is using.
        """
        s = 'Player ' + str(self.checker)
        return s
    
    def opponent_checker(self):
        """
        returns a one-character string representing the checker of the Player
        object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        return 'X'
    
    def next_move(self, b):
        """
        accepts a Board object b as a parameter and returns the column where
        the player wants to make the next move
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col):
                return col
            else:
                print("Try again!")
        
        
        
        
        
        
        
        
        

