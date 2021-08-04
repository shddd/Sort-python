#Tri de Shell / Shell sort
#Complexité en temps : Au mieux O(n log² n), Au pire O(n²)
#Complexité en espace : Au pire O(1)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

def Shellsort(A):
    n = len(A)
    j = 0
    temp = 0
    E = [701, 301, 132, 57, 23, 10, 4, 1]
    for e in E:
        for i in range (e, n):
            temp = A[i]
            j = i
            while ((j >= e) and (A[j-e] > temp)):
                A[j] = A[j-e]
                j = j-e
                A[j] = temp
    return A

#Just for testing
A = [125, 142, 12, 11, 24, 2, 1]
print(Shellsort(A))
