"""
pristinizer.visualizer
----------------------

Missing data visualization utilities.

Provides functions to visualize missing values using heatmaps,
matrix plots, and bar charts.

Author: pristinizer
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def _validate_dataframe(df):
    """
    Internal helper to validate input.

    Raises:
        TypeError: if input is not a pandas DataFrame
        ValueError: if DataFrame is empty
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    if df.empty:
        raise ValueError("DataFrame is empty")


def missing_matrix(df, figsize=(10, 6), save_path=None):
    """
    Visualize missing values as a matrix.

    Each column is shown vertically, missing values highlighted.

    Parameters:
        df (pd.DataFrame): input dataframe
        figsize (tuple): figure size
        save_path (str, optional): path to save image

    Returns:
        matplotlib.figure.Figure
    """
    _validate_dataframe(df)

    fig, ax = plt.subplots(figsize=figsize)

    ax.imshow(df.isnull(), aspect='auto', interpolation='nearest')

    ax.set_xlabel("Columns")
    ax.set_ylabel("Rows")
    ax.set_title("Missing Value Matrix")

    ax.set_xticks(range(len(df.columns)))
    ax.set_xticklabels(df.columns, rotation=90)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    return fig


def missing_heatmap(df, figsize=(10, 6), cmap="viridis", save_path=None):
    """
    Visualize missing values using heatmap.

    Parameters:
        df (pd.DataFrame): input dataframe
        figsize (tuple): figure size
        cmap (str): colormap
        save_path (str, optional): path to save image

    Returns:
        matplotlib.figure.Figure
    """
    _validate_dataframe(df)

    fig, ax = plt.subplots(figsize=figsize)

    sns.heatmap(
        df.isnull(),
        cbar=False,
        cmap=cmap,
        yticklabels=False,
        ax=ax
    )

    ax.set_title("Missing Value Heatmap")
    ax.set_xlabel("Columns")
    ax.set_ylabel("Rows")

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    return fig


def missing_bar(df, figsize=(10, 6), color="red", save_path=None):
    """
    Show missing value counts per column as bar chart.

    Parameters:
        df (pd.DataFrame): input dataframe
        figsize (tuple): figure size
        color (str): bar color
        save_path (str, optional): path to save image

    Returns:
        matplotlib.figure.Figure
    """
    _validate_dataframe(df)

    missing_counts = df.isnull().sum()

    fig, ax = plt.subplots(figsize=figsize)

    missing_counts.plot.bar(ax=ax, color=color)

    ax.set_title("Missing Values per Column")
    ax.set_xlabel("Columns")
    ax.set_ylabel("Missing Count")

    plt.xticks(rotation=45)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    return fig
