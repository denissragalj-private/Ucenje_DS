<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Testna skripta za Ubuntu 24

Evo kompletne skripte koja demonstrira sve navedene Unicode simbole:

```bash
#!/bin/bash

# Boje za bolje vizualno predstavljanje
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

clear

echo -e "${WHITE}═══════════════════════════════════════════════════════"
echo -e "    TESTIRANJE UNICODE SIMBOLA ZA BASH SKRIPTE"
echo -e "═══════════════════════════════════════════════════════${NC}\n"

# Statusni indikatori
echo -e "${GREEN}## STATUSNI INDIKATORI${NC}"
echo -e "${GREEN}✔${NC} Uspješno izvršavanje (U+2714)"
echo -e "${GREEN}✓${NC} Alternativni check mark (U+2713)"
echo -e "${GREEN}√${NC} Kvadratni korijen kao fallback"
echo -e "${GREEN}✅${NC} Emoji verzija uspjeha"
echo ""
echo -e "${RED}✗${NC} Greška (U+2717)"
echo -e "${RED}✘${NC} Alternativni X (U+2718)"
echo -e "${RED}×${NC} Jednostavan X (U+00D7)"
echo -e "${RED}❌${NC} Emoji verzija greške"
echo ""
echo -e "${YELLOW}⚠${NC} Upozorenje (U+26A0)"
echo -e "${YELLOW}‼${NC} Dvostruki uskličnik (U+203C)"
echo -e "${YELLOW}⚠️${NC} Emoji upozorenje"
echo ""
echo -e "${BLUE}ℹ${NC} Informacija (U+2139)"
echo -e "${BLUE}ℹ️${NC} Emoji informacija"

echo -e "\n${CYAN}## STRELICE I NAVIGACIJA${NC}"
echo -e "→ Strelica desno (U+2192)"
echo -e "← Strelica lijevo (U+2190)"
echo -e "↑ Strelica gore (U+2191)"
echo -e "↓ Strelica dolje (U+2193)"
echo ""
echo -e "➡ Deblja strelica desno (U+27A1)"
echo -e "⬅ Deblja strelica lijevo (U+2B05)"
echo -e "⬆ Deblja strelica gore (U+2B06)"
echo -e "⬇ Deblja strelica dolje (U+2B07)"
echo ""
echo -e "❯ Pointer za meniuje (U+276F)"
echo -e "▶ Play simbol"

echo -e "\n${PURPLE}## AKTIVNOSTI I PROCESI${NC}"
echo -e "⚙ Zupčanik - postavke (U+2699)"
echo -e "🔄 Refresh/reload"
echo -e "⏳ Pješčani sat - čekanje (U+23F3)"
echo -e "🌀 Spirala - kontinuiran proces"
echo -e "🔍 Lupa - pretraživanje"
echo -e "📝 Olovka - pisanje/uređivanje"
echo -e "♻️ Recikliranje"

echo -e "\n${WHITE}## GEOMETRIJSKI OBLICI${NC}"
echo -e "● Puna točka (U+25CF)"
echo -e "○ Prazna točka (U+25CB)"
echo -e "■ Pun kvadrat (U+25A0)"
echo -e "□ Prazan kvadrat (U+25A1)"
echo -e "▲ Trokut gore (U+25B2)"
echo -e "▼ Trokut dolje (U+25BC)"
echo -e "◆ Pun dijamant (U+25C6)"
echo -e "◇ Prazan dijamant (U+25C7)"

echo -e "\n${YELLOW}## ZVIJEZDE I OZNAČAVANJE${NC}"
echo -e "★ Crna zvijezda (U+2605)"
echo -e "☆ Bijela zvijezda (U+2606)"
echo -e "⭐ Emoji zvijezda"

echo -e "\n${RED}## BOJENI KRUGOVI${NC}"
echo -e "🔴 Crveni krug"
echo -e "${GREEN}🟢 Zeleni krug${NC}"
echo -e "${YELLOW}🟡 Žuti krug${NC}"
echo -e "⚫ Crni krug"
echo -e "⚪ Bijeli krug"

echo -e "\n${BLUE}## CHECKBOX I RADIO ELEMENTI${NC}"
echo -e "☐ Prazan checkbox (U+2610)"
echo -e "☑ Označen checkbox (U+2611)"
echo -e "☒ X u checkboxu (U+2612)"
echo -e "◯ Prazan radio (U+25EF)"
echo -e "◉ Označen radio (U+25C9)"

echo -e "\n${GREEN}## PRAKTIČNI PRIMJER UPOTREBE${NC}"
echo -e "${GREEN}✔${NC} Aplikacija pokrenuta uspješno"
echo -e "${YELLOW}⚠${NC} Upozorenje: Niska razina memorije"
echo -e "${RED}✗${NC} Greška: Datoteka nije pronađena"
echo -e "${BLUE}ℹ${NC} Info: Proces je u tijeku..."
echo -e "${CYAN}→${NC} Prelazim na sljedeći korak"
echo -e "${PURPLE}🔄${NC} Restartiranje servisa..."
echo -e "${GREEN}✅${NC} Sve je završeno uspješno!"

echo -e "\n${WHITE}═══════════════════════════════════════════════════════"
echo -e "              TESTIRANJE ZAVRŠENO"
echo -e "═══════════════════════════════════════════════════════${NC}\n"

# Test ASCII fallback verzije
echo -e "${CYAN}## ASCII FALLBACK VERZIJE (za starije terminale)${NC}"
echo "[OK] Uspjeh"
echo "[FAIL] Greška"
echo "[WARN] Upozorenje"
echo "[INFO] Informacija"
echo "-> Strelica desno"
echo "<- Strelica lijevo"
echo "* Bullet point"
echo "# Kvadrat"

echo -e "\n${GREEN}Skripta završena. Svi simboli trebaju biti vidljivi u Ubuntu 24!${NC}"
```


## Kako pokrenuti skriptu

1. **Spremite skriptu:**
```bash
nano unicode_test.sh
```

2. **Zalijepite gore navedeni kod i spremite datoteku**
3. **Dodajte izvršne dozvole:**
```bash
chmod +x unicode_test.sh
```

4. **Pokrenite skriptu:**
```bash
./unicode_test.sh
```


## Očekivani rezultat

Ubuntu 24 standardno podržava UTF-8 kodiranje i moderna terminala poput Gnome Terminal-a trebaju prikazati sve Unicode simbole ispravno. Ako neki simboli nisu vidljivi, možda trebate:

- Provjeriti da terminal koristi UTF-8 kodiranje
- Instalirati font koji podržava više Unicode simbola (npr. Noto fonts)
- Koristiti ASCII fallback verzije na dnu skripte

Ova skripta će vam pokazati kako izgledaju svi spomenuti simboli i omogućiti vam da odaberete one koji najbolje rade u vašem okruženju.

