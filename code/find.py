from init import *
import csv
import numpy as np
import sys

# house == 1 == Gryffindor
# house == 2 == Ravenclaw
# house == 3 == Slytherin
# house == 4 == Hufflepuff

# def findbestsubject():
    # data = openfile()
    # tab_result= []
    # for i in range(6, len(data)):
    #     tab_result.append((abs(ecart_type(data[feature[i]])) / abs(moyenne(data[feature[i]])) * 100))
    # print(tab_result)
    # min = 0
    # idx = 0
    # i = 7
    # for k in tab_result:
    #     if (min == 0):
    #         min = k
    #         idx = i
    #     if (min > k):
    #         min = k
    #         idx = i
    #     i = i + 1
    # print(idx)

def find(house, name, same_size=False, other_size= True):
    feature = []
    option = ""
    data = {}
    nbr_l =  0
    with open("../docs/dataset_train.csv", "r") as fichier: 
      ligne = fichier.readline()
      for i in ligne:
          if (i != ',' and i != '\n'):
            option += i
          else :
            feature.append(option)
            data[option] = []
            option = ""

      for ligne in fichier:
          option = ""
          nbr_l = 0
          for i in ligne:
            if (i != ',' and i != '\n'):
                option += i
            else:
                if (nbr_l == 1 and house == 1 and option != "Gryffindor"):
                    break
                if (nbr_l == 1 and house == 2 and option != "Ravenclaw"):
                    break
                if (nbr_l == 1 and house == 3 and option != "Slytherin"):
                    break
                if (nbr_l == 1 and house == 4 and option != "Hufflepuff"):
                    break
                if (option != "")  :
                    try:
                        data[feature[nbr_l]].append(float(option))
                    except ValueError:
                        data[feature[nbr_l]].append((option))
                    option = ""
                nbr_l+= 1
    return data[name]
    
# if __name__ == "__main__":
#     findbestsubject()