<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Interpretacija escape sekvenci u echo -e

Echo -e omogućava interpretaciju escape sekvenci kroz **dvostruki proces parsiranja** - prvo kroz bash shell, a zatim kroz echo naredbu samu.

## Proces interpretacije

### 1. Shell razina (prva interpretacija)

```bash
echo -e "Test\nNova linija"
```

Shell **ne interpretira** `\n` ako je u dvostrukim navodnicima, već ga prosljeđuje echo naredbi kao literal string[^1].

### 2. Echo -e razina (druga interpretacija)

Echo naredba s `-e` opcijom **aktivira svoj parser** koji interpretira backslash sekvence:


| Escape sekvenca | Interpretacija | Rezultat |
| :-- | :-- | :-- |
| `\n` | Nova linija | Prelazak u novi red |
| `\t` | Tab karakter | Horizontalni tab |
| `\r` | Carriage return | Povratak na početak linije |
| `\b` | Backspace | Brisanje jednog znaka unatrag |
| `\\` | Literal backslash | Prikazuje \ |

## Razlika u interpretaciji navodnika

**Dvostruki navodnici:**

```bash
echo -e "Varijabla: $USER\nNova linija"
# Shell interpretira $USER, echo -e interpretira \n
```

**Jednostruki navodnici:**

```bash
echo -e 'Varijabla: $USER\nNova linija'
# Shell ne interpretira ništa, sve ide na echo -e
```


## ANSI escape sekvence za boje

Echo -e interpretira i **ANSI escape kodove** za kontrolu terminala[^4]:

```bash
echo -e "\033[31mCrveni tekst\033[0m"
# \033[31m → kod za crvenu boju
# \033[0m → reset na normalnu boju
```


### Struktura ANSI koda:

- `\033[` - ANSI escape sekvenca početak
- `31m` - kod boje (31 = crvena)
- Tekst koji se boji
- `\033[0m` - reset kod


## Escape karakter backslash

Backslash (`\`) služi kao **signal za escape interpretaciju**[^2][^3]:

```bash
# Bez escape - literal prikaz
echo "Tekst\n"
# Output: Tekst\n

# S echo -e - interpretacija
echo -e "Tekst\n"
# Output: 
# Tekst
# (novi red)

# Double escape za literal backslash
echo -e "Literal \\n tekst"
# Output: Literal \n tekst
```


## Praktični primjer interpretacije

```bash
#!/bin/bash

# Korak 1: Shell čita naredbu
VAR="Poruka"
echo -e "${VAR}:\n\t- Stavka 1\n\t- Stavka 2"

# Korak 2: Shell ekspandira varijablu
# Predaje echo-u: "Poruka:\n\t- Stavka 1\n\t- Stavka 2"

# Korak 3: Echo -e interpretira escape sekvence
# \n → novi red
# \t → tab
# Rezultat:
# Poruka:
#     - Stavka 1
#     - Stavka 2
```


## Specifični slučajevi interpretacije

**Problematični znakovi poput `\x1b`:**

```bash
echo -e "\x1b[2J"  # ANSI kod za brisanje ekrana
# Echo -e interpretira \x1b kao ESC karakter (0x1B)
```

**Zaštićavanje od interpretacije:**

```bash
# Korištenje printf umjesto echo za sigurniju kontrolu
printf '%s\n' "Tekst s \n koji neće biti interpretiran"
```

Ključno je razumjeti da **echo -e aktivira dodatni sloj interpretacije** escape sekvenci nakon što shell završi svoj parsing, omogućavajući naprednu kontrolu formatiranja terminala[^5].

<div style="text-align: center">⁂</div>

[^1]: https://stackoverflow.com/questions/37129699/escaping-rules-when-reading-in-bash

[^2]: https://mywiki.wooledge.org/BashGuide/SpecialCharacters

[^3]: https://tecadmin.net/handling-special-characters-in-shell-scripts/

[^4]: https://www.reddit.com/r/bash/comments/13uob2m/escape_value_x1b_echoing_problem/

[^5]: https://www.shellscript.sh/escape.html

[^6]: https://unix.stackexchange.com/questions/141312/how-to-escape-special-characters-in-a-string

[^7]: https://askubuntu.com/questions/1433229/how-do-i-echo-a-file-path-after-interpreting-characters-like-dots-and-tildes

[^8]: https://superuser.com/questions/1612281/why-does-writing-a-before-a-string-affect-how-bash-interprets-backslashes-in-i

[^9]: https://unix.stackexchange.com/questions/611419/how-does-the-escape-character-work-in-bash-prompt

[^10]: https://labex.io/questions/how-to-handle-special-characters-in-linux-file-names-17991

