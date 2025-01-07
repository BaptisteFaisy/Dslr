
from init import *

import matplotlib.pyplot as plt

import numpy as np

import matplotlib



def pair_plot_hist(ax, X): # facile
  h1 = X[:327]
  h1 = h1[~np.isnan(h1)]
  ax.hist(h1, alpha=0.5)

  h2 = X[327:856]
  h2 = h2[~np.isnan(h2)]
  ax.hist(h2, alpha=0.5)

  h3 = X[856:1299]
  h3 = h3[~np.isnan(h3)]
  ax.hist(h3, alpha=0.5)

  h4 = X[1299:]
  h4 = h4[~np.isnan(h4)]
  ax.hist(h4, alpha=0.5)

def pair_plot_scatter(ax, X, y):
  ax.scatter(X[:327], y[:327], s=1, color='red', alpha=0.5)
  ax.scatter(X[327:856], y[327:856], s=1, color='yellow', alpha=0.5)
  ax.scatter(X[856:1299], y[856:1299], s=1, color='blue', alpha=0.5)
  ax.scatter(X[1299:], y[1299:], s=1, color='green', alpha=0.5)

def pair_plot():
    legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    data = openfile()
    features = list(data.keys())[6:]
    print(features)
    font = {'family' : 'DejaVu Sans',
            'weight' : 'light',
            'size'   : 7}
    matplotlib.rc('font', **font)

    size = len(features)
    _, ax = plt.subplots(nrows=size, ncols=size)
    plt.subplots_adjust(wspace=0.15, hspace=0.15)

    # for row in range(0, size):
    #     for col in range(0, size):
    #         X = dataset[:, col]
    #         y = dataset[:, row]

    #         if col == row:
    #             pair_plot_hist(ax[row, col], X)
    #         else:
    #             pair_plot_scatter(ax[row, col], X, y)

    #         if ax[row, col].is_last_row():
    #             ax[row, col].set_xlabel(features[col].replace(' ', '\n'))
    #         else:
    #             ax[row, col].tick_params(labelbottom=False)

    #         if ax[row, col].is_first_col():
    #             ax[row, col].set_ylabel(features[row].replace(' ', '\n'))
    #         else:
    #             ax[row, col].tick_params(labelleft=False)

    #         ax[row, col].spines['right'].set_visible(False)
    #         ax[row, col].spines['top'].set_visible(False)
    features = list(data.keys())  # Liste des clés du dictionnaire
    values = list(data.values())  # Liste des valeurs associées à chaque clé (en tant que listes)

    size = len(features)  # Taille du dictionnaire (nombre de caractéristiques)

    # Création des sous-graphes
    _, ax = plt.subplots(nrows=size, ncols=size)
    plt.subplots_adjust(wspace=0.15, hspace=0.15)

    # Parcours des paires de colonnes et lignes pour tracer les graphiques
    for row in range(0, size):
        for col in range(0, size):
            X = values[col]  # Les valeurs de la colonne (par exemple, 'feature1', 'feature2', etc.)
            y = values[row]  # Les valeurs de la ligne (par exemple, 'feature1', 'feature2', etc.)

            # Si on est sur la diagonale (col == row), afficher un histogramme
            if col == row:
                pair_plot_hist(ax[row, col], X)
            else:
                pair_plot_scatter(ax[row, col], X, y)

            # Ajout des labels pour les axes
            if ax[row, col].is_last_row():
                ax[row, col].set_xlabel(features[col].replace(' ', '\n'))
            else:
                ax[row, col].tick_params(labelbottom=False)

            if ax[row, col].is_first_col():
                ax[row, col].set_ylabel(features[row].replace(' ', '\n'))
            else:
                ax[row, col].tick_params(labelleft=False)

            # Suppression des bordures inutiles
            ax[row, col].spines['right'].set_visible(False)
            ax[row, col].spines['top'].set_visible(False)

    plt.legend(legend, loc='center left', frameon=False, bbox_to_anchor=(1, 0.5))
    plt.show()


if __name__ == "__main__":
    pair_plot()
