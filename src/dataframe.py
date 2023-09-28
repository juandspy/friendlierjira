"""Utility functions for dataframes."""
import streamlit as st
import pandas as pd


@st.cache_data
def convert_df(df):
    """Convert a Pandas dataframe to a CSV object."""
    return df.to_csv(index=False).encode('utf-8')


def show_df_with_download_button(df: pd.DataFrame):
    """Render the dataframe with a download button to get the CSV."""
    st.dataframe(df)

    st.download_button(
        "Download the CSV",
        convert_df(df),
        "file.csv",
        "text/csv"
    )
