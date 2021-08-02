#Tri par insertion
#Complexité en temps: Au mieux O(n), En moyenne O(n²) Au pire O(n²)
#complexité en espace : O(1)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

def bubblesort(L):
    for x in range(0, len(L) -1):
        for y in range(0, len(L) -1 -x):
            if L[y] > L[y+1]:
                L[y], L[y+1] = L[y+1], L[y]
    return L
  
A = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubblesort(A))
