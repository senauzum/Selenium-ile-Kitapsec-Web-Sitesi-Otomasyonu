# Selenium ile Kitapseç Web Sitesi Otomasyonu

## Proje Hakkında
Bu proje, Python ve Selenium WebDriver kullanılarak https://www.kitapsec.com/ web sitesi üzerinde geliştirilen bir UI test otomasyonunu içermektedir. 

---

## Senaryo Adı: Kitapseç Web Sitesi Üzerinden Ürün Arama ve Sepete Ekleme Senaryosu

Senaryo Adımları:
1. Kitapseç ana sayfasının açıldığının doğrulanması
2. Sayfanın tam ekran yapılması
2. Arama kutusuna ürün adı girilmesi
3. Arama işleminin başlatılması
4. Arama sonuçlarının listelendiğinin doğrulanması
3. Arama sonuçlarından bir ürün seçilmesi
4. Ürünün detay sayfasına gidilmesi
5. Sayfanın aşağıya doğru scroll edilmesi
4. Ürünün sepete eklenmesi
5. Sepete ekleme sonrası açılan popup/overlay'in kontrol edilmesi 
6. Sepet sayfasına yönlendirilmenin doğrulanması 
Not: Dinamik elementler için bekleme (wait) mekanizmalarının kullanılmıştır.

---

## Senaryo Adı: Kitapseç Web Sitesi Üzerinden Filtreleyerek Ürün Listeleme ve Sepete Ekleme Senaryosu

Senaryo Adımları:
1.	Kitapseç ana sayfasının açıldığının doğrulanması
2.	Sayfanın tam ekran yapılması
3.	Menülerden Çocuk Kitabı sekmesine tıklaması
4.	Çocuk kitabı menüsünün içinde Dünya Klasikleri'ne tıklanması
5.	Arama sonuçlarının listelendiğinin doğrulanması
6.	Sayfanın aşağıya doğru scroll edilmesi
7.	Filtreleme kısmındaki Yayıncı kısmından İş bankası Kültür Yayınları seçilmesi
8.	Sayfanın aşağıya doğru scroll edilmesi
9.	Fiyat filtresi kısmında Başlangıç Fiyatı'na tıklanması
10.	Fiyat listesinden 50 TL'nin tıklanması
11.	Fiyat filtresi kısmında Bitiş Fiyatı'na tıklanması
12.	Fiyat listesinden 100 TL'nin tıklanması
13.	Ara butonu ile arama işleminin başlatılması
14.	Arama sonuçlarının listelendiğinin doğrulanması
15.	Sayfanın aşağıya doğru scroll edilmesi
16.	Arama sonuçlarından bir ürün seçilmesi
17.	Sayfanın aşağıya doğru scroll edilmesi
18.	Ürünün detay sayfasına gidilmesi
19.	Sayfanın aşağıya doğru scroll edilmesi
20.	Ürün adetinin sayısının artırılarak 2 yapılması
21.	Ürünün sepete eklenme

---

## Kullanılan Teknolojiler/Araçlar
- Python 3.13.1
- Selenium WebDriver
- Google Chrome
- chromedriver-autoinstaller
- Visual Studio Code
