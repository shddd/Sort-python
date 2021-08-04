#Tri par selection / Selection sort
#Complexité en temps : Au mieux O(n²), En moyenne O(n²), Au pire O(n²)
#Complexité en espace : Au pire O(1)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

def selsort(A):
    n = len(A)
    m = 0
    for i in range(0, n):
        m = i
        for j in range((i+1), n):
            if (A[j] < A[m]):
                m = j
            if (m != i):
                A[i], A[m] = A[m], A[i]
    return A
    
    
#Just for testing
A = [125, 142, 12, 11, 24, 2, 1]
print(selsort(A))
