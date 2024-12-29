
import matplotlib.pyplot as plt

import numpy as np

import matplotlib.pyplot as plt

# Données
def main():
    dataset1 = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    dataset2 = [2, 3, 3, 4, 4, 5, 5, 6, 7]

    # Créer un histogramme pour plusieurs ensembles
    plt.hist([dataset1, dataset2], bins=5, label=['Dataset 1', 'Dataset 2'], color=['blue', 'orange'], alpha=0.7, edgecolor='black')

    # Ajouter des titres et légendes
    plt.title('Histogramme avec plusieurs ensembles de données')
    plt.xlabel('Valeurs')
    plt.ylabel('Fréquence')
    plt.legend()

    # Afficher
    plt.show()



if __name__ == "__main__":
    main()
