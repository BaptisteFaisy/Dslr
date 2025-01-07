
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# FAUX FAUX FAUX

def load_csv(filename):
  dataset = list()
  with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    try:
      for _ in reader:
        row = list()
        for value in _:
          try:
            value = float(value)
          except:
            if not value:
              value = np.nan
          row.append(value)
        dataset.append(row)
    except csv.Error as e:
      print(f'file {filename}, line {reader.line_num}: {e}')
  return np.array(dataset, dtype=object)

def scatter_plot(X, y, legend, xlabel, ylabel):
  print(X[0])
  print(y[0])
  plt.scatter(X[:327], y[:327], color='red', alpha=0.5)
  plt.scatter(X[327:856], y[327:856], color='yellow', alpha=0.5)
  plt.scatter(X[856:1299], y[856:1299], color='blue', alpha=0.5)
  plt.scatter(X[1299:], y[1299:], color='green', alpha=0.5)
  print(X)

  plt.legend(legend, loc='upper right', frameon=False)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.show()

def pair_plot_hist(ax, X):
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

def pair_plot(dataset, features, legend):
  font = {'family' : 'DejaVu Sans',
          'weight' : 'light',
          'size'   : 7}
  matplotlib.rc('font', **font)

  size = dataset.shape[1]
  _, ax = plt.subplots(nrows=size, ncols=size)
  plt.subplots_adjust(wspace=0.15, hspace=0.15)

  for row in range(0, size):
    for col in range(0, size):
      X = dataset[:, col]
      y = dataset[:, row]

      if col == row:
        pair_plot_hist(ax[row, col], X)
      else:
        pair_plot_scatter(ax[row, col], X, y)

      if ax[row, col].is_last_row():
        ax[row, col].set_xlabel(features[col].replace(' ', '\n'))
      else:
        ax[row, col].tick_params(labelbottom=False)

      if ax[row, col].is_first_col():
        ax[row, col].set_ylabel(features[row].replace(' ', '\n'))
      else:
        ax[row, col].tick_params(labelleft=False)

      ax[row, col].spines['right'].set_visible(False)
      ax[row, col].spines['top'].set_visible(False)

  plt.legend(legend, loc='center left', frameon=False, bbox_to_anchor=(1, 0.5))
  plt.show()

if __name__ == '__main__':
  dataset = load_csv('../docs/dataset_train.csv')
  data = dataset[1:, 6:]
  data = data[data[:, 1].argsort()]

  features = dataset[0, 6:]
  legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

  pair_plot(np.array(data, dtype=float), features, legend)
  plt.show()
