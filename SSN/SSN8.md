# Sieci 28.04.16

### Teoria pola średniego dla szt. sieci neuronowej
$$<s_i> = \tanh(\beta h_i)$$

Wyodrębniamy neuron i opisujemy wpływ od jego sąsiadów pole średnie (*dressed test particle*, trochę jak.

Równanie uwikłane -> przekształcenia -> czynnik proporcjonalny do liczby wzorców - pole zewnętrzne $h^{\text{ext}}$. Osłabia pole zewnętrzne. Gdyby nie czynnik $1/N$, mielibyśmy kichę.

Zakładamy po drodze że średnie pole $J_{ij} = J/N$

Czyli jak na FSiT szukamy pierwiastków równania nieliniowego

Ćwierćkolisty wykres $<S>(T)$ z wypłaszczeniem po lewej na górze, temperatura krytyczna. W temperaturze krytycznej $T_c$ sieć niczego nie pamięta, cała dynamika układu jest stochastyczna, brak korelacji historycznej. Ising, no. :)

### MEAN FIELD EQUATIONS:
Wnioski z powyższego. $\alpha$ - zapełnienie, średnia liczba wzorców $P_c/N$
$$<m> = \frac{1}{P} \sum_{\mu=1}^P <m^\mu> >$$
Analogiczny ćwierćkolisty wykres z płaskim etapem:

Sypią się **wszystkie** wzorce, nie tylko np. ostatni! Bo stochastycznie, Ising, szum temperaturowy!

### SIZE EFFECT

> Storage capacity of ANN

Dla dużych sieci, nieco powyżej $\alpha =0.138: 0.14$ duży peak histogramu overlapu do m = 1 (znalazł wzorzec)

Do mniejszych - pojawiają się atraktory pasożytnicze ale większość czasu spędza i tak w tym-tamtym

Dla $\alpha = 0.16$ dla dużej sieci może być gorzej niż dla małej! Histogram dla $N=3000$: dwa duże gaussy na m = 1 i m = 0.3

Dla tego samego $\alpha$ i $N=500$  - lepiej niż dla $N=3000$! ZONK!

Ogólnie: te sieci są często nieintuicyjne.

> Zdolności pamięciowe różnie zależą od rozmiaru sieci i od tego, w jaki sposób jest zrealizowana - kod, hardware... może mieć dobrą, słabą pojemność.

Generalnie chodzi o limity asymptotyczne algorytmów.
