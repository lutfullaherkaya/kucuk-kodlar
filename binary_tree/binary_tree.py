# Bu kodlar Python 2 ve Python 3 uyumludur.
# temel agac fonksiyonlari odtu ceng111 dersindendir.
# DIKKAT: herhangi bir dugumun degeri liste olamaz.
# Bu fonksiyonlari yazarken agaci grafik olarak gorememek bir sorun.
# Bu sorunu cozmek icin asagida print_binary_tree fonksiyonu tanimladim.
# Su sitede Binary Search Tree gorseli olusturabilirsiniz:
# https://www.cs.usfca.edu/~galles/visualization/BST.html
# Bu modulu indirip fonksiyonlari denemenizi oneririm.
# Hatta fonksiyonlari sadece okumak yerine
# fonksiyonun ne yaptigina bakip fonksiyonu kendiniz
# yazmanizi oneririm.

from copy import deepcopy


def datum(tree):
    return tree[0]


def bos_mu(tree):
    return tree == []

# leaf node ornegi: [4, [], []]
def isleaf(tree):
    return sol_agac(tree) == [] and sag_agac(tree) == []


# ornek agac: [deger, sol_agac, sag_agac]
def sol_agac(tree):
    if bos_mu(tree):
        return []
    return tree[1]


def sag_agac(tree):
    if bos_mu(tree):
        return []
    return tree[2]


def dugumOlustur(datum, sol_agac=None, sag_agac=None):
    return [datum, sol_agac if sol_agac else [], sag_agac if sag_agac else []]
# Burada direk dugumOlustur(datum, sol_agac=[], sag_agac=[]) dememek
# gerekiyor cunku oyle dersek, fonksiyonu her cagirdigimizda ayni
# bos listeyi kullanir fonksiyon. Her cagirista yeni bos liste
# olusturmaz. Su sitede daha fazla bilgi ve ornekler var:
# http://effbot.org/zone/default-values.htm



# Tree traversal; gezinme, dolasma demektir.
# Agactaki tum dugum degerlerine bakmaktir.
# Mesela preorder_traversal
# once roota, sonra sol alt agaca, sonra sag alt agaca bakar.
# inorder ve postorder traversallar da bunun farkli siralanmislaridir.
# Su videoyu izleyebilirsiniz gormek icin:
# https://youtu.be/TMEa6E-KBW8?t=25
# not bos_mu(tree) dedigimiz icin recursive fonksiyonumuz
# bir yerden sonra daha derine inmeyi birakiyor, yukari cikiyor.
def preorder_traversal(tree):
    if not bos_mu(tree):
        print(datum(tree))
        preorder_traversal(sol_agac(tree))
        preorder_traversal(sag_agac(tree))


def inorder_traversal(tree):
    if not bos_mu(tree):
        inorder_traversal(sol_agac(tree))
        print(datum(tree))
        inorder_traversal(sag_agac(tree))


def postorder_traversal(tree):
    if not bos_mu(tree):
        postorder_traversal(sol_agac(tree))
        postorder_traversal(sag_agac(tree))
        print(datum(tree))


# Breadth First Traversal (Enine Gezinme) agacin en ust
# seviyesinden baslar ve seviye seviye gezinir.
# Mesela agacimiz  [1, [2, [3, [], []], []], [4, [], []]] ise
# breadth first traversal soyle olur: [1, 2, 4, 3]
# print_binary_tree([1, [2, [3, [], []], []], [4, [], []]]) fonksiyonu
# ile agaci rahatca gorebilirsiniz.
# Asagidaki fonksiyon queue veri tipinin kullanisli bir ornegi.
def breadth_first_traversal(tree):
    queue = deepcopy(tree)
    sonuc = []
    while len(queue) > 0:
        if type(queue[0]) != list:
            sonuc.append(queue.pop(0))
        else:
            queue.extend(queue.pop(0))
    return sonuc


# Mesela bir dugumlu agacin yuksekligi 1'dir.
# Bu fonksiyon agacin recursive ozelligini kullaniyor.
# Bir agacin yuksekligi, kollarindaki en uzun agacin
# yuksekliginin bir fazlasidir.
def height(tree):
    if bos_mu(tree):
        return 0
    return 1 + max(height(sol_agac(tree)), height(sag_agac(tree)))


