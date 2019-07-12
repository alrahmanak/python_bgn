import matplotlib.pyplot as plot
import numpy as np

def testscaterplt(x_data, y_data, x_label="", y_label="", title="", color = "b", yscale_log=False):

    # plot object
    _, ax = plot.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 10, color = color, alpha = 0.50)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plot.show();
	
age = [0,2,4,8,10,12,14,16,18,20,22,24]
slphrs = [12,12,11,10,10,10,10,9,9,9,9,9]
testscaterplt(age, slphrs, "Age", "Sleep Hrs", "Age vs Sleep")
