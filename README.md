# Pseudo Random Number Generator
  Projede amaç sözde rastgele sayılar oluşturmaktır. Lehmer algoritması kullanılarak kullanılan değişken ve sabitlere asal sayılar atanmıştır. 
  Kullanılan sayıların rastgele sayı oluşturmayı ne şekilde etkilediği ve aralarında ne gibi bir ilişki ile değer atanması gerektiği incelenmiştir. Bu algoritmada kullanılan formül özyinelemeli olarak devam etmekte böylece istenen sayıda rastgele sayı üretilmeye devam etmektedir. 

### Gerçek Rastgele Sayı Üreteçleri (True-Random Number Generators TRNG)
Gerçek rastgele sayı üretimi için dış bir kaynaktan veri alana üreteçlerdir çünkü dış kaynaklar determinist değildir ve entropi daha fazladır. Sıcaklık, fare ve klavye hareketleri, saat bu üreteçler için kaynak olabilir.
### Sözde Rastgele Sayı Üreteçleri(Pseudo-Random Number Generators PRNG)
Rastgele sayı dizilerine yaklaşan sayı dizileri üreten üreteçlerdir. Bir başlangıç değeri yani tohum(seed) seçilerek, genelde gerçek bir rastgele sayı olarak seçilir, daha sonra bu tohuma tekrar tekrar uygulanan algoritma ile yeni rastgele sayılar üretilebilir. Basit algoritmalarla oluşturulan dizilerde periyodu da kısa olur. Kompleks algoritmalarla rastgeleliğin periyodu arttırılabilir.

Rastgele bir sayı üreticisinde olması gereken özellikler: 
1. Üretilen sayılar olabildiğince üniform yani kendini tekrarlamayan bir dağılıma sahip olmalıdır. 
2. Üretim hızlı olmalıdır.
3. Üretici program, bilgisayar belleğinde çok yer kaplamamalıdır. 
4. Üretici uzun bir periyoda sahip olmalıdır. 
5. Üretici, farklı bir dizi sayı da üretebilmeli veya bir dizi sayıyı yeniden üretebilmelidir. 
6. Yöntem sabit olarak sabit bir değer oluşturabilmek için bozulmamalıdır.
- matplotlib
- random (Seçilen ilk asal tohum için)
## Kodda Kullanılan Lehmer Algoritması:
<img src="https://github.com/simayhosmeyve/Pseudo_random_number_generator/blob/main/lehmer_algoritması.png"/>

## Kullanılan Teknolojiler:
<img  align="left" style="margin-left:0.5em" width="45px" src="https://img.icons8.com/color/48/000000/python--v1.png"/>



- matplotlib
- random (Seçilen ilk asal tohum için)
