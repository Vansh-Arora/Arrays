
def getMinMax( a, n):
    mi_ma = [a[0],a[0]]
    for i in a:
        if i < mi_ma[1]:
            mi_ma[1] = i
        if i > mi_ma[0]:
            mi_ma[0] = i
    return mi_ma