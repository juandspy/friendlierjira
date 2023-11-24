"""Utility functions to read from the database."""
from sqlalchemy import create_engine

import pandas as pd
import streamlit as st

from src.config import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST, DB_PORT, QUERY_TIMEOUT_SECONDS


CONNECTION_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    CONNECTION_STRING,
    connect_args={
        "options": f"-c statement_timeout={QUERY_TIMEOUT_SECONDS * 1000}"}
    if QUERY_TIMEOUT_SECONDS > 0 else {},
    echo=True
)

@st.cache_data
def run_query(query: str) -> pd.DataFrame:
    """Run a query and get a pandas DataFrame as result."""
    return pd.read_sql(query, con=engine)
    


if __name__ == "__main__":
    df = run_query(
        """
        SELECT
            key,
            created,
            creator_display_name,
            status,
            summary
        FROM jira_issue
        WHERE project_key = 'CCXDEV'
        LIMIT 10;
        """
    )
    print(df)
