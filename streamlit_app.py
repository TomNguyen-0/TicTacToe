"""
Purpose:
    Using the knowledge from an AI class I took, CS550
    where I learned how to solve a NPuzzle.
    I applied that to the game Tic Tac Toe.


references:
    [Tamoghna Das Made his own version]: https://alphazero-tictactoeapp.streamlit.app/
        [Tamoghna Das GitHub]: https://github.com/tamoghna21/alphazero-TicTacToe_streamlit/blob/main/app_tictactoe_alphazero_streamlit.py
    Dr. Marie A. Roch Ph.D. - CS550

Date            Name            Description
05/26/2024      Tom Nguyen      initial create
05/27/2024      Tom Nguyen      Allow A.I. to make a move
05/28/2024      Tom Nguyen      Add check for winner
05/29/2024      Tom Nguyen      allow A.I. to go second
"""
import streamlit as st
from css import get_button_color_css
from click_button import on_button_click, ai_move
from reset_board import reset_game
from copy import deepcopy

st.markdown(get_button_color_css(), unsafe_allow_html=True)
st.header('Play Tic Tac Toe with an A.I. agent using :red[BreadthFirst] methodologies', divider='rainbow')
options = ["You play first", "You play second"]
selected_option = st.radio("Select an option:", options=options, horizontal=True,
                           on_change=reset_game, key='radio')

# Initialize session state for the board and current player
if 'board' not in st.session_state:
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
if 'current_player' not in st.session_state:
    st.session_state.current_player = 'X'
if 'ai_decision' not in st.session_state:
    st.session_state.ai_decision = ''
if 'winner' not in st.session_state:
    st.session_state.winner = ''
if 'go_first' not in st.session_state:
    st.session_state.go_first = False

num_cols = 3
cols= st.columns(num_cols,gap='small')
for i in range(num_cols):
    for j in range(num_cols):
        cols[j].button(label=st.session_state.board[i][j] or "  ",
                    on_click=on_button_click, 
                    args=(i, j, st.session_state.current_player), 
                    key=f'button_{i}_{j}',
                    type="primary")

if st.session_state.ai_decision and st.session_state.winner == '':
    st.write("AI is thinking of making these moves (row,column):",tuple(st.session_state.ai_decision))
st.write(st.session_state.winner)
st.button("Play Again!", on_click=reset_game,type="secondary")