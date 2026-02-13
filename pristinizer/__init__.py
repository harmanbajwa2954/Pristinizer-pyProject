"""
pristinizer
-----------

A lightweight Python package for automatic data cleaning,
exploratory data analysis (EDA), and missing value visualization.

Core Features:
- clean(): Automatically clean datasets
- summarize(): Generate dataset summary
- missing_matrix(): Visualize missing values as matrix
- missing_heatmap(): Visualize missing values as heatmap
- missing_bar(): Visualize missing values as bar chart
"""

# Cleaning
from .cleaner import clean

# EDA
from .eda import summarize

# Visualization
from .missing import (
    missing_matrix,
    missing_heatmap,
    missing_bar,
)

# Version
__version__ = "1.0.1"

# Public API
__all__ = [
    "clean",
    "summarize",
    "missing_matrix",
    "missing_heatmap",
    "missing_bar",
]
