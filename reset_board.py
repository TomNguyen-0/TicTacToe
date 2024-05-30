
import streamlit as st
from click_button import  ai_move

def reset_game():
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.ai_decision = ''
    st.session_state.winner = ''

    if st.session_state.radio == "You play second":
        ai_move(convert_board_for_ai=st.session_state.board)