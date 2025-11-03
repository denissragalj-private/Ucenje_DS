<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Box Drawing znakovi - specijalni znakovi za obrube

Znakovi koje koristite su iz **Unicode Box Drawing** grupe (U+2500-U+257F). Evo kompletnog pregleda dostupnih znakova:

## Osnovni Box Drawing znakovi

### Jednostruke linije

| Znak | Unicode | Opis |
| :-- | :-- | :-- |
| ─ | U+2500 | Horizontalna linija |
| │ | U+2502 | Vertikalna linija |
| ┌ | U+250C | Gornji lijevi kut |
| ┐ | U+2510 | Gornji desni kut |
| └ | U+2514 | Donji lijevi kut |
| ┘ | U+2518 | Donji desni kut |
| ├ | U+251C | Lijeva T veza |
| ┤ | U+2524 | Desna T veza |
| ┬ | U+252C | Gornja T veza |
| ┴ | U+2534 | Donja T veza |
| ┼ | U+253C | Križ/plus |

### Dvostruke linije (kao u vašem primjeru)

| Znak | Unicode | Opis |
| :-- | :-- | :-- |
| ═ | U+2550 | Horizontalna dvostruka |
| ║ | U+2551 | Vertikalna dvostruka |
| ╔ | U+2554 | Gornji lijevi (dvostruko) |
| ╗ | U+2557 | Gornji desni (dvostruko) |
| ╚ | U+255A | Donji lijevi (dvostruko) |
| ╝ | U+255D | Donji desni (dvostruko) |
| ╠ | U+2560 | Lijeva T (dvostruko) |
| ╣ | U+2563 | Desna T (dvostruko) |
| ╦ | U+2566 | Gornja T (dvostruko) |
| ╩ | U+2569 | Donja T (dvostruko) |
| ╬ | U+256C | Križ (dvostruko) |

## Deblje linije

| Znak | Unicode | Opis |
| :-- | :-- | :-- |
| ━ | U+2501 | Deblja horizontalna |
| ┃ | U+2503 | Deblja vertikalna |
| ┏ | U+250F | Deblji gornji lijevi |
| ┓ | U+2513 | Deblji gornji desni |
| ┗ | U+2517 | Deblji donji lijevi |
| ┛ | U+251B | Deblji donji desni |

## Kako pronaći znakove kada vam trebaju

### 1. Character Map aplikacije

**Ubuntu:**

```bash
sudo apt install gucharmap
gucharmap
```

Tražite "Box Drawing" u kategorijama.

**Windows:**

- Pritisnite `Win + R`, unesite `charmap`
- Filtrirajte po "Unicode blok: Box Drawing"


### 2. Online Unicode reference

**Korisni web resursi:**

- [unicode-table.com](https://unicode-table.com/en/blocks/box-drawing/)
- [fileformat.info](https://www.fileformat.info/info/unicode/block/box_drawing/list.htm)
- [compart.com](https://www.compart.com/en/unicode/block/U+2500)


### 3. Bash skripta za pregled

```bash
#!/bin/bash

echo "╔═══════════════════════════════════════════════════════╗"
echo "║                BOX DRAWING ZNAKOVI                    ║"
echo "╠═══════════════════════════════════════════════════════╣"
echo "║                                                       ║"
echo "║ JEDNOSTRUKE LINIJE:                                   ║"
echo "║ ┌─┬─┐  ├─┼─┤  └─┴─┘                                  ║"
echo "║ │ │ │  │ │ │                                         ║"
echo "║                                                       ║"
echo "║ DVOSTRUKE LINIJE:                                     ║"
echo "║ ╔═╦═╗  ╠═╬═╣  ╚═╩═╝                                  ║"
echo "║ ║ ║ ║  ║ ║ ║                                         ║"
echo "║                                                       ║"
echo "║ DEBLJE LINIJE:                                        ║"
echo "║ ┏━┳━┓  ┣━╋━┫  ┗━┻━┛                                  ║"
echo "║ ┃ ┃ ┃  ┃ ┃ ┃                                         ║"
echo "╚═══════════════════════════════════════════════════════╝"
```


## Praktični primjeri različitih stilova

### Jednostruka tablica

```bash
echo "┌─────────────┬─────────┬─────────┐"
echo "│ PROIZVOD    │ CIJENA  │ KOLIČINA│"
echo "├─────────────┼─────────┼─────────┤"
echo "│ Jabuke      │  12.50  │   100   │"
echo "│ Naranče     │  15.75  │    85   │"
echo "└─────────────┴─────────┴─────────┘"
```


### Dvostruka tablica

```bash
echo "╔═════════════╦═════════╦═════════╗"
echo "║ PROIZVOD    ║ CIJENA  ║ KOLIČINA║"
echo "╠═════════════╬═════════╬═════════╣"
echo "║ Jabuke      ║  12.50  ║   100   ║"
echo "║ Naranče     ║  15.75  ║    85   ║"
echo "╚═════════════╩═════════╩═════════╝"
```


### Mješoviti stilovi

```bash
echo "╔═══════════════════════════════════════════════════════╗"
echo "║                    GLAVNI NASLOV                      ║"
echo "╠═══════════════════════════════════════════════════════╣"
echo "║ ┌─────────────────────────────────────────────────┐   ║"
echo "║ │              Podnaslov                         │   ║"
echo "║ └─────────────────────────────────────────────────┘   ║"
echo "║                                                       ║"
echo "║ ◆ Prva stavka                                         ║"
echo "║ ◆ Druga stavka                                        ║"
echo "╚═══════════════════════════════════════════════════════╝"
```


## Pomoćna skripta za kreiranje okvira

```bash
#!/bin/bash

# Funkcija za kreiranje okvira
create_box() {
    local text="$1"
    local style="${2:-single}"
    
    if [ "$style" = "double" ]; then
        local top_left="╔" top_right="╗"
        local bottom_left="╚" bottom_right="╝"
        local horizontal="═" vertical="║"
    else
        local top_left="┌" top_right="┐"
        local bottom_left="└" bottom_right="┘"
        local horizontal="─" vertical="│"
    fi
    
    local length=${#text}
    local padding=4
    local total_width=$((length + padding))
    
    # Gornji red
    printf "%s" "$top_left"
    for ((i=1; i<=total_width; i++)); do printf "%s" "$horizontal"; done
    printf "%s\n" "$top_right"
    
    # Srednji red s tekstom
    printf "%s  %s  %s\n" "$vertical" "$text" "$vertical"
    
    # Donji red
    printf "%s" "$bottom_left"
    for ((i=1; i<=total_width; i++)); do printf "%s" "$horizontal"; done
    printf "%s\n" "$bottom_right"
}

# Korištenje
create_box "Jednostrukan okvir" "single"
echo ""
create_box "Dvostruk okvir" "double"
```

**Savjet:** Najbolji način je **kopiranje iz online Unicode tablica** ili korištenje Character Map aplikacije za pronalaženje točno onih znakova koji vam trebaju!

