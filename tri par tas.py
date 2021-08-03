#Tri par tas / heapsort
#Complexité en temps:Au mieux O(n), En moyenne O(n log n) Au pire O(n log n)
#Complexité en espace : Au pire O(1)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant

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
