from init import *


def printconter(data, feature, nbr_l):
	nbr =  conter(data[feature[nbr_l]])
	if (len(str(nbr) )> 20):
		str1 = arrondir(nbr)
	else:
		print(nbr, end="")
		for i in range(17 - len(str(nbr))):
			print(" ", end="")

def printmoy(data, feature, nbr_l):
	nbr = moyenne(data[feature[nbr_l]])
	if (nbr == -1):  # Indentation correcte
		print("Invalid value", end ="")
		for i in range(16 - len("Invalid value")):
			print(" ", end="")
		return
	print(f"{nbr:.2f}", end="")  # Affiche la moyenne avec 2 décimales
	for i in range(16 - len(f"{nbr:.2f}")):
		print(" ", end="")

def printstd(data, feature, nbr_l):
	nbr = ecart_type(data[feature[nbr_l]])
	if (nbr == -1):  # Indentation correcte
		print("Invalid value", end ="")
		for i in range(15 - len("Invalid value")):
			print(" ", end="")
		return
	print(f"{nbr:.2f}", end="")  # Affiche la moyenne avec 2 décimales
	for i in range(15 - len(f"{nbr:.2f}")):
		print(" ", end="")

def printmin(data, feature, nbr_l):
	nbr = valeur_minimale(data[feature[nbr_l]])
	if (nbr == -1):  # Indentation correcte
		print("Invalid value", end ="")
		for i in range(15 - len("Invalid value")):
			print(" ", end="")
		return
	print(f"{nbr:.2f}", end="")  # Affiche la moyenne avec 2 décimales
	for i in range(15 - len(f"{nbr:.2f}")):
		print(" ", end="")

def print25(data, feature, nbr_l):
	nbr = percentile(data[feature[nbr_l]], 0.25)
	if (nbr == -1):  # Indentation correcte
		print("Invalid value", end ="")
		for i in range(15 - len("Invalid value")):
			print(" ", end="")
		return
	print(f"{nbr:.2f}", end="")  # Affiche la moyenne avec 2 décimales
	for i in range(15 - len(f"{nbr:.2f}")):
		print(" ", end="")

def print50(data, feature, nbr_l):
	nbr = percentile(data[feature[nbr_l]], 0.5)
	if (nbr == -1):  # Indentation correcte
		print("Invalid value", end ="")
		for i in range(14 - len("Invalid value")):
			print(" ", end="")
		return
	print(f"{nbr:.2f}", end="")  # Affiche la moyenne avec 2 décimales
	for i in range(14 - len(f"{nbr:.2f}")):
		print(" ", end="")

def print75(data, feature, nbr_l):
	nbr = percentile(data[feature[nbr_l]], 0.75)
	if (nbr == -1):  # Indentation correcte
		print("Invalid value", end ="")
		for i in range(15 - len("Invalid value")):
			print(" ", end="")
		return
	print(f"{nbr:.2f}", end="")  # Affiche la moyenne avec 2 décimales
	for i in range(15 - len(f"{nbr:.2f}")):
		print(" ", end="")

def printmax(data, feature, nbr_l):
	nbr = valeur_maximale(data[feature[nbr_l]])
	if (nbr == -1):  # Indentation correcte
		print("Invalid value", end ="")
		for i in range(14 - len("Invalid value")):
			print(" ", end="")
		return
	print(f"{nbr:.2f}", end="")  # Affiche la moyenne avec 2 décimales
	for i in range(14 - len(f"{nbr:.2f}")):
		print(" ", end="")