"""Test: Example"""

import pandas as pd


def read_dataframe(dataframe: pd.DataFrame):
    """
    Creates a copy of the provided pandas DataFrame.

    This function is intended for potential use cases where you might want to
    avoid modifying the original DataFrame directly. However, it's important
    to note that in most cases, it's more efficient to work directly with the
    original DataFrame unless there's a specific reason to create a copy.

    Args:
        dataframe (pd.DataFrame): The pandas DataFrame to be copied.

    Returns:
        pd.DataFrame: A new DataFrame that is a copy of the input DataFrame.

    Raises:
        TypeError: If the input is not a pandas DataFrame.
    """
    new_dataframe = dataframe.copy()
    return new_dataframe

def add_applicant_ids(dataframe: pd.DataFrame):
    new_dataframe = dataframe.copy()
    new_dataframe['applicant_id'] = range(0, len(new_dataframe))
    return(new_dataframe)