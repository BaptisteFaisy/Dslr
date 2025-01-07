from init import *

import matplotlib.pyplot as plt

import numpy as np

import matplotlib.pyplot as plt

def histogram():
    legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    xlabel='Marks'
    ylabel='Number of student'
    h1 = list(find(1, "Care of Magical Creatures"))
    h1 = np.array(h1)
    plt.hist(h1, color='red', alpha=0.5)
    h2 = list(find(4, "Care of Magical Creatures"))
    h2 = np.array(h2)
    plt.hist(h2, color='yellow', alpha=0.5)
    h3 = list (find(2, "Care of Magical Creatures"))
    h3 = np.array(h3)
    plt.hist(h3, color='blue', alpha=0.5)
    h4 = list (find(3, "Care of Magical Creatures"))
    h4 = np.array(h4)
    print (h4)
    plt.hist(h4, color='green', alpha=0.5)

    plt.legend(legend, loc='upper right', frameon=False)
    plt.title("Care of Magical Creatures")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()




if __name__ == "__main__":
    histogram()
