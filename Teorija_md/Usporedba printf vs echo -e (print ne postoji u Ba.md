<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Usporedba printf vs echo -e (print ne postoji u Bash-u)

**Napomena:** Bash **nema ugrađenu `print` naredbu**. Glavne opcije su `printf` i `echo -e`.


| Karakteristika | `printf` | `echo -e` |
| :-- | :-- | :-- |
| **Novi red** | Ne dodaje automatski | Automatski dodaje na kraju |
| **Format specifikatori** | ✅ Da (%s, %d, %f, %c) | ❌ Ne |
| **Escape sekvence** | ✅ Da (\n, \t, \$ | ✅ Da (\n, \t, \$ |
| **Preciznost formatiranja** | ✅ Vrlo visoka | ❌ Osnovna |
| **Složenost sintakse** | Kompleksnija | Jednostavnija |
| **Portabilnost** | ✅ POSIX standard | Varira među sustavima |
| **Kontrola širine** | ✅ Da (%-10s, %05d) | ❌ Ne |
| **Decimalne pozicije** | ✅ Da (%.2f) | ❌ Ne |
| **Boje ANSI** | ✅ Da | ✅ Da |

## Praktični primjeri usporedbe

### Osnovni ispis

```bash
# Printf
printf "Pozdrav svijetu\n"

# Echo -e  
echo -e "Pozdrav svijetu"
```


### Formatiranje brojeva

```bash
broj=3.14159

# Printf - precizno formatiranje
printf "Pi: %.2f\n" $broj          # Pi: 3.14
printf "Cijena: %8.2f HRK\n" $broj # Cijena:     3.14 HRK

# Echo -e - samo osnovni ispis
echo -e "Pi: $broj"                # Pi: 3.14159
```


### Tablica formatiranje

```bash
# Printf - profesionalna tablica
printf "%-15s | %8s | %6s\n" "IME" "GODINE" "PLAĆA"
printf "%-15s | %8s | %6s\n" "───" "──────" "─────"
printf "%-15s | %8d | %6.0f\n" "Marko Petrović" 30 5000
printf "%-15s | %8d | %6.0f\n" "Ana Kovač" 25 4500

# Echo -e - osnovni pristup
echo -e "IME\t\t| GODINE | PLAĆA"
echo -e "Marko Petrović\t| 30     | 5000"
echo -e "Ana Kovač\t| 25     | 4500"
```


### Escape sekvence

```bash
# Printf
printf "Red1\nRed2\tTab\n"

# Echo -e (isti rezultat)
echo -e "Red1\nRed2\tTab"
```


### Boje

```bash
# Printf
printf "\033[31m%s\033[0m\n" "Crveni tekst"

# Echo -e 
echo -e "\033[31mCrveni tekst\033[0m"
```


## Kada koristiti koju naredbu

### Koristite `printf` kada:

- ✅ Trebate precizno formatiranje
- ✅ Radite s brojčanim podacima
- ✅ Kreirate tablice ili izvještaje
- ✅ Trebate kontrolu nad širinom i poravnanjem
- ✅ Portabilnost je važna


### Koristite `echo -e` kada:

- ✅ Potreban je jednostavan ispis
- ✅ Radite s osnovnim tekstom
- ✅ Trebate brze debug poruke
- ✅ Koristite osnovne escape sekvence


## Praktični hibridni pristup

```bash
#!/bin/bash

# Kombiniranje prednosti obje naredbe
echo -e "\n🔍 SISTEMSKI PREGLED"
printf "═%.50s═\n" "══════════════════════════════════════════════════"

printf "%-20s: %s\n" "Datum" "$(date '+%d.%m.%Y')"
printf "%-20s: %s\n" "Korisnik" "$USER"

echo -e "\n💾 MEMORIJA:"
printf "   Ukupno: %8.1f GB\n" "$(free -g | awk 'NR==2{print $2}')"
printf "   Koristi: %8.1f GB\n" "$(free -g | awk 'NR==2{print $3}')"

echo -e "\n✅ Pregled završen!"
```

**Preporučeno:** Koristite `printf` za strukturirane izlaze i `echo -e` za jednostavne poruke. Kombiniranje obaju pristupa često daje najbolje rezultate u profesionalnim skriptama.

<div style="text-align: center">⁂</div>

[^1]: https://stackoverflow.com/questions/35603323/difference-between-printf-and-echo-in-bash

[^2]: https://stackoverflow.com/questions/66448210/difference-between-echo-and-printf-in-bash

[^3]: https://tecadmin.net/comparing-printf-vs-echo-commands-in-linux/

[^4]: https://linuxhandbook.com/bash-printf/

[^5]: https://www.namehero.com/blog/unlocking-the-potential-of-printf-in-shell-scripting/

[^6]: https://linuxconfig.org/bash-printf-syntax-basics-with-examples

[^7]: https://unix.stackexchange.com/questions/344666/printing-ranges-of-output-with-echo

[^8]: https://superuser.com/questions/1834509/how-to-achieve-side-by-side-output-in-bash

[^9]: https://www.reddit.com/r/bash/comments/kcmxqu/difference_between_print_and_printf/

[^10]: https://ioflood.com/blog/bash-printf/

