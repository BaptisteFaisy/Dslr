from init import *
import sys

def main(): # faut faire par rapport au maison fuck
   feature = []
   option = ""
   data = {}
   nbr_l =  0
   if (len(sys.argv) != 2):
      print("Erreur : Input incorrect")
      return
   argv = sys.argv[1]
   with open(argv, "r") as fichier: # ../docs/dataset_train.csv
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
   tab_result= []
   for i in range(6, len(data)):
      tab_result.append((abs(ecart_type(data[feature[i]])) / abs(moyenne(data[feature[i]])) * 100))
   print(tab_result)
   min = 0
   idx = 0
   i = 7
   for k in tab_result:
      if (min == 0):
         min = k
         idx = i
      if (min > k):
         min = k
         idx = i
      i = i + 1
   print(idx)

if __name__ == "__main__":
    main()