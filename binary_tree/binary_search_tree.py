import binary_tree as bt


# Binary Search Tree'nin ozelligi her bir dugumun sag kolunun
# kendinden buyuk, sol kolunun kendinden kucuk olmasidir.
def dugum_ekle(tree, value):
    if bt.bos_mu(tree):
        tree += bt.dugumOlustur(value)
    elif value < bt.datum(tree):
        dugum_ekle(bt.sol_agac(tree), value)
    elif value > bt.datum(tree):
        dugum_ekle(bt.sag_agac(tree), value)


def dugumler_ekle(tree, values):
    for value in values:
        dugum_ekle(tree, value)

def agac_binary_search_tree_mi(tree):
    if not bt.bos_mu(tree):
        if bt.isleaf(tree):
            return True
        if not bt.bos_mu(bt.sol_agac(tree)) and bt.datum(bt.sol_agac(tree)) >= bt.datum(tree):
            return False
        if not bt.bos_mu(bt.sag_agac(tree)) and bt.datum(bt.sag_agac(tree)) <= bt.datum(tree):
            return False
        return (agac_binary_search_tree_mi(bt.sol_agac(tree))
            and agac_binary_search_tree_mi(bt.sag_agac(tree)))
    return True # bunu yazmayinca bir ust satirda None and True diyordu, None donuyordu.


def agacta_deger_var_mi(tree, deger):
    if bt.bos_mu(tree):
        return False
    datum_tree = bt.datum(deger)
    if datum_tree == deger:
        return True
    elif datum_tree > deger:
        return agacta_deger_var_mi(bt.sol_agac(tree), deger)
    elif datum_tree < deger:
        return agacta_deger_var_mi(bt.sag_agac(tree), deger)


def dugum_derinligi_bul(tree, dugum_degeri, depth=0):
    if bt.bos_mu(tree):
        return -1
    datum_tree = bt.datum(tree)
    if datum_tree == dugum_degeri:
        return depth
    elif datum_tree > dugum_degeri:
        return dugum_derinligi_bul(bt.sol_agac(tree), dugum_degeri, depth+1)
    elif datum_tree < dugum_degeri:
        return dugum_derinligi_bul(bt.sag_agac(tree), dugum_degeri, depth+1)


def tree_max(tree):
    if bt.bos_mu(bt.sag_agac(tree)):
        return bt.datum(tree)
    return tree_max(bt.sag_agac(tree))


def tree_min(tree):
    if bt.bos_mu(bt.sol_agac(tree)):
        return bt.datum(tree)
    return tree_min(bt.sol_agac(tree))


if __name__ == "__main__":
    tree4 = []
    dugumler_ekle(tree4, [50,25,63,25,89,74,15,48,62,59,48,25,36,74,19,94,78,41,55,95,13,72])
    bt.print_binary_tree(tree4)
    print("Agacin nested list hali: "+ str(tree4))
    input("Cikmak icin bir sey yaziniz: ")
