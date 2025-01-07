from init import *

import matplotlib.pyplot as plt

import numpy as np

import matplotlib.pyplot as plt


def scatter_plot():
    data = openfile()
    x = list(find(1, "Astronomy"))
    y = list(find(1, "Defense Against the Dark Arts"))
    if (len(x) >= len(y)):
        x = size_corrector(x,y)
    else :
        y = size_corrector(x,y)
    plt.scatter(np.array(x), np.array(y), color='red', alpha=0.3)
    x = list(find(4, "Astronomy"))
    y = list(find(4, "Defense Against the Dark Arts"))
    if (len(x) >= len(y)):
        x = size_corrector(x,y)
    else :
        y = size_corrector(x,y)
    plt.scatter(np.array(x), np.array(y), color='yellow', alpha=0.3)
    x = list(find(2, "Astronomy"))
    y = list(find(2, "Defense Against the Dark Arts"))
    if (len(x) >= len(y)):
        x = size_corrector(x,y)
    else :
        y = size_corrector(x,y)
    plt.scatter(np.array(x), np.array(y), color='blue', alpha=0.3)
    x = list(find(3, "Astronomy"))
    y = list(find(3, "Defense Against the Dark Arts"))
    if (len(x) >= len(y)):
        x = size_corrector(x,y)
    else :
        y = size_corrector(x,y)
    plt.scatter(np.array(x), np.array(y), color='green', alpha=0.3)
    plt.legend(['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'], loc='upper right', frameon=False)
    plt.xlabel("Astronomy")
    plt.ylabel("Defense Against the Dark Arts")
    plt.show()





if __name__ == "__main__":
    scatter_plot()
