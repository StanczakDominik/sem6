# 2016 04 15 kwanty - ćwiczenia


Na 7 ćwiczeniach kolokwium

### Rozpraszanie
Mamy potencjał sferyczny $V(r)$
$$f(\theta, phi) = -\frac{2\mu}{q\hbar^2} \int_0^{+\infty} dr*rsin(q\cdot r) V(r)$$
$$\vec{q} = \vec{k}-\vec{k'}$$
$$V(r) = \frac{2e^2}{r} exp(-\alpha r)$$

Przyda się całeczka:
$$\int \exp(ax) \sin(bx) dx = \frac{exp(ax)}{a^2+b^2}(a\sin(bx) -b\cos(bx))$$

Wtedy (bez granic)
$$f(\theta, \phi) = 2e^2*\frac{-2\mu}{q\hbar^2}\big(
    \frac{exp(-\alpha x)}{\alpha^2+q^2}(-\alpha\sin(qx) -q\cos(qx))
    \big)
$$
Podstawiając granice
$$f(\theta, \phi) = 2e^2*\frac{-2\mu}{\hbar^2}\big(
    \frac{1}{\alpha^2+q^2}
    \big)
$$

$$f(\theta, \phi) =
    \frac{-4e^2\mu}{\hbar^2}
    \frac{1}{\alpha^2+q^2}
$$
W granicy klasycznej $\alpha = 0$

$$f(\theta, \phi) = \frac{-4e^2\mu}{\hbar^2 q^2}
$$

(po drodze: $\mu = \frac{m_e m_p Z}{m_e + Z m_p} \sim m_e$)

$\exp(- \alpha x)$ - czynnik uzbieżniający. Trik matematyczny. Inny trik: regularyzacja Tofta:
$$\int d^4x -> \lim_{a->4} \int d^a x$$

Mamy wynik $f(\theta, \phi)$.

Kolejne założenie: rozpraszanie sprężyste $E_p = E_k$, bez konwersji energii na wzbudzenia wewnętrzne ("analog ciepła, tarcia"?).
$$E = \frac{(\hbar k)^2}{2m}$$
więc
$$|k| = |k'|$$

$$q^2 = k^2 + k'^2 - 2 |k| |k'| \cos(\theta) = 2k^2 (1-\cos(\theta)) = 4k^2 \sin^2(\theta/2)$$

Więc w tym przypadku dostajemy (w klasycznym przypadku) bardzo *fuzyjną* zależność
$$f(\theta, \phi) = \frac{-Ze^2}{4E \sin^2(\theta/2)}$$

Wracając do oryginalnego:
$$f(\theta, k) = \frac{-2m_eZe^2}{\hbar^2(\alpha^2+4k^2\sin^2(\theta/2))}$$

Różniczkowy przekrój czynny
$$\frac{d\sigma}{d\Omega} = |f(\theta)|^2 = \frac{4m_e^2Z^2e^4}{\hbar^4(\alpha^2+4k^2\sin^2(\theta/2))^2}
$$
Całkowity przekrój czynny
$$\sigma  = \int d\Omega \frac{d\sigma}{d\Omega}$$
Po $\psi$ od $0$ do $2\pi$, po $\theta$ od $0$ do $\pi$. Podstawienie $x = \cos(\theta)$, dość sztampowe, wychodzi
$$\sigma =\frac{ 2 \pi m_e^2 Z^2 e^4}{\hbar^4 k^2} \big(\frac{1}{\alpha^2} - \frac{1}{\alpha^2+4k^2}\big)$$

W granicy klasycznej $\alpha \to 0$ rozbieżne. Więc $\alpha$ nie jest zero! Jest faktycznie jakieś ekranowanie

> $\alpha \to 0$ - TU ŻYJĄ SMOKI I ELEKTRODYNAMIKA KWANTOWA

> Ale proszę zauważyć że masa tego sznurka jest zaniedbywalna w porównaniu z masą kuli!

### Potencjały typu $\alpha/r^\beta$
(ogólniejsze, nie tylko kulmbowskie)

$\sigma$ zbieżne dla $\beta \geq 3$ (krótkozasięgowe - można zaniedbać wpływ otoczenia, "odseparować")

Wodór: oddziaływanie H-H - VDW - krótkozasięgowy $r^{-6}$

Twierdzenie: biorąc amplitudę rozpraszania $f(\vec{k})$ ($E=\frac{(\hbar k)^2}{2m}$) można pokazać że w rozwinięciu Taylora $f^{-1}(k)$ wchodzą parzyste potęgi:

$$f^{-1}(k) \sim -\frac{1}{a_s} + \frac{r_{eff}}{2} k^2 + \frac{c}{4!} k^2 + ...$$
$a_s$ - długość rozpraszania

$r_{eff}$ - zasięg efektywny

Pamiętajmy że jesteśmy w nierelatywistycznym reżimie :)

