| Magistrala | wat | hm |
|------|-----|----|
|USART|
|SPI|
|TWI|
|USB|
|1Wire

# Pojęcia
* Baud rate - prędkość transmisji *informacji* (merytorycznej)
* Bit rate - prędkość przesyłu danych (w tym maintenance jak parity, stop, start)

# Magistrale
1. USART
    * Dwie linie transmisyjne
        1. RxD - Receive Data
        2. TxD - Transmit Data
    * Tryb synchroniczny, asynchroniczny (konieczny dobór taktowania!)
    * Ramka transmisyjna
        * ma cały przewód dla siebie
        * stała szybkość przesyłu (np. 1200bps)
        * start bit = 0, odbiornik łapie falling edge
        * 5-9 bitów danych rosnąco wg potęg (od lsb)
        * opcjonalnie: parity bit` = sum(bits)%2`
        * stop bit = 1, przygotowuje falling edge
    * Rejestry w AVR
        * UBRR - **U**SART **B**aud **R**ate **R**egister
        * UDR - **U**SART **D**ata **R**egister, input\output
        * UCSRA - **U**SART **C**ontrol and **S**tatus **R**egister
            * RXC: Receive Complete
            * TXC: Transmit Complete, bufor pusty
            * UDRE: USART Data Register Empty, można wpisać do UDR
            * FE: Framing Error: bit stopu nie jest 1
            * PE: Parity Error
            * DOR: Data OverRun: coś zostało w UDR
            * U2X: USART 2krotnie szybszy przesył danych
            * MPCM: MultiProcessor Communication Mode
                * UCSRB
            * RXCIE: Receive Complete Interrupt Enable
            * TXCIE
            * UDRIE: UDR (Empty) Interrupt Enable
            * RXEN: Receive Enable (odbiornik)
            * TXEN: Trasmit Enable
            * UCSZ: USART Character SiZe (ile bitów w ramce to informacje?)
            * RXB8, TXB8 - dla 9-bitowego trybu ramki
                * UCSRC
            * URSEL: USART Register SELect (UCSRC czy UBRRH)
            * UMSEL: USART Mode SELect (async, sync)
            * UMP: USART Mode Parity
            * USBS: USART Stop Bite Size (1, 2)
2. SPI
    * Rozdział Master\Slave. Liie danych między jednym a drugim
        * SCK: Serial ClocK
        * MISO: Master In Slave Out - wejście do mastera
        * MOSI: Master Out Slave In - wyjście z mastera
        * SS: Slave Select
    * SPCR - SPI Control Register
        * SPIE - SPI Interrupt Enable (transmisja zakończona)
        * SPE - SPI Enable
        * DORD - Data ORDer
        * MSTR - 1: MaSTeR, 0: Slave
        * CPOL - Clock POLarity - high czy low na bezczynnym
        * CPHA - Clock PHAse - rising czy falling edge sampling
        * SPR: SamPling Rate
    * SPSR - SPI Status Register
        * SPIF: SPI Interrupt Flag
        * WCOL: Word COLlision
        * SPI2X: SPI dwakroć szybszy
    * SPDR - SPI Data Register
