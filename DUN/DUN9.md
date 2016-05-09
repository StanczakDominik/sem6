# DUN 2016.05.05

Skończyliśmy na oscylatorach liniowych, nieliniowych.

### **odwzorowanie okręgu**
Inna klasa zjawisk mocno związanych, od strony dyskretnych odwzorowań.
Quasiperiodyczność - niewspółmierne częstotliwości (nie omega, 2 omega, 3 omega...) - niewymierne stosunki częstotliwości


*Oscylator (anharmoniczny) Duffinga* z harmoniczną siłą napędzającą
$$\ddot{\theta} + a \dot{\theta} + a \theta \big(\theta^2-1\big) = B \cos(t)$$
Można to przedstawić jako sprzężony Duffing z harmonicznym, oscylującym jako $B\cos(t)$. Zazwyczaj zakładamy że prawa strona nie ma wpływu na lewą; tutaj zrobimy inaczej.

> Można tym modelować komórki mięśnia sercowego.

Rozbicie na dwuwymiarowe odwzorowanie, układ dwóch równań na $\theta_{n+1}, \omega_{n+1}$. $\omega$ to częstość chwilowa.

Zjawisko jest nieokresowe i częstość (1/okres) jest zmienna.

Po zaniku początkowych transientów $\omega_n$ jest funkcją tylko $\theta_n$.

### Odwzorowanie okręgu

### Odwzorowanie standardowe

$$\theta_{n+1} = \Big(\theta_n + \Omega - \frac{K}{2\pi} \sin(2\pi\theta_n)\Big) \text{mod } 1$$

Dla liniowego $K=0$, wtedy dwie linie proste o nachyleniu 1 oddalone od $y=x$. Trajektoria zamyka się. Wymierne ułamki jako omega: trajektorie zamknięte. $\omega = p/q$, mają związek z liczbą przecięć krzywych i prostej.

Po włączeniu nieliniowości: nieliniowe wygięte krzywe. Klawisz F4 czyści w `circle.exe` historię. Dostajemy tą samą stabilną trajektorię.

### Drgania synfazowe i mode locking

Winding number: średnia zmiana fazy na iterację. Dla $K=0$ stała, częstość kołowa. Dla

Średnia zmiana fazy: $\lim_{n \to \infty} \frac{\theta_n-\theta_0}{n}$ gdzie faza *nie jest ograniczona modulo*

*Jęzory Arnolda - rejony dla odwzorowania standardowego* gdzie średnia zmiana fazy jest stała

Cała zabawa z programami i Dynamics Solverem. Jest co kodzić. `:>`

### Drogi do chaosu dla odwzorowania okręgu

Intermitencja TEŻ jest sposobem dojścia do chaosu - od okna periodycznego w głąb chaosu
