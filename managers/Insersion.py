from models.Laptop import Laptop


def insertion(laptops, insertionCompareCounter, insertionSwapCounter):

    for i in range(1, len(laptops)):

        key = laptops[i].ramVolume

        j = i - 1
        while j >= 0 and key < laptops[j].ramVolume:
            insertionCompareCounter += 2
            insertionSwapCounter += 1
            laptops[j+1].ramVolume = laptops[j].ramVolume
            j -= 1
            laptops[j+1].ramVolume = key

    return insertionCompareCounter, insertionSwapCounter
