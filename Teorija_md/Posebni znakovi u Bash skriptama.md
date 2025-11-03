<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Posebni znakovi u Bash skriptama

U Linux bash skriptama možete koristiti različite tipove znakova - od osnovnih posebnih znakova koji imaju funkcionalnost u bash-u do Unicode znakova i emoji-ja kao što je ♻️ u vašem primjeru.

## Osnovni posebni znakovi u bash-u

| Znak | Značenje |
| :-- | :-- |
| `#` | Komentar - sve nakon ovog znaka se ignoriše[^1][^6] |
| `$` | Referenca na vrijednost varijable[^1][^6] |
| `>` | Preusmjeravanje izlaza u datoteku[^1][^6] |
| `>>` | Dodavanje izlaza na kraj datoteke[^1][^6] |
| `<` | Preusmjeravanje ulaza iz datoteke[^1][^6] |
| `|` | Pipe - proslijedi izlaz jedne naredbe kao ulaz drugoj[^1][^6] |
| `&` | Pokreni naredbu u pozadini[^1][^6] |
| `;` | Sekvencijalno izvršavanje naredbi[^1][^6] |
| `*` | Wildcard za bilo koji broj znakova[^1][^6] |
| `?` | Wildcard za točno jedan znak[^1][^7] |
| `\` | Escape znak za poništavanje posebnog značenja[^1][^8] |

## Unicode znakovi i emoji-ji

Za Unicode znakove poput ♻️ iz vašeg primjera, možete koristiti nekoliko formata:

**UTF-8 oktalni format:**

```bash
echo -e "\342\236\244"  # Crna strelica prema desno
```

**UTF-8 heksadecimalni format:**

```bash
echo -e "\xe2\x9e\xa4"  # Isti znak
```

**\$'...' sintaksa s Unicode kod bodovima:**

```bash
echo $'\u2764'  # Crveno srce ❤️
echo $'\u267e'  # Simbol recikliranja ♾️
```

**Direktno umetanje emoji-ja:**
Možete direktno kopirati emoji iz izvora poput getemoji.com i zalijepiti ga u skriptu[^4]:

```bash
echo "♻️ Recikliranje"
echo "✅ Uspješno"
echo "❌ Greška"
echo "⚠️ Upozorenje"
```


## Korisni Unicode znakovi za skripte

- **Strelice:** → ← ↑ ↓ ⬆️ ⬇️ ➡️ ⬅️
- **Status indikatori:** ✅ ❌ ⚠️ ℹ️ 🔴 🟢 🟡
- **Aktivnosti:** ♻️ 🔄 ⏳ ⚙️ 🛠️ 📝 📊
- **Geometrijski oblici:** ● ○ ■ □ ▲ ▼ ◆ ◇


## Primjer korištenja u skripti

```bash
#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}✅ Aplikacija je pokrenuta uspješno"
echo -e "${YELLOW}♻️ Preporučamo restart ERPNext kontejnera"
echo -e "${RED}❌ Greška u konfiguraciji"
echo -e "${NC}ℹ️ Informacija: Proces je završen"
```


## Napomene o escapiranju

Kod korištenja posebnih znakova poput `!` u echo naredbama, koristite jednostruke navodnike da spriječite interpretaciju[^3]:

```bash
echo 'Wake up!'  # Radi ispravno
echo "Wake up!"  # Može uzrokovati grešku zbog !
```

Za znakove poput `$`, `\`, i druge bash meta-znakove, koristite backslash za escapiranje ili jednostruke navodnike za literalno tretiranje[^7][^8].

<div style="text-align: center">⁂</div>

[^1]: https://mywiki.wooledge.org/BashGuide/SpecialCharacters

[^2]: https://askubuntu.com/questions/1440734/using-utf-16-syntax-to-include-unicode-characters-in-bash-prompt-ps1

[^3]: https://unix.stackexchange.com/questions/191673/using-character-in-echo

[^4]: https://apple.stackexchange.com/questions/331995/display-emoji-faces-for-correct-wrong-commands-in-terminals

[^5]: https://javarevisited.blogspot.com/2011/06/special-bash-parameters-in-script-linux.html

[^6]: https://tecadmin.net/bash-special-characters/

[^7]: https://devdojo.com/bobbyiliev/17-special-characters-in-the-shell-that-you-should-know

[^8]: https://www.baeldung.com/linux/special-characters-in-shell-scripts

[^9]: https://stackoverflow.com/questions/70549800/handling-special-characters-in-bash-script

[^10]: https://stackoverflow.com/questions/72324913/how-to-pass-variables-with-special-characters-into-a-bash-script-when-called-fro

