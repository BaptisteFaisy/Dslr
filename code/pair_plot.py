
from init import *

import matplotlib.pyplot as plt

import numpy as np

import matplotlib



def pair_plot_hist(ax, X): # patch ca
  h1 = np.array(list(find(1, X)))
  ax.hist(h1, alpha=0.5)

  h2 = np.array(list(find(4, X)))
  ax.hist(h2, alpha=0.5)

  h3 = np.array(list(find(2, X)))
  ax.hist(h3, alpha=0.5)

  h4 = np.array(list(find(3, X)))
  ax.hist(h4, alpha=0.5)

def pair_plot_scatter(ax, X, Y): # patch ca
    x = list(find(1, X))
    y = (list(find(1, Y)))
    if (len(x) >= len(y)):
        x = size_corrector(x,y)
    else :
        y = size_corrector(x,y)
    ax.scatter(np.array(x), np.array(y), s=1, color='red', alpha=0.5)
    x =list(find(4, X))
    y = list(find(4, Y))
    if (len(x) >= len(y)):
        x = size_corrector(x,y)
    else :
        y = size_corrector(x,y)
    ax.scatter(np.array(x), np.array(y), s=1, color='yellow', alpha=0.5)
    x = list(find(2, X))
    y = list(find(2, Y))
    if (len(x) >= len(y)):
        x = size_corrector(x,y)
    else :
        y = size_corrector(x,y)
    ax.scatter( np.array(x),  np.array(y), s=1, color='blue', alpha=0.5)
    x = list(find(3, X))
    y = list(find(3, Y))
    if (len(x) >= len(y)):
        x = size_corrector(x,y)
    else :
        y = size_corrector(x,y)
    ax.scatter(np.array(x), np.array(y), s=1, color='green', alpha=0.5)

def pair_plot():
    legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    data = openfile()
    features = list(data.keys())[6:]
    font = {'family' : 'DejaVu Sans',
            'weight' : 'light',
            'size'   : 7}
    matplotlib.rc('font', **font)

    size = len(features)
    _, ax = plt.subplots(nrows=size, ncols=size)
    plt.subplots_adjust(wspace=0.15, hspace=0.15)

    for row in range(0, size):
        for col in range(0, size):
            X = list(data.keys())[col +6 ] # X = name
            y = list(data.keys())[row +6 ]
            
            if col == row:
                pair_plot_hist(ax[row, col], X)
            else:
                pair_plot_scatter(ax[row, col], X, y)

            if col == size - 1:
                ax[row, col].set_xlabel(features[col].replace(' ', '\n'))
            else:
                ax[row, col].tick_params(labelbottom=False)

            if col == 0:
                ax[row, col].set_ylabel(features[row].replace(' ', '\n'))
            else:
                ax[row, col].tick_params(labelleft=False)

            ax[row, col].spines['right'].set_visible(False)
            ax[row, col].spines['top'].set_visible(False)

    plt.legend(legend, loc='center left', frameon=False, bbox_to_anchor=(1, 0.5))
    plt.show()


if __name__ == "__main__":
    pair_plot()