# bir agacin balanced olmasi icin tum 
# leaf node ikililerinin derinlik farki en fazla 1 olmalidir.
# Bu fonksiyon leaf'lerin derinliklerini listeler,
# listenin acikligini bulur. Aciklik 1 den buyuk mu ona bakar.
def isBalanced(tree):
    depths_of_leaf_nodes = []
    def leaf_node_depths(tree, depth=0):
        if not bos_mu(tree):
            if isleaf(tree):
                depths_of_leaf_nodes.append(depth)
            leaf_node_depths(sol_agac(tree), depth+1)
            leaf_node_depths(sag_agac(tree), depth+1)
    leaf_node_depths(tree)
    return max(depths_of_leaf_nodes) - min(depths_of_leaf_nodes) <= 1


# Asagidaki fonksiyon pre-order traversal ile
# buldugu degerlerin derinliklerini yazdirir.
# Fonksiyon basit ama kotu kismi
# dugum derinligini yazdirdiktan sonra agaci gezinmeye
# devam etmesidir. Derinligi bulduktan sonra bir sekilde
# tum ic ice cagirilan fonksiyonlardan cikilmasi lazim.
# Iki asagidaki fonksiyon bunu yapiyor ama biraz karisik gibi.
def dugum_derinligi_bul_print(tree, value, depth=0):
    if not bos_mu(tree):
        if datum(tree) == value:
            print(depth)
        dugum_derinligi_bul_print(sol_agac(tree), value, depth+1)
        dugum_derinligi_bul_print(sag_agac(tree), value, depth+1)
        return -1

# -1 donmesi demek dum degerleri traverse etti ama aranan
# degeri hic bulamadi demek. Degeri buldugunda ise her
# zaman -1'den buyuk olan depth degerini donuyor,
# yani aramayi birakip agacta yukari cikmaya basliyor.
def dugum_derinligi_bul(tree, value, depth=0):
    if not bos_mu(tree):
        if datum(tree) == value:
            return depth
        sol = dugum_derinligi_bul(sol_agac(tree), value, depth+1)
        if sol > -1: return sol
        sag = dugum_derinligi_bul(sag_agac(tree), value, depth+1)
        if sag > -1: return sag
        return -1


# Agactaki bir derinlik seviyesinin genisligi (width),
# o seviyedeki dugum sayisidir. Yani derinligi ayni
# olan dugum sayisidir. Bir agacin genisligi ise (width),
# genisligi en buyuk olan seviyenin genisligidir.
def width_list(tree):
    her_bir_derinlikteki_dugum_sayilari = height(tree) * [0]
    def listeye_ekle(tree, derinlik=0):
        if not bos_mu(tree):
            her_bir_derinlikteki_dugum_sayilari[derinlik] += 1
            listeye_ekle(sol_agac(tree), derinlik+1)
            listeye_ekle(sag_agac(tree), derinlik+1)
    listeye_ekle(tree)
    return her_bir_derinlikteki_dugum_sayilari

def width(tree):
    return max(width_list(tree))

# Her bir dugum degeri ikiye bolunur, yeni degerler children node olur.
# Eger dugum degeri tek sayiysa, mesela 5 ise yeni dugumler 2 ve 3 olur.
def ikiye_bolme_agaci_olustur(n):
    if n == 1:
        return dugumOlustur(1)
    elif n % 2 == 0:
        tree = dugumOlustur(n, ikiye_bolme_agaci_olustur(n/2),
                               ikiye_bolme_agaci_olustur(n/2))
    else:
        tree = dugumOlustur(n, ikiye_bolme_agaci_olustur((n-1)/2+1),
                               ikiye_bolme_agaci_olustur((n-1)/2))
    return tree


# Buradan sonraki fonksiyonlar agaci print edebilmek icin yazilmistir.

# Agacin seviyelerini listeler. Mesela
# derinlige_gore_listele([1, [2, [], []], [3, [4, [], []], []]])
# sonucu [[1], [2, 3], [4]] olur. Bu fonksiyon agaci yazdirma
# fonksiyonunda ise yarayacak.
def derinlige_gore_listele(tree):
    breadth_first_duzlenmis_liste = breadth_first_traversal(tree)
    kat_listesi = []
    for width in width_list(tree):
        bir_kat = []
        for _ in range(width):
            bir_kat.append(breadth_first_duzlenmis_liste.pop(0))
        kat_listesi.append(bir_kat)
    return kat_listesi


