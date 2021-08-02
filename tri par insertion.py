#Tri par insertion
#Complexité en temps: Au mieux O(n), En moyenne O(n²) Au pire O(n²)
#complexité en espace : O(1)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

def echange(L, i, j): #Echange L[i] avec L[j]
    L[i],L[j]=L[j],L[i]
    return (L)

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
