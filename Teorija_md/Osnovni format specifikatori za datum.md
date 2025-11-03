<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Osnovni format specifikatori za datum

Umjesto `'+%A, %d %B %Y'` možete koristiti različite kombinacije format specifikatora[^1][^2]:

### Dan

| Format | Opis | Primjer |
| :-- | :-- | :-- |
| `%d` | Dan mjeseca (01-31) | `01, 15, 31` |
| `%A` | Puno ime dana | `Monday, Tuesday` |
| `%a` | Skraćeno ime dana | `Mon, Tue` |

### Mjesec

| Format | Opis | Primjer |
| :-- | :-- | :-- |
| `%m` | Mjesec kao broj (01-12) | `01, 06, 12` |
| `%B` | Puno ime mjeseca | `January, June` |
| `%b` | Skraćeno ime mjeseca | `Jan, Jun` |

### Godina

| Format | Opis | Primjer |
| :-- | :-- | :-- |
| `%Y` | Puna godina (4 cifre) | `2024` |
| `%y` | Skraćena godina (2 cifre) | `24` |

## Preddefinirane kombinacije

**Standardni formati:**[^1]

```bash
date +%D      # MM/DD/YY format (10/08/24)
date +%F      # YYYY-MM-DD format (2024-10-08)
date +%x      # Lokalizirani datum
```


## Vrijeme format specifikatori

| Format | Opis | Primjer |
| :-- | :-- | :-- |
| `%H` | Sat 24-satni format (00-23) | `14` |
| `%I` | Sat 12-satni format (01-12) | `02` |
| `%M` | Minuta (00-59) | `45` |
| `%S` | Sekunda (00-59) | `30` |
| `%p` | AM/PM indikator | `PM` |
| `%T` | Vrijeme HH:MM:SS format | `14:45:30` |

## Praktični primjeri različitih formata

**Europski stil:**

```bash
date '+%d.%m.%Y'           # 23.05.2025
date '+%d/%m/%Y'           # 23/05/2025
date '+%d-%m-%Y'           # 23-05-2025
```

**Američki stil:**

```bash
date '+%m/%d/%Y'           # 05/23/2025
date '+%B %d, %Y'          # May 23, 2025
```

**ISO format:**

```bash
date '+%Y-%m-%d'           # 2025-05-23
date '+%Y-%m-%d %H:%M:%S'  # 2025-05-23 14:53:00
```

**Opisni formati:**

```bash
date '+%A, %B %d, %Y'      # Friday, May 23, 2025
date '+%a %b %d %Y'        # Fri May 23 2025
date '+%d. %B %Y.'         # 23. May 2025.
```


## Kombinacije s vremenom

```bash
# Datum i vrijeme
date '+%d.%m.%Y %H:%M'     # 23.05.2025 14:53
date '+%A, %d %B %Y u %H:%M' # Friday, 23 May 2025 u 14:53

# 12-satni format
date '+%d/%m/%Y %I:%M %p'  # 23/05/2025 02:53 PM

# Kompletan format
date '+%A, %d. %B %Y. godine u %H:%M:%S' 
# Friday, 23. May 2025. godine u 14:53:00
```


## Specijalni formati

**Unix timestamp:**[^2]

```bash
date +%s                   # 1716468780
```

**RFC format:**[^1]

```bash
date -R                    # Fri, 23 May 2025 14:53:00 +0200
```

**UTC format:**

```bash
date -u '+%Y-%m-%d %H:%M:%S UTC'  # 2025-05-23 12:53:00 UTC
```


## Prilagođeni separatori

```bash
date '+%Y_%m_%d'           # 2025_05_23
date '+%d|%m|%Y'           # 23|05|2025
date '+%Y%m%d'             # 20250523 (bez separatora)
```

**Napomena:** Svi format specifikatori moraju počinjati s `+` znakom[^1][^2]. Za potpunu listu formatiranja koristite `man date` naredbu u terminalu.

<div style="text-align: center">⁂</div>

[^1]: https://phoenixnap.com/kb/linux-date-command

[^2]: https://www.scaler.com/topics/date-command-in-linux/

[^3]: https://www.putorius.net/linux-date-command.html

[^4]: https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings

[^5]: https://www.tutorialspoint.com/date-command-in-linux

[^6]: https://unix.stackexchange.com/questions/686551/where-can-i-find-a-complete-list-of-format-specifiers-for-the-date-command

[^7]: https://www.baeldung.com/linux/date-command

[^8]: https://www.redhat.com/en/blog/formatting-date-command

[^9]: https://labex.io/es/tutorials/linux-linux-date-command-with-practical-examples-422628

[^10]: https://www.prepbytes.com/blog/linux/date-command-linux-examples/

