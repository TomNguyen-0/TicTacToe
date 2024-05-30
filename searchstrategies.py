
"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles of an odd length
    with solutions that contain the blank in the middle and numbers going
    from left to right in each row, e.g.:
        123
        4 5
        678
    When mulitple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 

reference:
    Dr. Marie A. Roch - CS 550

05/22/2024      Tom Nguyen      initial create
"""

import math

# For each of the following classes, create classmethods g and h
# with the following signatures
#       @classmethod
#       def g(cls, parentnode, action, childnode):
#               return appropritate g value
#       @classmethod
#        def h(cls, state):
#               return appropriate h value
 

class BreadthFirst:
    "BredthFirst - breadthfirst search"
    @classmethod
    #using a prioirty queue we will pop off the lowest f value.
    # as the list grows it will start to look: 1,2,3.
    #it will continue to pop off all the queue in depth 1 before moving to depth 2.
    def g(cls, parentnode, action, childnode):#up to the childnode
    #    print('parentnode: ',parentnode)#parentnode:  f=0.0 (g=0.0 + h=0.0) \n tileboard(n)
    #    print('action: ',action)#action:  [1, 0]
    #    print('childnode.depth: ',childnode.depth)#childnode.depth:  1
       return childnode.depth
    @classmethod
    def h(cls,state):
        return 0
    #pass

class DepthFirst:
    "DepthFirst - depth first search"
    @classmethod
    #this works because in the priority queue we will pop the lowest f value off first.
    #so as the list grows example: -1, -2, -3. the later one will always be popped off first.
    def g(cls,parentnode,action,childnode):#
        #print('childnode.depth: ',-childnode.depth)#childnode.depth:  -1 # the child depth is stored in from parent.depth
        return (-childnode.depth) #start from the lowest level first
    
    @classmethod
    def h(cls, state):
        return 0
    #pass
        
class Manhattan:
    "Manhattan Block Distance heuristic"
    @classmethod
    def g(cls,parentnode,action,childnode):
        #print('g: ',parentnode.depth)
        return parentnode.depth
    @classmethod
    def h(cls,state):
        #print('state of h board: ',state.board)#state of h board:  [[1, 3, 5], [4, 2, None], [6, 7, 8]]
        distance = 0
        self=cls()
        goal_list=self.make_goal(state.boardsize)
        #print('goal_list ', goal_list)#goal_list  [[1, 2, 3], [4, None, 5], [6, 7, 8]]
        #print('goal_list len',len(goal_list))#goal_list len 3
        len_of_puzzle = len(goal_list)**2
        counter_for_tile=0
        if len(goal_list)%2==0:#even 
            none_is_located_here = len_of_puzzle-1
        else: #odd puzzle size odd by odd puzzle board.
            none_is_located_here = math.floor(len_of_puzzle/2) 
        for row in range(state.boardsize):
            for column in range(state.boardsize):
                value_of_state = state.board[row][column]
                counter_for_tile = counter_for_tile + 1
                tile_goal_state = goal_list[row][column]
                if goal_list[row][column] is None:
                    tile_goal_state = none_is_located_here+.5
                if value_of_state is None:
                    value_of_state = none_is_located_here+.5
                distance = distance + abs(value_of_state-tile_goal_state)

        #print ('h :', distance)
        return distance
    
    def make_goal(self,size):       
        self.size =size
        self.list=[]
        list_row=[]
        number_to_add_to_list=0
        if size%2 ==0: #even rows. the None is at the end of the list. not a good use for even numbers
            for i in range(size):
                for j in range(size):
                    number_to_add_to_list = number_to_add_to_list +1
                    list_row.append(number_to_add_to_list)
                self.list.append(list_row)
                list_row=[]
            self.list[size-1][size-1]=None
        else:       #odd rows
            middle = int(size/2)
            for i in range(size):
                if(i!=middle):
                    for j in range(size):
                        number_to_add_to_list = number_to_add_to_list +1
                        list_row.append(number_to_add_to_list)
                    self.list.append(list_row)
                    list_row=[]
                else:
                    for j in range(size):
                        if(j==middle):#we found the middle tile
                            list_row.append(None)
                            continue
                        number_to_add_to_list = number_to_add_to_list +1
                        list_row.append(number_to_add_to_list)
                    self.list.append(list_row)
                    list_row=[]
        return self.list          
       