Zwykle wprowadzamy skalę energetczną $\Lambda < k$ i siedzimy z energiami poniżej tejże

Załóżmy że zmierzyliśmy $a_s$, $r_{eff}$

V_{eff}(r) możemy sobie wybrać stosunkowo dowolnie, byleby zgadzało się z naszymi parametrami - warto żeby się dobrze liczyło

Mamy elementarny proces rozpraszania -> możemy odtworzyć dowolny proces.

### Rozpraszanie neutronu
neutron wpadający na jądro atomowe
$k \to 0$
$a_s \sim -18.8 fm$

Zakładamy
$$V(r) = g \delta(\vec{r})$$


(potem rozpatrzymy neutron wpadający na ścianę z jąder atomowych)

1. Bierzemy przybliżenie Borna
2. Liczymy amplitudę rozpraszania
3. Żądamy żeby była stała dla małych k i utożsamić z długością rozpraszania

$ m << m_j$, więc masa zredukowana to po prostu masa neutronu

Przybliżenie Borna (fale kuliste):
$$f(\theta, \phi) = \frac{-m}{2\pi\hbar^2} \int V(\vec{r}) \exp(i \vec{q} \cdot \vec{r}) d^3\vec{r}$$

Całka wychodzi po prostu $g$, więc biorąc $f^{-1} = -a_s^{-1} = \frac{-mg}{2\pi\hbar^2}$  mamy
$$g = \frac{2\pi\hbar^2a_s}{m}$$

Dla przypadku interfejsu próżnia-ośrodek, $\vec{k}$ frunie przez próżnię i pada na ośrodek, załamując się

$$mv = p = \hbar k$$
$$n = \frac{v_{\text{ośrodek}}}{v_\text{próżnia}} = \frac{k_{\text{ośrodek}}}{k_\text{próżnia}}$$

W próżni $E=\frac{\hbar^2 k^2}{2m}$, w ośrodku dodajemy $\bar{V}$ (uśredniony potencjał z oddziaływań). Potencjał modelujemy jako całkę tych deltowych potencjałów $g\delta(\vec{r})$ dzieloną przez objętość

$$\bar{V} = \frac{1}{V} \int_V \sum_i g\delta(\vec{r}-\vec{r_i}) d^3\vec{r} = \frac{Ng}{V} = \rho g$$
($\rho$ - gęstość ilościowa atomów)

$$E_o = \frac{\hbar^2 k'^2}{2m} + \rho \frac{2\pi \hbar^2 a_s}{m} = E$$

$$k = \frac{\sqrt{2mE}}{\hbar}$$
$$k' = \sqrt{(E-\rho \frac{2\pi \hbar^2 a_s}{m}) \frac{2m}{\hbar^2}}$$

$$ n = \frac{k'}{k} = \sqrt{1-\frac{2\pi\rho\hbar^2a_s}{mE}} = n$$
