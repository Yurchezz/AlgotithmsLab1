from models.Laptop import Laptop
from managers.Insersion import insertion
from managers.Merge import merge


def main():
    laptops = [
        Laptop(2.8, "Lenovo", 4),
        Laptop(3.6, "MSI", 16),
        Laptop(3.1, "Razer", 8)
    ]

    insersionParams = insertion(
        laptops,
        insertionCompareCounter=0,
        insertionSwapCounter=0
    )

    print("\n"
          "Sorted with insertion method by RAM Volume"
          )
    for i in range(0, len(laptops)):
        laptops[i].show()
    print(
        "Insertion: Compares: "
        + str(insersionParams[0])
        + "\tSwaps: "
        + str(insersionParams[1])
    )

    mergeParams = merge(
        laptops,
        mergeCompareCounter=0,
        mergeSwapCounter=0
    )
    print("\n"
          "Sorted with merge method by CPU speed"
          )
    for i in range(0, len(laptops)):
        laptops[i].show()
    print(
        "Merge: Compares: "
        + str(mergeParams[0])
        + "\tSwaps: "
        + str(mergeParams[1])
    )


if __name__ == '__main__':
    main()
