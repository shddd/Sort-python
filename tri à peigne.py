#Tri à peigne / comb sort
#Complexité en temps : Au mieux O(n log n), Au pire O(n²)
#Complexité en espace : Au pire O(1)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

def comb(A):
    n= len(A)
    echange = False
    while ((n > 1) or (echange == True)):
        n = int(n / 1.3)
        if (n < 1):
            n = 1
        i = 0
        echange = False
        while (i < len(A) - n):
            if(A[i] > A[i+n]):
                A[i], A[i+n] = A[i+n], A[i]
                echange = True
            i = i+1
    return A

#Just for testing
A = [125, 142, 12, 11, 24, 2, 1]
print(comb(A))
