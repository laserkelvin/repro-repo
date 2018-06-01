"""routines.py

    This is a dummy Python module that serves as a placeholder
    for any code you want to use across your notebooks.

    Some examples are file I/O functions that you repeatedly use
    across different notebooks, and plotting functions (if you
    don't have a module written already).

    It's important to keep good docstrings in your code, so
    that you can come back to it a week later and continue
    where you left off!
"""

import numpy as np
import pandas as pd
from glob import glob
import os
from matplotlib import pyplot as plt


def load_data(filepath):
    """ Function to load data in as a pandas DataFrame.
    Uses whitespace as delimiters.

    Args: filepath - path to the data you want to load in
    """
    df = pd.read_csv(filepath, delim_whitespace=True)
    return df


def batch_load(directory):
    """ Batch load a directory of files as pandas DataFrames
    Uses `glob` to find all the files and `load_data` to load
    them.

    Args: directory - path to the directory you want to load.
    """
    # Glob picks up all of the files
    filelist = glob(os.path.join(directory, "*"))
    # List comprehension to batch load
    # try/except to make sure any bad data points are flagged
    # and the user is warned
    try:
        dataframes = [load_data(item) for item in filelist]
    except EmptyDataError:
        print(item + " was empty and could not be loaded.")
    return dataframes


def plot_df(df, x=None):
    """ Function to plot all of the columns of a dataframe.
    Optional argument allows you to specify the x (absicssa). If
    this is None, then the first column is used.

    args: df - Dataframe to plot
          x - column name to use as x axis (optional)
    """
    if x and x in df.columns:
        # Check that the specified column name actually
        # exists in the dataframe
        x_col = x
    else:
        # If nothing is given or an invalid choice of column,
        # default to using the first column
        x_col = df.columns[0]
    fig, ax = plt.subplots(figsize=(4,8))

    # Loop over the dataframe columns
    for col in df:
        # For everything except the x-axis, plot it up
        if col != x_col:
            ax.plot(
                df[x_col],
                df[col],
                label=col
                )
    # Generate a legend
    ax.legend()
    fig.tight_layout()
    return fig, ax

