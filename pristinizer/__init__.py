"""
Pristinizer: Automatic Data Cleaning and EDA package
"""

from .cleaner import clean
from .eda import analyze
from .missing import visualize_missing

__all__ = ["clean", "analyze", "visualize_missing"]

__version__ = "0.1.0"
