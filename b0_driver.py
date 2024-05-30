"""
Date            Name            Description
05/22/2024      Tom Nguyen      initial create
"""
from b1_board import Board
from b2_tileboard import TileBoard
from b5_npuzzle import NPuzzle
from searchstrategies import (BreadthFirst)
from b6_problemsearch import graph_search
import b7_generate_all_wins
import random
from copy import deepcopy 
import streamlit as st

def driver(board: "2D list", i:int, j:int):

    ## create the board
    convert_board_to_tuple = [item for sublist in board for item in sublist]
    convert_board_to_tuple = tuple(convert_board_to_tuple)
    tile_board = TileBoard(8, force_state=convert_board_to_tuple)

    if i == 9 and j == 9:
        ## ai is going first      
        ai_copy_board = deepcopy(tile_board)
        ai_setup = NPuzzle(8, player_signs=2, board=ai_copy_board.board, 
                        g=BreadthFirst.g, h=BreadthFirst.h, force_state=ai_copy_board.state_tuple())
        ai = graph_search(ai_setup, player_sign=2)
        ai = ai[2:]
        valid_move = False
        while not valid_move:
            random_choice = random.choice(ai)
            if random_choice in tile_board.get_actions():
                valid_move = True
        st.session_state.board[random_choice[0]][random_choice[1]] = 'O'
        tile_board.place(random_choice[0], random_choice[1], 2)
        ai.remove(random_choice)
        st.session_state.ai_decision = ai
        return tile_board
    else:
    ## crate the movement space
        movement = [i, j]

    ## check if the move is valid
    ## if it is valid then have AI move -> [0,0]
    ## else do nothing   


    ## the player is always 'X'
        tile_board.place(movement[0], movement[1], 1)
    ## check if the player won
        if tile_board.solved():
            b7_generate_all_wins.is_solved(tile_board.board)
        else:
            ai_copy_board = deepcopy(tile_board)
            ai_setup = NPuzzle(8, player_signs=2, board=ai_copy_board.board, 
                            g=BreadthFirst.g, h=BreadthFirst.h, force_state=ai_copy_board.state_tuple())
            try: # no possible moves to win
                ai = graph_search(ai_setup, player_sign=2, 
                                verbose=False,
                                debug=False)
                ai = ai[2:]
            except:
                # st.write(tile_board.get_actions())
                ai = tile_board.get_actions()

            valid_move = False
            while not valid_move:
                random_choice = random.choice(ai)
                if random_choice in tile_board.get_actions():
                    valid_move = True
            st.session_state.board[random_choice[0]][random_choice[1]] = 'O'
            tile_board.place(random_choice[0], random_choice[1], 2)
            ai.remove(random_choice)
            st.session_state.ai_decision = ai
            return tile_board
        # st.write(tuple(ai))
    ## get the moves from user
    