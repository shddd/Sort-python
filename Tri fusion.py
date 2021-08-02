#Tri fusion / Merge sort 
#Complexité en temps: quelque soit le cas O(n log n)
#Complexité en espace: Au mieux (1), Au pire O(n)
#Entrée : A, B, deux listes
#Sortie : A+B, une liste dans l'ordre croissant des termes de A et B

def fusion(l1, l2):
    i1 = 0
    i2 = 0
    f = []
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] <= l2[i2]:
            f.append(l1[i1])
            i1 = i1 + 1
        else:
            f.append(l2[i2])
            i2 = i2 + 1
    while i1 < len(l1):
        f.append(l1[i1])
        i1 = i1 + 1
    while i2 < len(l2):
        f.append(l2[i2])
        i2 = i2 + 1
    return f

def tri_fusion(l):
    longueur = len(l)
    if longueur>1:
        milieu = longueur // 2
        return fusion(tri_fusion(l[:milieu]), tri_fusion(l[milieu:]))
    else:
        t = l
    return t

print(fusion(A, B))
