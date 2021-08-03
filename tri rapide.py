#Tri rapide / Quicksort
#Complexité en temps: Au mieux O(n log n), En moyenne O(n log n) Au pire O(n²)
#complexité en espace : En moyenne O(log n), Au pire O(n)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

import random

def quicksort(a):
	if len(a)<=1: 
	    return a 

	smaller,equal,larger=[],[],[]
	pivot=a[random.randint(0,len(a)-1)]

	for x in a:
		if x<pivot:
		    smaller.append(x)
		elif x==pivot:
		    equal.append(x)
		else:
		    larger.append(x)

	return quicksort(smaller)+equal+quicksort(larger)


#just for testing
a = [6, 4, 2, 1, 3, 5]
print(quicksort(a))
