import init

import csv
import numpy as np 
from sklearn.preprocessing import LabelEncoder

# Fonction sigmoïde
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Fonction de coût
def compute_cost(theta, X, y):
    m = len(y)
    h = sigmoid(X.dot(theta))
    cost = (-1/m) * (y.T.dot(np.log(h)) + (1 - y).T.dot(np.log(1 - h)))
    return cost

# Gradient de la régression logistique
def compute_gradient(theta, X, y):
    m = len(y)
    h = sigmoid(X.dot(theta))
    gradient = (1/m) * X.T.dot(h - y)
    return gradient

# Gradient Descent pour entraîner un modèle
def gradient_descent(X, y, theta, learning_rate, num_iterations):
    m = len(y)
    for i in range(num_iterations):
        gradient = compute_gradient(theta, X, y)
        theta -= learning_rate * gradient
    return theta

# Entraînement One-vs-All
def one_vs_all(X, y, num_labels, learning_rate=0.1, num_iterations=1000):
    m, n = X.shape
    all_theta = np.zeros((num_labels, n))  # Matrice de theta pour chaque classe
    
    X = np.hstack([np.ones((m, 1)), X])  # Ajouter une colonne de 1 pour le biais
    
    for c in range(num_labels):
        y_c = np.array([1 if label == c else 0 for label in y])  # Cible binaire pour la classe c
        theta = np.zeros(n + 1)  # Initialisation de theta
        all_theta[c] = gradient_descent(X, y_c, theta, learning_rate, num_iterations)  # Entraînement
    return all_theta

# Prédiction
def predict_all(X, all_theta):
    m = X.shape[0]
    X = np.hstack([np.ones((m, 1)), X])  # Ajouter le biais
    prob = sigmoid(X.dot(all_theta.T))  # Calcul des probabilités
    return np.argmax(prob, axis=1)  # Retourner la classe avec la probabilité la plus élevée

if __name__ == "__main__":
    file_path = '../docs/dataset_train.csv'
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    features = [
        'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts',
        'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic',
        'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'
    ]
    X = np.array([[float(row[feature]) if row[feature] else np.nan for feature in features] for row in data])
    y = np.array([row['Hogwarts House'] for row in data])

    encoder = LabelEncoder()
    y = encoder.fit_transform(y)

    col_means = np.nanmean(X, axis=0)
    inds = np.where(np.isnan(X))
    X[inds] = np.take(col_means, inds[1])

    num_labels = len(np.unique(y))

    all_theta = one_vs_all(X, y, num_labels)

    predictions = predict_all(X, all_theta)

    print("Prédictions:", predictions)
