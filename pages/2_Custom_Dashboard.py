"""In this page you can visualize Jira statistics."""

import streamlit as st
from streamlit_ace import st_ace

from src.dashboard import Dashboard, px

st.write("# Custom Dashboard")

st.write("Build your own dashboards.")

PLOT_FUN_MAP = {
    "Bar": px.bar,
    "Line": px.line
}

with st.expander("Dashboard settings", expanded=True):
    col1, col2, col3 = st.columns(3)
    name = col1.text_input("Dashboard name", value="Test dashboard")
    x = col2.text_input("Horizontal axis", value="month")
    y = col2.text_input("Vertical axis", value="issue_count")
    group_by = col3.text_input("Group by column", value="assignee_display_name")
    plot_fun = col1.selectbox("Type of plot", options=PLOT_FUN_MAP.keys())
    add_trend = col3.toggle("Add tendency line")

    st.write("Query")
    query = st_ace(
        language="sql",
        min_lines=3,
        key="user_input",
        value="""
SELECT
    assignee_display_name,
    DATE_TRUNC('month', resolution_date) AS month,
    COUNT(*) AS issue_count
FROM jira_issue
WHERE project_key = 'CCXDEV'
AND assignee_display_name = 'Juan Diaz Suarez'
    AND status = 'Closed'
    AND LOWER(labels::TEXT)::jsonb ? 'ccx-processing'
GROUP BY assignee_display_name, month;
"""
    )

if query:
    d = Dashboard(
        name=name,
        query=query,
        x=x,
        y=y,
        group_by=group_by,
        plot_fun=PLOT_FUN_MAP[plot_fun],
        add_trend=add_trend
    )
    d.render()
