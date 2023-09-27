"""Dashboard implementation."""

from typing import List
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

from src.reader import run_query


class Dashboard:
    """This class is used to build dashboards in an easy way."""
    def __init__(self, name: str, query: str, x: str, y: str,
                 group_by: List[str], plot_fun = px.bar,
                 add_trend: bool = False):
        self.name = name
        self.query = query
        self.x = x
        self.y = y
        self.group_by = group_by
        self.plot_fun = plot_fun
        self.add_trend = add_trend

    def __str__(self) -> str:
        """What is shown when printing this class."""
        return self.name

    def get_ans(self) -> pd.DataFrame:
        """Get the data from the DB and convert it to a DataFrame"""
        return run_query(self.query).convert_dtypes()

    def plot(self):
        """Show a Plotly bar representing this data."""
        data = self.get_ans()
        fig = self.plot_fun(
                data, x=self.x, y=self.y, color=self.group_by)
        if self.add_trend:
            reg = LinearRegression().fit(
                data[self.x].values.reshape(-1, 1),
                data[self.y].values.reshape(-1, 1))
            data['tendency'] = reg.predict(
                data[self.x].values.astype(float).reshape(-1, 1))
            fig.add_traces(
                go.Scatter(
                    name='tendency',
                    x=data[self.x],
                    y=data['tendency'],
                    mode = 'lines'))
        fig.update_layout(title=self.name)
        st.plotly_chart(fig, use_container_width=True)

    def render(self):
        """Show the raw data, SQL query and plot."""
        data = self.get_ans()
        with st.expander("Raw data", expanded=False):
            st.dataframe(data)
        with st.expander("SQL query", expanded=False):
            st.code(
                language="sql",
                body=self.query)
        self.plot()
