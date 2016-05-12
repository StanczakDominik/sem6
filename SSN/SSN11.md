# SSN 16.05.12
## Multilayer Perceptron
1. Warstwa neuronów wejściowych (tu podajemy sygnał $\vec{x}$
2. Neurony wewnętrzne (ukryte)
3. Warstwa neuronów wyjściowych (często mniej niż na wejściu). Każdy odpowiada np. czy wykryto wino nr 1, wino nr 2... Można oznaczyć jako wektor wyjściowy $\vec{y} = \vec{d}$

Kierunek propagacji sygnału jest oczywiście od wejścia do wyjścia
Rysunek: cztery warstwy łącznie, strzałeczki między kolejnymi

### Jak zaprojektować perceptron:
Ustalamy:
* liczbę neuronów w wejściu
* liczbę neuronów w wyjściu
* liczbę warstw obliczeniowych
* liczbę neuronów w poszczególnych warstwach obliczeniowych
* połączenia synaptyczne między warstwami (**backpropagation!**)

> Liczba - obiekty przeliczalne, ilość - nieprzeliczalne (np. woda)

### Jak nałóczyć Perceptron
Mamy zbiór tupli uczących ${(\vec{X}, \vec{d})}$: np. obrazek i string "autobus", obrazek i string "kot"

Przez backpropagation tworzymy (powolny proces) macierz połączeń synaptycznych J (**oznaczana często jako W**)

**Perceptrony generalizują**, ale nie muszą zwracać - oczywiście - dobrych odpowiedzi

<img href="rys1.png">

### Funkcja energetyczna
$$ E = 0.5 \sum_{k=1}^M (y_k - d_k)^2$$
$y_k$ - co faktycznie mamy w $k$-tym neuronie
$d_k$ - co mamy w $k$-tym neuronie dla danego wzorca
$M$ - liczba neuronów na wyjściu

Zjeżdżamy z energią do 0 (norma jest dodatnia)

### Backpropagation

$$\Delta W = - \eta \nabla E(W)$$
$\eta$ - stała uczenia

Więc to generalnie jest algo optymalizacyjny E :D

$\Delta W$ jest zmianą wektorą macierzy W w danym rzędzie! Dlatego to się zgadza:

### Powtórka z matematyki

$$f(y(x))$$
$$df/dx = df/dy \cdot dy/dx$$

### Wzory

P - pary uczące, M - neurony na wyjściu

$$E(W) = 0.5 \sum_p^P \sum_m^M (y_m^p - d_m^p)^2$$

oznaczmy stan i-tej warstwy przez $\vec{v_i}$

f - funkcja aktywacji

$$\vec{v_i} = f(\sum_n^N \hat{W} \vec{v_{}})$$

Poruszamy się od wyjścia do wejścia (czy to czasami nie jest trochę iteracyjne odwracanie tej macierzy...?)

1. Analiza sieci przy zwykłym przepływie sygnału (z wejścia do wyjścia)
2. Odwrócenie kierunku postępowania : idziemy od wyjścia do wejścia, obliczamy poprawki do kolejnych wektorów w macierzy połączeń synaptycznych

$$W_{ij}^{(1)} (t+1) = W_{ij}^{(1)} + \Delta W_{ij}^{(1)}$$

3. Powtarzamy tak dla kadego wzorca
4. Powtarzamy all powyższe, aż energia dla KAŻDEGO wzorca będzie $\le \epsilon$
5. Cieszymy się perceptronem

### Zastosowania
* Identyfikacja związków chemicznych (detekcja czy się wydzieliła odpowiednia ilość związków chemicznych, bo wtedy mogą przereagować i kogoś zabić). Perceptron: na wejściu stężenia wszystkich możliwych w fabryce związków, na wyjściu: ryzyko zatrucia wynikami
* Identyfikacja rodzaju i rocznika wina (bardzo subtelne różnice!). Działało dla 80 rodzajów win (12 sensorów na wejściu, 5 diodek (binarnych - czy dany rodzaj wina) na wyjściu, 5 warst wewnętrznych). 75% trafienia w 112000 iteracjach.
* Dobieranie składu mieszanki w samochodzie żeby zoptymalizować moc silnika
* Identyfikacja autobusu wśród mgieł
* CERN: identyfikacja konkretnej cząstki po torach (43, 22, 1 - 43 wejścia, 22 warstwy wewnętrzne, 1 "czy znaleźliśmy Higsa?")

### Potencjalne pytania
* Jak przygotować materiał do uczenia perceptronu (przygotować dane w formie dużej liczby par $(\vec(X), \vec(d))$, odpowiednie liczby wymiarów tego wektora)
* Jak zaprojektować perceptron?
* Jak działa uczenie perceptronu? (wzór z małą deltą!)
* Zastosowania perceptronu
* Struktura perceptronu: rysunek
* Kiedy się używa perceptronów zamiast innych sieci (jeszcze się to pewnie pojawi na wykładzie)
* 
