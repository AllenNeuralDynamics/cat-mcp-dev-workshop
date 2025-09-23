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
def execute_query(file_path: str, query: str, table_name: str) -> str:
    """
    Execute a SQL query on a CSV file and return the results as a JSON string.
    `table_name` MUST match the table name in the SQL query.
    """
    return pl.read_csv(file_path).sql(query, table_name=table_name).write_json()

"""
TASK: Fix the arguments in the function - make it more descriptive!
"""
@mcp.tool()
def get_summary_stats(var_1, var_2):
    """
    Get summary statistics for a csv file, with optional subsetting of a list of columns.
    
    """
    df = pl.read_csv(var_1)
    if var_2:
        df = df.select(var_2)
    return df.select(var_2 or pl.all()).describe().write_json()

"""
TASK: create a MCP function for our server.

Given that df[column].value_counts() returns the count of 
each variable in a column, fill out the function below.

Note that df = pl.read_csv(x) allows you to read a csv based on the file path.

You will need to input arguments, type hints, a docstring and the function.
"""
@mcp.tool()
def get_value_counts():
    """
    TODO

    """
    pass

def main():
    """Main entry point for the MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()