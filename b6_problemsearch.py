'''
reference:
    Dr. Marie A. Roch - CS 550
    Based on Russell, S. J., and Norvig, P. (2010). Artificial intelligence : 
        a modern approach (Prentice Hall, Upper Saddle River), pp. xviii, 1132 p.
    Contains contributions from multiple authors

Date            Name            Description
05/22/2024      Tom Nguyen      initial create
'''

from b3_searchrep import (Node, print_nodes)
from b4_queues import PriorityQueue 
from explored import Explored
import time
        
def graph_search(problem, player_sign, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """
        
    number_of_nodes_explored=0
    if verbose == True:
        solution_in_moves=0
        #print_nodes(problem)
    root_node = Node(problem=problem, state=problem.initial)
    f = Node.get_f
    front_list = PriorityQueue(f=f)#the 
    front_list.append(root_node)
#    print('frontier: ',front_list)#frontier:  <basicsearch_lib02.queues.PriorityQueue object at 0x0000000002718C88>
    explored_list = Explored()
    #print('explore list: ',explored_list)#explore list:  <explored.Explored object at 0x0000000002751208>
    explored_list.add(root_node.state)#add root to the explored list

  #  print('root_node: ',root_node)#root_node:  f=0.0 (g=0.0 + h=0.0) \n tileboard(n)
 #   print('frontier: ',front_list) #frontier:  <basicsearch_lib02.queues.PriorityQueue object at 0x0000000002735E80>
  #  print('root_node.state: ',root_node.state)#tileboard(n)
    solution_found = False
    while not solution_found:
   # for d in range(3):
        number_of_nodes_explored = number_of_nodes_explored +1

        
        parent_node = front_list.pop()#exploring this frontier. Pop of the first node
   
       # print('parent_node: ',parent_node)#parent_node:  f=15.0 (g=15.0 + h=0.0) \n tileboard(n)

        if parent_node.state.solved():#if it is solve exit.
            if debug == True:
                print('number of steps to solve: ',len(parent_node.solution()))
                #print (parent_node.solution())#[[0, 1], [1, 0], [1, 0], [0, -1], [-1, 0], [-1, 0], [0, 1], [0, 1], [1, 0], [1, 0], [0, -1], [-1, 0]]
                
            solution_in_moves=len(parent_node.solution())#return how many moves did it take to solve the puzzle
            solution_found = True
        else:
            children_node = parent_node.expand(problem = problem)#expanding the parent edges.
           # print('children node: ', children_node)#children node:  [f=-1792.0 (g=-1792.0 + h=0.0) \n tileboard(b)]
      #      print('children.node.__len__(): ',children_node.__len__())#children.node.__len__():  4
            i=0
            while i < children_node.__len__():#how many edges are there?
                i = i +1

                if  explored_list.exists(children_node[i-1].state):#this node is already on the explored list move on
                    continue
                front_list.append(children_node[i-1])#new nodes are found at this level. add it to the frontier list
                explored_list.add(children_node[i-1].state)#add to explore list as a record of what we have explored
               # print('children_node[{}]: '.format(i-1),children_node[i-1].state)#left, up, right, down: tileboard(n)

    if debug == True:
        print('number of nodes explored: {}'.format(number_of_nodes_explored))
    if verbose ==True:
        if solution_found != True:
            print('no solution found')
        else:
            print('Solution in {} moves'.format(solution_in_moves))
            print('Initial State')
            print(problem.initial)
            new_node = problem.initial
            counter = 0
            while counter < solution_in_moves:
                counter = counter + 1
                print('Move {} - {}'.format(counter,parent_node.solution()[counter-1]))
                new_node = new_node.move(parent_node.solution()[counter-1], player_sign)
                print(new_node)
    
    list_numbers=[]
    list_numbers.append(number_of_nodes_explored) 
    list_numbers.append(solution_in_moves)   
    for item in range(solution_in_moves-1,-1,-1):
        list_numbers.append(parent_node.solution()[item])
    # print('list_numbers: ',list_numbers) # list_numbers:  [51, 3, [2, 1], [1, 1], [0, 1]]
    return list_numbers
    
 #   raise NotImplemented
