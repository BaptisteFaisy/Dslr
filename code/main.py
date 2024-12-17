from init import *

def main():
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
					data[feature[nbr_l]].append(option)
					option = ""
					nbr_l+= 1
	cles = list(data.keys())
	str1 = ""
	nbr_l = 0
	# print(data[feature[0]])
	print ("                                                  Count                    Mean                    Std                    Min                    25%                    50%                   75%                 Max")
	for k in cles: # changement de ligne 
		print(k, end="")
		for i in range(50 - len(k)):
			print(" ", end="")
		printconter(data, feature, nbr_l)
		printmoy(data, feature , nbr_l)
		nbr_l += 1


if __name__ == "__main__":
    main()


