"""In this page you can visualize Jira statistics."""

import streamlit as st

from src.examples.dashboards import SAMPLE_DASHBOARDS

st.write("# Prebuilt Dashboards")

st.write("Visualize your data in a much friendlier way.")

tabs = tabs = st.tabs([d.name for d in SAMPLE_DASHBOARDS])
for i, dashboard in enumerate(SAMPLE_DASHBOARDS):
    with tabs[i]:
        dashboard.render()
