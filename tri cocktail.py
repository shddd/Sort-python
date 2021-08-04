#Tri cocktail / Cocktail sort
#Complexité en temps : Au mieux O(n), En moyenne O(n²), Au pire O(n²)
#Complexité en espace : Au pire O(1)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

def cocktailsort(A):
    for k in range(len(A)-1, 0, -1):
        ech = False
        for i in range(k, 0, -1):
            if A[i]<A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                ech = True

        for i in range(k):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                ech = True
      
        if not ech:
            return A

#Just for testing
A = [125, 142, 12, 11, 24, 2, 1]
print(cocktailsort(A))
