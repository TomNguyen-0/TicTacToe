'''
reference:
    Dr. Marie A. Roch - CS 550

05/22/2024      Tom Nguyen      initial create

method breakdown:
    1. state_tuple
        takes the board and converts it to a tuple
    2. get_actions
        returns the possible moves
    3. move
        move the pieces changing the board
    4. solved
        return true or false if the board is solved


'''
import random
import copy
import math

from b1_board import Board
import b7_generate_all_wins


class TileBoard(Board):
    def __init__(self, n, multiple_solutions=False, force_state=None):
        """"tileboard(n, multiple_solutions
        Create a tile board for an n puzzle.
        If multipleSolutions are true, the solution need not
        have the space in the center.
        
        force_state can be used to initialize an n puzzle to a desired
        configuration.  No error checking is done.  It is specified as
        a list with n+1 elements in it, 1:n and None in the desired order.
        """
        self.boardsize = int(math.sqrt(n+1))  
        if math.sqrt(n+1) != self.boardsize:
            raise ValueError("Bad board size\n" +
                "Must be one less than an odd perfect square 8, 24, ...")
            
        # Does the space have to be in the center (False)
        # or are multiple solutions allowed.
        self.multiple_solutions = multiple_solutions
        
        if force_state:
            tiles = force_state
        else:
            # Build initial state - all in order
            tiles = [val+1 for val in range(n)]
            tiles.append(None)
            # Verify problem is solvable
            solvable = False
            while not solvable:
                random.shuffle(tiles)  # mix up tiles
                # Compute inversion order
                # defined as:
                # for each number in the list of tiles,
                #    How many following numbers are less than that one
                #    e.g. [13, 10, 11, 6, 5, 7, 4, 8, 1, 12, 14, 9, 3, 15, 2, None]
                #    Tiles following 9:  [3, 15, 2, None]
                #    Two of these are smaller than 9, so the inversion order
                #        for 9 is 2
                # A puzzle's inversion order is the sum of the tiles inversion
                # orders.  For puzzles with even numbers of rows and columns,
                # the row number on which the blank resides must be added.  
                # Note that we need not worry about 1 as there are
                # no tiles smaller than one.  
                # 
                # See Wolfram Mathworld for further explanation:
                #     http://mathworld.wolfram.com/15Puzzle.html
                # and http://www.cut-the-knot.org/pythagoras/fifteen.shtml
                #
                # This lets us know if a problem can be solved.  The inversion
                # order modulo 2 is invariant across moves.  The solution state
                # has an even inversion order, so any puzzle with an odd inversion
                # number cannot be solved.
                inversionorder = 0
                for value in range(2,len(tiles)):
                    idx = tiles.index(value)
                    try:
                        after = tiles[idx+1:]  # Remaining tiles
                    except IndexError:
                        after = []  # nothing remaining
                    numtiles = len([x for x in after if x != None and x < value])
                    inversionorder = inversionorder + numtiles
                # Account for blank.
                if self.boardsize % 2 == 0:
                    inversionorder = inversionorder + \
                        math.floor(tiles.index(None) / self.boardsize)+1
                # Problem is solvable if inversion order even.
                solvable = inversionorder % 2 == 0
        
        # initialize the board
        super(TileBoard, self).__init__(self.boardsize, self.boardsize)
        # populate it
        for r in range(self.boardsize):
            for c in range(self.boardsize):
                tile = tiles[r*self.boardsize + c]  # next tile
                if tile:                    
                    self.place(r, c, tile)
                else:
                    # keep track of empty tile
                    self.empty = (r, c)
                    
    def __hash__(self):
        "__hash__ - Hash the board state"
        
        # Convert state to a tuple and hash
        return hash(self.state_tuple())
    
    def __eq__(self, other):
        "__eq__ - Check if objects equal:  a == b"
        
        # Set pairs to be equal to another
        equal = True  # until we found out otherwise
        # pair up board items in tuples and compare them
        for (mystate, otherstate) in zip(self.state_tuple(), other.state_tuple()):
            equal = mystate == otherstate
            if not equal:
                break
        return equal
    
    def state_tuple(self):
        "state_tuple - Return board state as a single tuple"
        
        # Iterate over the items in each list, merging them
        flattened = [item for sublist in self.board
                            for item in sublist]
        # convert to tuple (hashable) and return 
        return(tuple(flattened))
    
    def get_actions(self):
        "Return row column offsets of where the empty tile can be moved"
        
        actions = []
        # check row and column, no diagonal moves allowed
        return [[index_sublist, index] for index_sublist,sublist in enumerate(self.board) for index,item in enumerate(sublist) if item == None]
    
            
    def move(self, offset, player_sign):
        "move - Move the empty space by [delta_row, delta_col] and return new board"
        
        # Current row and column of empty space
     
        
        [delta_r, delta_c] = offset


        # Make a copy of the board so that mutating it does not 
        # modify other copies of the board.  Not the most efficient
        # way to do this, but it will get the job done.
        newboard = copy.deepcopy(self)
        # Slide a tile into the empty slot position
        newboard.place(delta_r, delta_c, player_sign)
        # update empty position

 
        
        return newboard
        
    #def __repr__(self):
    #    """Alternate board representation - as state tuple
    #       Useful for verifying that solutions do not have duplicate
    #       states in path."""
    #    return str(self.state_tuple())
    
    def solved(self):
        "solved - Is the puzzle solved?"
        current_board = copy.deepcopy(self.board)
        for sublist in current_board:
            for item in sublist:
                if item == None:
                    current_board[current_board.index(sublist)][sublist.index(item)] = 0
        if b7_generate_all_wins.is_solved(current_board) > 0:
            solved = True
        else:
            solved = False
                    
        return solved