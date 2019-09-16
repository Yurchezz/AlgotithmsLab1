def merge(laptops, mergeCompareCounter=0, mergeSwapCounter=0):
    if len(laptops) > 1:
        mergeCompareCounter += 1
        mid = len(laptops) // 2
        L = laptops[:mid]
        R = laptops[mid:]

        merge(L)
        merge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):

            if L[i].speed < R[j].speed:
                mergeCompareCounter += 1
                laptops[k] = L[i]
                i += 1
                mergeSwapCounter += 1
            else:
                laptops[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            laptops[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            laptops[k] = R[j]
            j += 1
            k += 1

    return mergeCompareCounter, mergeSwapCounter
