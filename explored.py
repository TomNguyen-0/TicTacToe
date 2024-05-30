'''
reference:
    Dr. Marie A. Roch - CS 550

Date            Name            Description
05/26/2024      Tom Nguyen      initial create
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        self.explore_table = dict()
        # print("self.explore_table: ", self.explore_table)
        self.explore_tuple = ()
        # print("self.explore_tuple: ", self.explore_tuple)
        
    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError
        hash_value = hash(state)
        try:
            hash_table = self.explore_table[hash_value]
            hash_table.append(state)
        except KeyError:#do this when the hash of state is not in the dictionary
            new_state = [state]#turning state into a list
            self.explore_table[hash_value] = new_state#when the state has not been explore yet. set state to this hash value
     
          
    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        hash_value = hash(state)
        flag_already_explored = False
       # print(state.state_tuple())#(5, 2, 3, 7, 8, None, 6, 1, 4)
        if state.state_tuple() == self.explore_tuple:#from tileboard.state_tuple() 
            raise("state and explore states are the same")
   #     print('state: ',state) #print tileboard(size)
   #     print('hash(state) :',hash_value) #hash(state) : -3913242927317608944
        try:
            #print('self.explore_table[hash_value]',self.explore_table[hash_value]) #self.explore_table[hash_value] [      0        1        2  tileboard(n)
            hash_list = self.explore_table[hash_value]
            for i in hash_list:
                #print('item: ',item)    #item:        0        1        2  
                if i == state:#we have explored this node already
                    flag_already_explored = True
                    break
        except KeyError:
            return flag_already_explored
        finally:
            return  flag_already_explored
    
    # def __repr__(self) -> str:
    #     print('self.explore_table: ',self.explore_table)
    #     print('self.explore_tuple: ',self.explore_tuple)
    #     return 'explored.Explored object'
            
