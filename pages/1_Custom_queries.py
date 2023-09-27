"""In this page you can run custom quieries to the Jira SQL database."""

import streamlit as st
from streamlit_ace import st_ace

from src.reader import run_query
from src.examples.queries import SAMPLE_QUERIES


st.write("# Custom queries")

st.markdown("""
Run custom queries using SQL statements. Check the table definition in
[the docs](https://hub.steampipe.io/plugins/turbot/jira/tables).""")


query = st_ace(
    language="sql",
    min_lines=3,
    key="user_input"
)

with st.expander("Result", expanded=True):
    if query:
        try:
            ans = run_query(query)
            st.dataframe(ans)
        except Exception as ex:
            st.error(
                f"""
                There was an error running the query:
                
                {ex}
                """)

st.write("#### Get inspired by sample queries")

tabs = st.tabs(SAMPLE_QUERIES.keys())
for i, (alias, query) in enumerate(SAMPLE_QUERIES.items()):
    with tabs[i]:
        st_ace(
            value=query,
            language="sql",
            min_lines=3,
            readonly=True,
            key=f"sample_{alias}"
        )
