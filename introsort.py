#Introsort
#Complexité en temps:En moyenne O(n log n) Au pire O(n log n)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

import random
import math

def heap(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[i] < A[l]:
        largest = l
    if r < n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heap(A, n, largest)
  
  
def heapsort(A):
    n = len(A)
    for i in range(n//2, -1, -1):
        heap(A, n, i)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heap(A, i, 0)
    return A
  
#Just for testing
A = [1, 25436, 12, 24, 6, 2]
print(heapsort(A))
	



def sort(A):
    maxdepth = math.floor(math.log(len(A)) * 2)
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
print(sort(a))
