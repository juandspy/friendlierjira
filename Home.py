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

st.markdown(
    """
Welcome to the Friendlier Jira tool. A webapp that lets you run SQL
queries on your favourite Jira instance, be it cloud based or self-hosted.

Use the menu on the left side of the page to navigate. You can run custom
queries, build custom dashboard or use the prebuilt ones.
""")

st.image(
    "https://thenounproject.com/api/private/icons/546312/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=752&flipX=false&flipY=false&foregroundColor=%23000000&foregroundOpacity=1&imageFormat=png&rotation=0",
    width=250
)
