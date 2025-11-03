<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Echo naredba - osnove

**`echo`** je jedna od najosnovnijih bash naredbi za ispis teksta na terminal.

## Razlika između `echo` i `echo -e`

### `echo` (bez opcija)

```bash
echo "Pozdrav svijete"
# Ispisuje: Pozdrav svijete
```

**Karakteristike:**

- Ispisuje tekst doslovno
- Ne interpretira escape sekvence
- Dodaje novi red na kraju


### `echo -e` (s opcijom -e)

```bash
echo -e "Pozdrav\nsvijete"
# Ispisuje:
# Pozdrav
# svijete
```

**Karakteristike:**

- **Interpretira escape sekvence**
- Omogućuje formatiranje teksta
- Dodaje novi red na kraju


## Najčešće escape sekvence

| Sekvenca | Značenje | Primjer |
| :-- | :-- | :-- |
| `\n` | Novi red | `echo -e "Red1\nRed2"` |
| `\t` | Tab | `echo -e "Ime:\tIvan"` |
| `\r` | Carriage return | `echo -e "Loading\r100%"` |
| `\b` | Backspace | `echo -e "Test\b\b12"` |
| `\a` | Zvučni signal | `echo -e "Upozorenje!\a"` |
| `\\` | Literal backslash | `echo -e "Putanja: C:\\Users"` |
| `\"` | Literal quote | `echo -e "Rekao je: \"Pozdrav\""` |

## Praktični primjeri

### Osnovni echo

```bash
echo "Jednostavan tekst"
echo Tekst bez navodnika
echo "Tekst s \n neće raditi"
# Output: Tekst s \n neće raditi
```


### Echo s -e opcijom

```bash
echo -e "Prva linija\nDruga linija"
# Output:
# Prva linija
# Druga linija

echo -e "Ime:\tIvan\nGodine:\t25"
# Output:
# Ime:    Ivan
# Godine: 25
```


### Formatiranje s bojama

```bash
# Bez -e (neće raditi)
echo "\033[32mZeleni tekst\033[0m"
# Output: \033[32mZeleni tekst\033[0m

# S -e (radi ispravno)
echo -e "\033[32mZeleni tekst\033[0m"
# Output: Zeleni tekst (u zelenoj boji)
```


## Ostale korisne opcije

### `echo -n` (bez novog reda)

```bash
echo -n "Bez novog reda"
echo "Nastavlja na istom redu"
# Output: Bez novog redaNastavlja na istom redu
```


### Kombiniranje opcija

```bash
echo -en "Loading\r"
sleep 1
echo -e "Complete!"
# "Loading" se prebrisava s "Complete!"
```


## Praktični primjer u skripti

```bash
#!/bin/bash

# Osnovno korištenje
echo "=== OSNOVNI ECHO ==="
echo "Jednostavan tekst"
echo Tekst bez navodnika

# Echo s escape sekvencama
echo -e "\n=== ECHO -E ==="
echo -e "Red 1\nRed 2\nRed 3"

# Formatiranje
echo -e "\n=== FORMATIRANJE ==="
echo -e "Ime:\t\tMarko"
echo -e "Prezime:\tPetrović"
echo -e "Grad:\t\tZagreb"

# Progress bar simulacija
echo -e "\n=== PROGRESS BAR ==="
echo -n "Loading: "
for i in {1..10}; do
    echo -n "█"
    sleep 0.1
done
echo -e "\nGotovo!"

# Boje
echo -e "\n=== BOJE ==="
echo -e "\033[31mCrveni tekst\033[0m"
echo -e "\033[32mZeleni tekst\033[0m"
echo -e "\033[33mŽuti tekst\033[0m"
```


## Ključna razlika

**Bez `-e`:** Escape sekvence se tretiraju kao obični tekst
**S `-e`:** Escape sekvence se interpretiraju i izvršavaju

Opcija `-e` je ključna za napredne bash skripte gdje trebate kontrolirati formatiranje, boje i layout terminala.

