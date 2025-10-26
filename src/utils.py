# src/utils.py
"""
utils.py
---------
Utility module for global environment setup, visualization style configuration,
and warning management. These settings are automatically applied when imported
in main.py or other project modules.
"""

import warnings
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def setup_environment():
    """
    Initialize the global environment.

    - Configure pandas display settings
    - Set matplotlib default figure style
    - Suppress unnecessary warnings
    - Apply 'ggplot' visualization theme
    """
    # Pandas display settings
    pd.set_option('display.float_format', '{:.2f}'.format)
    pd.set_option('display.max_columns', None)

    # Matplotlib style
    plt.rcParams['figure.figsize'] = [10, 6]
    plt.style.use('ggplot')

    # Suppress warnings
    warnings.filterwarnings('ignore')


def configure_chinese_fonts():
    """
    Configure matplotlib to properly display Chinese characters and minus signs.
    Call this function before plotting charts with Chinese text.
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']   # Support Chinese characters
    plt.rcParams['axes.unicode_minus'] = False     # Display minus signs correctly


def set_color_palette():
    """
    Define a custom color palette for visualization.

    Returns:
        list[str]: A list of HEX color codes for use in categorical plots.
    """
    return ["#FF9999", "#66CCFF"]


def show_missing_heatmap(df: pd.DataFrame, cmap: str = 'magma'):
    """
    Plot a heatmap of missing values in the dataset.

    Args:
        df (pd.DataFrame): Input dataframe.
        cmap (str, optional): Colormap to use. Defaults to 'magma'.
    """
    sns.heatmap(df.isnull(), cmap=cmap, cbar=False)
    plt.title("Missing Values Heatmap")
    plt.show()
