#Tri rapide / Quicksort
#Complexité en temps: Au mieux O(n log n), En moyenne O(n log n) Au pire O(n²)
#complexité en espace : En moyenne O(log n), Au pire O(n)
#Entrée : une liste A
#Sortie : A classée dans l'ordre croissant
  
def partition(a, l, r): #dependant quickselect
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def kthlargest(a, k): #quickselect
    l = 0
    r = len(a) - 1
    split_point = partition(a, l, r) #choosing a pivot and saving its index
    if split_point == r - k + 1: #if the choosen pivot is the correct elemnt, then return it
        result = a[split_point]
    elif split_point > r - k + 1: #if the element we are looking for is in the left part to the pivot then call 'kthlargest' on that part after modifing k
        result = kthlargest(a[:split_point], k - (r - split_point + 1))
    else: #if the element we are looking for is in the left part to the pivot then call 'kthlargest' on that part
        result = kthlargest(a[split_point + 1:r + 1], k)
    return result

def quicksort(L): #tri rapide en lui-même
	


#just for testing
a = [6, 4, 2, 1, 3, 5]
print(kthlargest(a, 4))
