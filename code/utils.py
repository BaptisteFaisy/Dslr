from init import *
import csv
import numpy as np
import sys

def openfile():
   feature = []
   option = ""
   data = {}
   nbr_l =  0
   with open( "../docs/dataset_train.csv", "r") as fichier: 
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
               if (option != ""):
                  data[feature[nbr_l]].append(option)
                  option = ""
               nbr_l+= 1
   return data

def size_corrector(liste1, liste2):
  if len(liste1) >= len(liste2):
    diff = len(liste1) - len(liste2)
    for i in range(diff):
      del liste1[-1]
    return liste1
  elif len(liste1) < len(liste2):
    diff = len(liste2) - len(liste1)
    for i in range(diff):
      del liste2[-1]
    return liste2
   