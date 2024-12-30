import math

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

def is_number(value):
    try:
        float(value)  # Essaye de convertir en float
        return True
    except ValueError:
        return False

def moyenne(tab):
    valid_values = [float(i) for i in tab if is_number(i) and i != ""]  # Filtrer les valeurs valides
    if not valid_values:
        return -1  # Retourne 0 si aucune valeur valide
    return sum(valid_values) / len(valid_values)

def ecart_type(tab):
    """
    Calcule l'écart type des valeurs numériques dans une liste.
    Ignore les valeurs non valides ou vides.

    Args:
        tab (list): Liste de valeurs.

    Returns:
        float: Écart type des valeurs si possible, sinon -1.
    """
    valid_values = [float(i) for i in tab if is_number(i) and i != ""]
    
    if not valid_values:
        return -1  # Aucun calcul possible
    
    moyenne_val = sum(valid_values) / len(valid_values)
    variance = sum((x - moyenne_val) ** 2 for x in valid_values) / len(valid_values)
    return math.sqrt(variance)

def valeur_minimale(tab):
    valid_values = [float(i) for i in tab if is_number(i) and i != ""]
    if not valid_values:
        return -1
    return min(valid_values)

def percentile(tab, nbr):
	valid_values = sorted([float(i) for i in tab if is_number(i) and i != ""])
	if not valid_values:
		return -1
	if (nbr == 0.25):
		index = int(0.25 * len(valid_values))
	elif (nbr == 0.5):
		index = int(0.5 * len(valid_values))
	elif (nbr == 0.75):
		index = int(0.75 * len(valid_values))
	return valid_values[index]

def valeur_maximale(tab):
    valid_values = [float(i) for i in tab if is_number(i) and i != ""]
    if not valid_values:
        return -1
    return max(valid_values)