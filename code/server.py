""" MCP server for data access """

import json
from typing import Any

from numpy import dtype
import polars as pl
import pandas as pd
from fastmcp import FastMCP

mcp = FastMCP("csv_explorer")


@mcp.tool()
def get_table_schema(file_path: str) -> dict[str, str]:
    """
    Retrieves column names and dtypes for a given csv path

    """
    df = pl.read_csv(file_path)
    return {
        col_name: str(df[col_name].dtype)
        for col_name in df.columns
    }

@mcp.tool()
def get_summary_stats(file_path: str, columns: list[str] | None = None) -> str:
    """
    Get summary statistics for a csv file, with optional subsetting of columns.
    
    Parameters
    ----------
    file_path : str
        Path to file

    columns : list[str]
        List of columns to subset data -- e.g. ["age", "sex", "education"]

    """
    df = pl.read_csv(file_path)
    if columns:
        df = df.select(columns)
    return df.select(columns or pl.all()).describe().write_json()


@mcp.tool()
def execute_query(file_path: str, query: str, table_name: str) -> str:
    """
    Execute a SQL query on a CSV file and return the results as a JSON string.
    `table_name` MUST match the table name in the SQL query.
    """
    return pl.read_csv(file_path).sql(query, table_name=table_name).write_json()

@mcp.tool()
def get_value_counts(file_path: str, column: str) -> str:
    """
    Returns count of each variable in a column within a data frame
    
    Parameters
    ----------
    file_path : str
        Path to file

    column : str
        Column in data frame -- e.g. "age"

    """
    df = pl.read_csv(file_path)
    return df[column].value_counts().write_json()

def main():
    """Main entry point for the MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()