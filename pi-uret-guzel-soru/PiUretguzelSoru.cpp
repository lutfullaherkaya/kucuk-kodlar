/* Problem:
 * 0 ve 1 arasinda rastgele sayi ureten fonksiyon var elinizde.
 * Bu fonksiyonu kullanarak pi'yi hesaplayiniz.
 */







/* Kendi cozumum:
 * Cember fonksiyonunu kullanarak 0 ve 1 arasindaki sayilarla 
 * ceyrek cember uretebiliriz.
 * Birim cember fonksiyonu: x^2 + y^2 = 1 => y = 1 - x^2
 * Tek yapmamiz gereken bu noktalari uretmek ve x e gore siralayip
 * cemberi olusturmak. Bu ceyrek cemberin cevresi pi'nin yarisidir.
 * Bu cevreyi de ardisik noktalar arasindaki uzakliklari toplayarak bulabiliriz.
 * Tabii ki olusturdugumuz geometrik sekil n kenarli cokgendir,
 * gercek bir cember degildir cunku sonsuz tane nokta uretemeyiz.
 * Ama hayatta ne gercek ki cember gercek olsun?
 */
#include <iostream>
#include <stdlib.h> // rand icin
#include <cstdlib> // RAND_MAX icin
#include <utility> // pair icin
#include <algorithm> // sort icin
#include <math.h>
#include <vector>

typedef std::pair<double, double> Nokta;

double rastgele0ve1arasiSayi() {
    // rand tam sayi uydurdugu icin...
    return (double)rand()/(double)RAND_MAX;
}

double ikiNoktaArasiUzaklik(Nokta A, Nokta B) {
    return sqrt(pow(B.first-A.first, 2) + pow(B.second-A.second, 2));
}

/* nokta sayisini artirdikca pi'ye daha cok yaklasiriz
 * lakin double de bir yere kadar gosterebilir pi'yi.
 * 123456 ozel sayisinin double'nin pi'yi gosterebilecegi kadar 
 * gostermesi icin mukemmel bir sayidir. 12345 sayisi denenirse 
 * olmaz. 1234567 denenirse hesaplamasi cok uzun surer.
 * en buyuk int olan 2^31-1 = 2147483647(2gb)'i girersek de
 * bir Nokta 16 bayt oldugu icin 32 gb ram gerekir
 * tum noktalari vektore ekleyebilmek icin.
 */
double piYap(int olusturulacakNoktaSayisi=12345) {
    std::vector<Nokta> ceyrekCemberNoktalari;
    for (int i = 0; i < olusturulacakNoktaSayisi; ++i) {
        double x = rastgele0ve1arasiSayi();
        ceyrekCemberNoktalari.push_back(Nokta(x, sqrt(1-x*x)));
    }

    // Nokta.first'e gore, yani x'e gore siralama
    sort(ceyrekCemberNoktalari.begin(), ceyrekCemberNoktalari.end());

    double piNinYarisi = 0;
    for (int i = 0; i < olusturulacakNoktaSayisi - 1; ++i) {
        piNinYarisi += ikiNoktaArasiUzaklik(
            ceyrekCemberNoktalari[i],
            ceyrekCemberNoktalari[i+1]);
    }

    return piNinYarisi * 2;
}

int main() {
    std::cout << "pi sayisi = " << piYap() << std::endl;;
    return 0;
}