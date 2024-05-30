import streamlit as st
import b0_driver as ai
from copy import deepcopy
from b2_tileboard import TileBoard

def convert_session_board_to_tuple(board_for_ai=0):
    if board_for_ai==0:
        session_board = deepcopy(st.session_state.board)
    else:
        session_board = deepcopy(board_for_ai)
    for index_sublist,sublist in enumerate(session_board):
        for index,item in enumerate(sublist):
            if item == 'X':
                session_board[index_sublist][index] = 1
            elif item == 'O':
                session_board[index_sublist][index] = 2
            else:
                session_board[index_sublist][index] = 0
    flattened = [item for sublist in session_board
                            for item in sublist]
    return tuple(flattened)

def ai_move(convert_board_for_ai,i=9, j=9):
    convert_board_for_ai = deepcopy(convert_board_for_ai)
    check_board = ai.driver(convert_board_for_ai,i ,j)
    if check_board.solved():
        st.session_state.winner = "A.I. Wins!"

def on_button_click(i, j, player_sign):
   if st.session_state.winner != '':
         return "Someone won so do nothing"
   ## check if it is a valid move
   tile_board_validation = TileBoard(8, force_state=convert_session_board_to_tuple())
   if [i,j] in tile_board_validation.get_actions():
    ## player makes a move
    st.session_state.board[i][j] = player_sign
    convert_board_for_ai = deepcopy(st.session_state.board)
    for index_sublist,sublist in enumerate(convert_board_for_ai):
        for index,item in enumerate(sublist):
            if item == 'X':
                convert_board_for_ai[index_sublist][index] = 1
            elif item == 'O':
                convert_board_for_ai[index_sublist][index] = 2
            else:
                convert_board_for_ai[index_sublist][index] = 0
    ## check if the player won
    check_board_tuple = [item for sublist in convert_board_for_ai for item in sublist]
    check_board = TileBoard(8, force_state=tuple(check_board_tuple))


    if check_board.solved(): # player just went so if it is solved then player won
        st.session_state.winner = "You Win!"
        return 0
    elif len(check_board.get_actions()) == 0:
        st.session_state.winner = "It's a tie!"
        return 0

    ## AI makes a move
    ai_move(convert_board_for_ai,i,j)
    ## check if the AI won
