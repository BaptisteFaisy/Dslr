def arrondir(nbr):

	i = 0
	while (len(nbr) > 20):
		round(nbr, i)
		i+=1
	return str1

def conter(tab):
	j = 0
	for i in tab:
		if (i != ""):
			j+= 1
	return j

def moyenne(tab):
	j = 0
	nbr = 0
	for i in tab:
		if (i.isdigit() == 0):
			return(-1)
		else:
			nbr += int(i)
	return (nbr / conter(tab))