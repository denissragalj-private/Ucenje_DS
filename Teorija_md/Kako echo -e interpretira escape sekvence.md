<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Kako echo -e interpretira escape sekvence

Opcija `-e` u echo naredbi **aktivira interpretaciju escape sekvenci**, što znači da bash umjesto da tretira backslash (`\`) kao obični znak, koristi ga kao **signal za posebno formatiranje**[^1][^4].

## Mehanizam interpretacije

**Bez `-e` opcije:**

```bash
echo "Prva linija\nDruga linija"
# Output: Prva linija\nDruga linija
```

**S `-e` opcijom:**

```bash
echo -e "Prva linija\nDruga linija"
# Output:
# Prva linija
# Druga linija
```


## Kako funkcionira escape karakter

Backslash (`\`) djeluje kao **escape karakter** koji označava da sljedeći znak ima posebno značenje[^4]:

### Osnovne escape sekvence

| Sekvenca | Funkcija | Rezultat |
| :-- | :-- | :-- |
| `\n` | Nova linija | Prelazi u novi red |
| `\t` | Tab | Dodaje tabulator |
| `\r` | Carriage return | Vraća kursor na početak linije |
| `\b` | Backspace | Briše jedan znak unatrag |
| `\\` | Literal backslash | Prikazuje jedan \ |

### Primjer interpretacije

```bash
# Bash čita: echo -e "Test\nNova linija"
# Interpretira: \n kao signal za novi red
# Izvršava: prikaži "Test", napravi novi red, prikaži "Nova linija"
```


## Boje i ANSI escape sekvence

Echo -e omogućava i interpretaciju **ANSI escape kodova** za boje[^2]:

```bash
echo -e "\033[31mCrveni tekst\033[0m"
# \033[ - ANSI escape početak
# 31m - kod za crvenu boju
# \033[0m - reset na normalnu boju
```


## Razlika u interpretaciji navodnika

**Dvostruki navodnici** omogućavaju interpretaciju nekih znakova već na razini shell-a[^5]:

```bash
# Shell interpretira $USER prije echo naredbe
echo -e "Korisnik: $USER\nDatum: $(date)"
```

**Jednostruki navodnici** sprječavaju shell interpretaciju[^5]:

```bash
# Sve ostaje literal za echo -e
echo -e 'Tekst: $USER\nNova linija'
```


## Praktični primjer rada

```bash
#!/bin/bash

# 1. Shell čita naredbu
echo -e "Status: \033[32m✔\033[0m\nGotovo!"

# 2. Shell predaje echo naredbi string:
# "Status: \033[32m✔\033[0m\nGotovo!"

# 3. Echo s -e opcijom interpretira:
# \033[32m → zelena boja
# ✔ → Unicode znak
# \033[0m → reset boje  
# \n → novi red
# Gotovo! → običan tekst

# 4. Terminal prikazuje:
# Status: ✔ (u zelenoj boji)
# Gotovo!
```


## Kontrola interpretacije

**Escape backslash za literal prikaz:**

```bash
echo -e "Literal \\n umjesto novog reda"
# Output: Literal \n umjesto novog reda
```

**Kombiniranje s varijablama:**

```bash
MESSAGE="Poruka"
echo -e "${MESSAGE}:\n- Prvi red\n- Drugi red"
```

Opcija `-e` u suštini **aktivira parser za escape sekvence** unutar echo naredbe, omogućavajući napredne formatiranje terminala koje inače ne bi bilo moguće s običnim tekstom.

<div style="text-align: center">⁂</div>

[^1]: https://stackoverflow.com/questions/37129699/escaping-rules-when-reading-in-bash

[^2]: https://labex.io/questions/what-is-the-purpose-of-the-echo-command-in-linux-271273

[^3]: https://mywiki.wooledge.org/BashGuide/SpecialCharacters

[^4]: https://www.shellscript.sh/escape.html

[^5]: http://www.compciv.org/topics/bash/text-values

[^6]: https://unix.stackexchange.com/questions/141312/how-to-escape-special-characters-in-a-string

[^7]: https://superuser.com/questions/1612281/why-does-writing-a-before-a-string-affect-how-bash-interprets-backslashes-in-i

[^8]: https://www.reddit.com/r/bash/comments/13uob2m/escape_value_x1b_echoing_problem/

[^9]: https://askubuntu.com/questions/1433229/how-do-i-echo-a-file-path-after-interpreting-characters-like-dots-and-tildes

[^10]: https://unix.stackexchange.com/questions/420185/what-do-special-characters-stand-for-in-echo-a-z

