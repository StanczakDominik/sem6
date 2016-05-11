# Sieci 16.05.11
## Bezpieczeństwo w Sieci
### Narzędzia
* Firewall
* Switche
* Kryptografia - wbudowana w HTTP(s), maile, itd
* IDS - Intrusion Detection System
* Antywirusy
* Backup, okresowy, automatyczny

### Co możemy zrobić my:
* Używać SSH
* Nie działać na koncie admina
* Aktualizoać soft
* Serwer tylko jako serwer, nie jako gloryfikowany klient
* Dobra konfiguracja
* Firewall, IDS, backup na serwerze (przynajmniej)
* Log aktywności + backup tegoż

### Od strony projektowania sieci
* Podział sieci na podukłady, każda z własną ochroną
* Firewall pomiędzy strefami własnej firmy
    * Breach na jeden komputer: cała podsieć compromised

### Jak się włamać do sieci
* Zbieranie informacji - strony, fora, materiały promocyjne
    * Kontra: nie udostępniać tego co niepotrzebne
* Inżynieria społeczna - dane osobowe, podszywanie się
    * Weryfikacja i szkolenie użytkowników
* Dostęp do DNS, WHOIS
    * Minimalizacja wpisów w tymże
* Mapowanie sieci (spingować każdy adres, traceroute)
    * Można zablokować ICMP
    * > Nie bądźmy frajerami
    * Użyć DNS
* Skanowanie portów
    * Jest karalne, jak kogoś złapać

### Jak już zbierzemy dane, jak się włamać do sieci
* Wyciągnąć login/hasło
    * social engineering
    * bruteforce
    * podsłuchać traffic sieciowy - jeśli ktoś wysyła bez enkrypcji to bingo
* Backdoory
* Exploity
    * > Little Bobby Tables
* APR spoofing (przekierowanie z IP na IP)
* TCP spoofing (przechwytywanie transmisji)
* Man in the middle (przekierowanie połączenia, by biegło przez nasz niecny hakerski system)
* DNS spoofing
* Zakłócenie komunikacji sieciowej - routing/ICMP
* DoS, DDoS

> Większość hakerów to n00by
