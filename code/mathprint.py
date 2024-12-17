from init import *


def printconter(data, feature, nbr_l):
	nbr =  conter(data[feature[nbr_l]])
	if (len(str(nbr) )> 20):
		str1 = arrondir(nbr)
	else:
		print(nbr)
		for i in range(20 - len(str(nbr))):
			print(" ", end="")

def printmoy(data, feature, nbr_l):
	nbr =  moyenne(data[feature[nbr_l]])
	if (len(str(nbr) )> 20):
		str1 = arrondir(nbr)
	else:
		print(nbr)
		for i in range(20 - len(str(nbr))):
			print(" ", end="")