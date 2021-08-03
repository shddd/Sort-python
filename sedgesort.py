#Segdesort
#Variante du tri rapide
#Complexité en temps: Au mieux O(n log n), En moyenne O(n log n) Au pire O(n²)
#complexité en espace : En moyenne O(log n), Au pire O(n)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

import random

def insort(A):
  a = len(A)
  for j in range(1, a):
    key = A[j]
    i = j-1
    while (i> 0 and A[i] > key):
      A[i+1] = A[i]
      i = i-1
    A[i + 1] = key
  for j in range(1, a):
    if (A[0] >A[j-1] and A[0]<A[j]):
      A.insert(A[0] , j)
      A.pop(0)
      break
  return A


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

	return insort(smaller)+equal+insort(larger)


#just for testing
a = [6, 4, 2, 1, 3, 5]
print(quicksort(a))
