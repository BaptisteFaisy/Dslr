from init import *
import sys

def main():
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
	cles = list(data.keys())
	str1 = ""
	nbr_l = 0
	# print(data[feature[0]])
	print ("                                             Count            Mean            Std            Min            25%            50%           75%            Max")
	for k in cles: # changement de ligne 
		print(k, end="")
		for i in range(45 - len(k)):
			print(" ", end="")
		printconter(data, feature, nbr_l)
		printmoy(data, feature , nbr_l)
		printstd(data, feature , nbr_l)
		printmin(data, feature, nbr_l)
		print25(data, feature, nbr_l)
		print50(data, feature, nbr_l)
		print75(data, feature, nbr_l)
		printmax(data, feature, nbr_l)
		print("")
		nbr_l += 1


if __name__ == "__main__":
    main()


