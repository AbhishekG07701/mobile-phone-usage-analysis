# Importing required modules
import matplotlib.pyplot as plt
from numerize.numerize import numerize


# Creating a helper function for adding titles and labels to the plot
def set_plot_title_and_labels(title, xlabel, ylabel):
    """
    Function for adding title and axis lables to the plot.

    Parameters:
    - title: The title of the plot.
    - xlabel: The label for the x-axis.
    - ylabel: The label for the y-axis.
    """

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


# Creating a helper function for changin the format of the values
def change_value_format(value, decimal = True):
    """
    Function for changing the format of the values to make it more human readable.
    
    Parameter:
    - value: The value whose format needs to be changed.
    """
    if not decimal:
        symbol = numerize(value)[-1]
        rounded_value = round(float(numerize(value)[:-1]))
        return f"{rounded_value}{symbol}"
    return numerize(value)


# Creating a helper function for annotating bars
def annotate_bars(ax, decimal = True):
    """
    Function for adding values on top of the bars.

    Parameter:
    - ax: The axis of the plot
    """
    
    # Annotating all of the bars
    for bar in ax.patches:
        if bar.get_height() > 0:
            ax.annotate(
                change_value_format(bar.get_height(), decimal),
                (bar.get_x() + bar.get_width()/2, bar.get_height()),
                ha = 'center', va = 'bottom', fontweight = 'bold'
            )
            
            