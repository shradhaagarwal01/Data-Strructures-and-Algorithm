def commonElements (A, B, C, n1, n2, n3):
        a = list(set(A) & set(B) & set(C)) 
        a.sort()
        return a