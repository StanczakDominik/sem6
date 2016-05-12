# 16.05.12 DUN
### Ruch kwaziperiodyczny

Brak oscylacji (punkt stały) - traci stabilność i zostaje zastąpiony oscylacjami (dokładnie tak jak u Strogatza! Subcritical, supercritical bifurcation)

### Oscylator van der Pola
$$\ddot{x} + \beta (x^2-1) \dot{x} + \omega^2 x = 0$$

Nieliniowe tłumienie (przy $\dot{x}$), liniowa częś mechaniczna
Dla małych $x$ $x^2-1 < 0$, *ujemna oporność* - tu właśnie pojawia się bifurkacja Hopfa, ze wzmacniacza robi się generator. Układ dostaje kopa na zewnątrz

Dla $|x|>1$ zwykłe tłumienie

### Ruch z 2 częstościami w przestrzeni fazowej

Można wizualizować jako torus: po dużym kole jedna częstość, po małym obwodzie druga częstość

Jeśli stosunek częstości jest wymierny, **synchronizacja n/m**, nie jest to stricte kwaziperiodyczność - trajektorie się zamykają (**jak w tokamakach :>**)

### Niestabilność Rayleigha Benarda
Temperatura od czasu T(t), $t= n \tau = n 2 \pi/ \omega_0$. W przestrzeni fazowej $(T(t), \dot{T}(t))$ dostajemy faktycznie torus - po zwiększeniu wpływu ciepła z dołu (kontrolnego) układ robi się chaotyczny, na pewno nie ma tam ruchu po torusie

### TURBULENCJA
> Landau kumplował się z Feynmanem

* Kaskada wirów: wir(wir(wir(wir(wir(...))))

Landau w 1944 rozgryza, że nieskończony ciąg bifurkacji Hopfa prowadzi do turbulencji w hydrodynamice.
Rok później Adolf Hitler popełnia samobójstwo.

Wiry: pochłaniają energię i tłumią drgania

### Nieco później, 1978

Newhouse, Taken, Ruelle - badali ruch na torusie, pokazali że ruch na 4-torusie jest niestabilny. Skoro tak, to wg Landaua byłoby:
1. laminarny
2. wałek
3. jakieś kuliste...?
4. Coś dalej...?
A oni wykazali że zaobserwujemy trzy częstości, bo tylko one są stabilne.

### Trzy drogi do chaosu
1. Podwajanie okresu
2. Intermitencja
    1. pierwsza
    2. druga
    3. trzecia
3. **Kwaziperiodyczność**
    * W widmie mocy 2, 3 częstości -> zmiana parametru kontrolnego -> szum na szerokim paśmie
    * Przed przejściem do chaosu rekonstrukcja trajektorii w phase space ujawnia torus (np. $(T, \dot{T})$) - odwzorowanie $\theta_{n+1} = f(\theta_n)$ podobne do odwzorowania okręgu
    * Podczas przejścia rozpad torusa
    * Pojawienie się diabelskich schodów w szeregu czasowym

### Przykłady na trzecią kwaziperiodyczną drogę do chaosu
* Hydrodynamika - Taylor-Couette flow
    * standaryzacja warunków brzegowych: wirujące współosiowe walce, między nimi ciecz z markerami (opiłki aluminium, tytanowe jakieś rzeczy)
    * Jeśli $\Delta \omega$ między dwoma walcami większa od wartości granicznej, ciecz przestaje płynąć laminarnie - zaczyna płynąć w wałkach toroidalnych
    * DALEJ JEST NIESTABILNE, WAŁKI SIĘ MIESZAJĄ (**MAGNETIC RECONNECTION**)
    * Model mechaniczny wiru na Jowiszu
    * Badamy to laserami (efekt: zmiana częstości lasera)
        1. jeden dyskretny peak na prędkości
        2. jedna dodatkowa częstość
        3. rozpad na ciągłe spektrum

        4. robimy Takensa,
        5. dostajemy torus
        6. zwiększając paramsy tors się rozpada (kolaps do środka)
* Numerycznie - równanie oscylatora nieliniowego $\ddot{\theta} + \gamma \dot{\theta} + \sin(\theta) = A \cos(\omega t)+ B$ (złącze Josephsona, fale plazmowe)
    * $\theta_n$ co okres siły wymuszającej
* LHC
* Tokamaki! <3
* Oscylator biologiczny - synchronizacja komórek serca embrionu kurczaka
    * test bed dla nowych leków: jak wpływają na bicie serca
    * $\delta_{i+1} + T_i = \delta_i + t_s$
    * czas refrakcji
    * zmieniając okres pobudzenia (impulsem elektrycznym) obserwujemy synchronizację różnych modów, 2:1, 1:1, 2:3
    * przejścia 1:1 -> 2:2 - to nie jest to samo bo są pewne różnice w fazie, 4:4 też
