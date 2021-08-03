#Introsort
#Complexité en temps:En moyenne O(n log n) Au pire O(n log n)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

import random
import math

def heapsort(A):
	



def sort(A):
    maxdepth = floor(log(len(A)) * 2)
    return introsort(A, maxdepth)

def introsort(A, maxdepth):
	n = len(A)
	if n <= 1:
	    return A
    elif (maxdepth == 0):
        heapsort(A)
    else :
        p = random.randint(0, len(A))
        introsort(A[0:p-1], maxdepth -1)
        introsort(A[p+1:n], maxdepth -1)


#just for testing
a = [6, 4, 2, 1, 3, 5]
print(introsort(a))
