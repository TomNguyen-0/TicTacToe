def get_button_color_css():
    return f"""
            <style>
                div[data-testid="column"]{{
                    width: 40px;
                    flex: unset;
                }}
                div[data-testid="column"] * {{
                    width: 40px;
                }}
                .stButton>button["primary"] {{
                    border: 1px solid #FF0000;
                    margin: 5px;
                    
                }}
                .stButton>button["secondary"] {{
                    border: 2px solid #FF0000;
                    margin: 5px;
                    outline: none;
                    
                }}
            </style>
            """