# Istenen yukseklikte, her dugumunde deger bulunan agac olusturur.
# Mesela agac_piramidi_olustur(2, "a") sonucu:
# ["a", ["a", [], []], ["a", [], []]]
# dugumOlustur fonksiyonunun bu sekilde kullanimi ilginctir.
def agac_piramidi_olustur(yukseklik, deger=""):
    if yukseklik == 0:
        return []
    else:
        return dugumOlustur(deger,
                            agac_piramidi_olustur(yukseklik-1),
                            agac_piramidi_olustur(yukseklik-1))


# Agactaki bos yerleri doldurur ki print ederken kaymasin
# agacin dugumleri.
def agac_doldur(tree, tree_height, depth=0):
    if bos_mu(tree):
        tree += agac_piramidi_olustur(tree_height-depth)
    else:
        agac_doldur(sol_agac(tree),  tree_height, depth+1)
        agac_doldur(sag_agac(tree), tree_height, depth+1)
    return tree


# Fonksiyonun calisma prensibi surada:
# https://i.ibb.co/pnrHq7b/asd.png
def print_binary_tree(tree):
    yukseklik = height(tree)

    # Burada agacin bos yerlerini doldururuz, tam bir piramit gibi gozukur agac.
    # Sonra da bu piramidin dugumlerini derinliklerine gore listeleriz.
    agac_kat_listesi = derinlige_gore_listele(agac_doldur(deepcopy(tree), yukseklik))

    # en cok karakterli dugum degerinin genisligini bulma
    dugum_karakter_genisligi = 1
    for kat in range(yukseklik):
        for dugum in range(len(agac_kat_listesi[kat])):
            if len(str(agac_kat_listesi[kat][dugum])) > dugum_karakter_genisligi:
                dugum_karakter_genisligi = len(str(agac_kat_listesi[kat][dugum]))

    # tum dugumlerin karakter sayisini ayni yapan dongu
    for kat in range(yukseklik):
        for dugum in range(len(agac_kat_listesi[kat])):
            agac_kat_listesi[kat][dugum] = (str(agac_kat_listesi[kat][dugum])).center(dugum_karakter_genisligi)

    # taban_genisligi, agacin en alt katinin genisligidir
    agac_son_kat_dugum_sayisi = len(agac_kat_listesi[-1])
    taban_bosluk_sayisi = agac_son_kat_dugum_sayisi - 1
    taban_genisligi = dugum_karakter_genisligi * agac_son_kat_dugum_sayisi + taban_bosluk_sayisi
    for derinlik, kat in enumerate(agac_kat_listesi):
        h = yukseklik - derinlik
        hayalet_node_sayisi = 2**(h-1) - 1
        bosluk_sayisi = 2**(h-1)
        toplam_bosluk_sayisi = bosluk_sayisi + hayalet_node_sayisi * dugum_karakter_genisligi
        print((" "*toplam_bosluk_sayisi).join(map(str, kat)).center(taban_genisligi))

# Bu if kosulu sayesinde asagidaki bu modulun kendi acilinca acilir.
# Modul baska yere import edilirse calismaz.
if __name__ == "__main__":
    import binary_search_tree as bst
    print_binary_tree(ikiye_bolme_agaci_olustur(23))
    print("Agacin nested list hali: "+ str(ikiye_bolme_agaci_olustur(23)))
    print("Bu agacin dengeli olma durumu: " + str(isBalanced(ikiye_bolme_agaci_olustur(23))))

    tree2 = []
    bst.dugumler_ekle(tree2, [10,30,5,3,8,2,23,42,7,9,22,24,43,41,45,96,32])
    print_binary_tree(tree2)
    print("Agacin nested list hali: "+ str(tree2))
    print("Bu agacin dengeli olma durumu: " + str(isBalanced(tree2)))

    tree5 = []
    bst.dugumler_ekle(tree5, [100, 50, 150, 13, 26, 175, 200, 75, 6, 125, 165, 130, 115, 85, 65])
    print_binary_tree(tree5)
    print("Agacin nested list hali: "+ str(tree5))
    input("Cikmak icin bir sey yaziniz: ")
