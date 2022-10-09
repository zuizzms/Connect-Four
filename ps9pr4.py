# Zuizz Saeed
# zuizzms@bu.edu
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """
    more “intelligent” computer player that will look ahead some number of moves
    into the future to assess the impact of each possible move that it could make
    for its next move, and it will assign a score to each possible move
    """
    def __init__(self, checker, tiebreak, lookahead):
        """
        constructs a new AIPlayer object with following attributes:
            - checker
            - tiebreak (string determining method of tiebreak decision
            - lookahead (integer for number of lookahead moves)
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """
        returns a string representing an AIPlayer object that also includes
        tiebreak method and lookeahead number
        """
        s = 'Player ' + str(self.checker) + ' (' + self.tiebreak + \
            ', ' + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        """
        takes a list scores containing a score for each column of the board, 
        and returns the index of the column with the maximum score (uses 
        given tiebreaking strategy if necessary)
        """
        maxscore = max(scores)
        maxList = []
        for i in range(len(scores)):
            if scores[i] == maxscore:
                maxList += [i]
        
        if self.tiebreak == 'LEFT':
            return maxList[0]
        if self.tiebreak == 'RIGHT':
            return maxList[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(maxList)
        
    def scores_for(self, b):
        """
        takes a Board object b and determines the called AIPlayer‘s scores 
        for the columns in b
        """
        scores = [0] * b.width
        for i in range(b.width):
            if not b.can_add_to(i):
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, \
                                    self.lookahead-1)
                oppScores = opponent.scores_for(b)
                if max(oppScores) == 100:
                    scores[i] = 0
                elif max(oppScores) == 0:
                    scores[i] = 100
                else:
                    scores[i] = 50
                b.remove_checker(i)
        return scores
    def next_move(self, b):
        """
        Rather than asking the user for the next move, this version of 
        next_move should return the called AIPlayer‘s judgment of its best 
        possible move.
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        