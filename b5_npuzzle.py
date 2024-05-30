'''
Name: Tom Nguyen

date: 05/22/2024
method breakdown:
    1. actions
        find a set of actions applicable to specified state
    2. result
        apply action to state and return new state
    3. goal_test
        Is state a goal?
    4. make_goal
        creates a matrix size x size
        placing none in the middle of the matrix
        if there is no middle of the matrix place it a the end
        example: size = 3
            [[1, 2, 3], [4, None, 5], [6, 7, 8]]
        example: size = 4
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
'''

from b2_tileboard import TileBoard
from b3_searchrep import Problem
import math
import b7_generate_all_wins

class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """
    def __init__(self, n, player_signs, board,force_state=None, **kwargs):
        """"__init__(n, force_state, **kwargs)
        
        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.
        
        The parent's class constructor is then called with the TileBoard
        instance any any remaining arguments captured in **kwargs.
        """
        
        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments 
        # into a dictionary.  The dictionary can be accessed like any other 
        # dictionary, e.g. kwargs["keyname"], or passed to another function 
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).

        #raise NotImplemented
        # goal_state = self.make_goal(int(math.sqrt(n+1)))
       # print('goal_state ',goal_state)
        self.player_sign = player_signs
        goal_state = self.make_goal(n, player_signs, state=board)

        # goal_state = [[1,3,5],[4,2,None],[6,7,8]]

        if force_state == None:
            puzzle = TileBoard(n)
        else:
            puzzle = TileBoard(n,force_state=force_state)
#        print(puzzle)
        super (NPuzzle,self).__init__(initial=puzzle,goals=goal_state,**kwargs)          
            
    def actions(self, state):
        "actions(state) - find a set of actions applicable to specified state"
        return state.get_actions()
        raise NotImplemented
    
    def result(self, state, action):
        "result(state, action)- apply action to state and return new state"
        if action not in self.actions(state):
            raise ValueError ('%d is not a legal action' %action)

        return state.move(action, self.player_sign)
        raise NotImplemented
    
    def goal_test(self, state):
        "goal_test(state) - Is state a goal?"
        # print(state.state_tuple())
        print(tuple([item for sublist in self.goals for item in sublist]))
        return state.state_tuple() == tuple([item for sublist in self.goals for item in sublist])
        raise NotImplemented

    def make_goal(self,size: int, player_sign, state=None) -> list:       
        """
        creates a matrix size x size
        placing none in the middle of the matrix
        if there is no middle of the matrix place it a the end
        example: size = 3
            [[1, 2, 3], [4, None, 5], [6, 7, 8]]
        example: size = 4
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
        """
        
        self.size =size
        self.list=[]
        list_row=[]

        if state:
            all_possible_wins = b7_generate_all_wins.generate_all_possible_wins()
            try:
                look_for_index = all_possible_wins.index(state)
                self.list = all_possible_wins[look_for_index]
            except ValueError: #E solution is not in the list
                for sublist in state:
                    for item in sublist:
                        if item == 0 :
                            state[state.index(sublist)][sublist.index(item)] = player_sign
                        elif item == None:
                            state[state.index(sublist)][sublist.index(item)] = player_sign
                try:
                    look_for_index = all_possible_wins.index(state)
                    self.list = all_possible_wins[look_for_index]
                except:
                    return []
        else:
            self.list=[
                [[player_sign,player_sign,player_sign],[player_sign,player_sign,player_sign],[player_sign,player_sign,player_sign]],
            ]
        # print('b5_goal_state ',self.list)
        return self.list
        



