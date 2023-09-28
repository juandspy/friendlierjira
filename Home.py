"""Home page"""

import streamlit as st


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "https://github.com/juandspy/friendlierjira"
    }
)

st.title('Friendlier Jira')
