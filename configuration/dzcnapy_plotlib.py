"""
Library for plotting graphs in DZCNAPY
"""
import matplotlib
import matplotlib.pyplot as plt

import configuration.config as config

results_path = "/Users/maimai/Desktop/project/May/data/givenchy/pickle" 
print(results_path)

matplotlib.rc("font", family="DejaVu Sans")
matplotlib.style.use("grayscale")



def set_extent(positions, axes, title=None):
    """
    Given node coordinates pos and the subplot,
    calculate and set its extent.
    """
    axes.tick_params(labelbottom="off")
    axes.tick_params(labelleft="off")
    if title:
        axes.set_title(title)

    x_values, y_values = zip(*positions.values())
    x_max = max(x_values)
    y_max = max(y_values)
    x_min = min(x_values)
    y_min = min(y_values)
    x_margin = (x_max - x_min) * 0.1
    y_margin = (y_max - y_min) * 0.1
    try:
        axes.set_xlim(x_min - x_margin, x_max + x_margin)
        axes.set_ylim(y_min - y_margin, y_max + y_margin)
    except AttributeError:
        axes.xlim(x_min - x_margin, x_max + x_margin)
        axes.ylim(y_min - y_margin, y_max + y_margin)

def plot(fname, size, save = True):
    
    plt.tight_layout()
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(size[0], size[1], forward=True)
    plt.rcParams['figure.figsize'] = size
    if save:
        plt.savefig("{}/{}.pdf".format(results_path, fname), dpi=600)
    plt.show()
    plt.close()
    
    
attrs = {
    "edge_color" : "gray",
    "font_family" : "DejaVu Sans",
    "font_size" : 10,
    "node_color" : "pink",
    "font_weight" : "bold",
    "node_size" : 70,
    "width" : 2,
}

thick_attrs = attrs.copy()
thick_attrs["alpha"] = 0.5
thick_attrs["width"] = 5

small_attrs = attrs.copy()
small_attrs["node_size"] = 5
small_attrs["font_size"] = 10

medium_attrs = small_attrs.copy()
medium_attrs["node_size"] = 25