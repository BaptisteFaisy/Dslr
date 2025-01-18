import init

import csv
import numpy as np 
from sklearn.preprocessing import LabelEncoder

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# X.dot(theta) est le produit matriciel entre X et theta, représentant les prédictions linéaires.
def compute_gradient(theta, X, y):
    m = len(y)
    h = sigmoid(X.dot(theta)) #sigmoid() applique la fonction sigmoïde pour transformer les valeurs linéaires en probabilités 
    gradient = (1/m) * X.T.dot(h - y)
    return gradient

def gradient_descent(X, y, theta, learning_rate, num_iterations):
    m = len(y)
    for i in range(num_iterations): # ca boucle sur 1k mais pas de probleme normalement
        gradient = compute_gradient(theta, X, y)
        theta -= learning_rate * gradient
    return theta

def one_vs_all(X, y, num_labels, learning_rate=0.1, num_iterations=1000):
    m, n = X.shape # m = ligne et n = colonne
    all_theta = np.zeros((num_labels, n))  # fait un tab de 0 idk why
    
    X = np.hstack([np.ones((m, 1)), X]) # np.one cree un tab de 1 et np.hstack les concatene ?
    
    for c in range(num_labels): #num labels = nombre de maison donc ca boucle sur 4 enfin jsp
        y_c = np.array([1 if label == c else 0 for label in y]) # y = tab avec les num pour les houses 
        theta = np.zeros(n + 1)
        all_theta[c] = gradient_descent(X, y_c, theta, learning_rate, num_iterations)
    return all_theta

def predict_all(X, all_theta):
    m = X.shape[0]
    X = np.hstack([np.ones((m, 1)), X])
    prob = sigmoid(X.dot(all_theta.T))
    return np.argmax(prob, axis=1)

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
    y = encoder.fit_transform(y) # y est un tab des numero des maisons genre la colonne.
    col_means = np.nanmean(X, axis=0)
    inds = np.where(np.isnan(X))
    X[inds] = np.take(col_means, inds[1])

    num_labels = len(np.unique(y)) # num label est le nombre de maison
    all_theta = one_vs_all(X, y, num_labels)

    predictions = predict_all(X, all_theta)

    print("Prédictions:", predictions)
