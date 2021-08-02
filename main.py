#tri_a_bulle\Bubble_sort
#Complexité en temps: au mieux O(n), en moyenne et au pire : O(n²)
#Complexité en espace: Au pire O(1)
#Entrée : A, une liste
#Sortie : A dans l'ordre croissant


def echange(L, i, j):  #Echange L[i] avec L[j]
	L[i], L[j] = L[j], L[i]
	return (L)


def est_trie(T):
	for i in range(len(T) + 1):
		if (T[i - 1] > T[i]):
			return False


def bubblesort(T):
	n = len(T) + 1
	for i in range(n):
		for j in range(i):
			if (T[n - j - 1] > T[n - j]):
				echange(T, n - (j), n - j + 1)
	return (T)


A = [6, 5, 3, 1, 8, 7, 2, 4]
while est_trie(A) == False:
	bubblesort(A)
print(A)
