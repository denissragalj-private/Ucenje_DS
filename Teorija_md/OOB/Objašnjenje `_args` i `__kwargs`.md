<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Objašnjenje `*args` i `**kwargs`

## `*args` - Pozicijski argumenti

**`*args`** omogućava funkciji da primi **proizvoljan broj pozicijskih argumenata** (bez ključa). Zvjezdica `*` je ključna - ona govori Pythonu da "raspakira" argumente u **tuple**.

```python
def suma(*args):
    print(type(args))  # <class 'tuple'>
    return sum(args)

print(suma(1, 2, 3))        # 6
print(suma(1, 2, 3, 4, 5))  # 15
print(suma(10))             # 10
```

Unutar funkcije, `args` postaje tuple koji sadrži sve proslijeđene argumente.

## `**kwargs` - Keyword argumenti

**`**kwargs`** omogućava funkciji da primi **proizvoljan broj keyword argumenata** (ključ-vrijednost parovi). Dvije zvjezdice `**` raspakuju argumente u **dictionary**.

```python
def ispis_info(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for kljuc, vrijednost in kwargs.items():
        print(f"{kljuc}: {vrijednost}")

ispis_info(ime="Denis", godine=30, grad="Zagreb")
# ime: Denis
# godine: 30
# grad: Zagreb
```

Unutar funkcije, `kwargs` je dictionary s ključevima i vrijednostima.

## Kombinacija - Svi tipovi parametara

```python
def funkcija(obavezan, *args, default="test", **kwargs):
    print(f"Obavezan: {obavezan}")
    print(f"Args (tuple): {args}")
    print(f"Default: {default}")
    print(f"Kwargs (dict): {kwargs}")

funkcija("prvi", "drugi", "treći", default="custom", ime="Denis", grad="Zagreb")

# Output:
# Obavezan: prvi
# Args (tuple): ('drugi', 'treći')
# Default: custom
# Kwargs (dict): {'ime': 'Denis', 'grad': 'Zagreb'}
```


### VAŽAN REDOSLIJED parametara:

1. **Obavezni parametri** (`param`)
2. **`*args`** (pozicijski)
3. **Default parametri** (`param="default"`)
4. **`**kwargs`** (keyword)

## Praktični primjeri:

### 1. Wrapper funkcije (kao u dekoratorima):

```python
def wrapper(*args, **kwargs):
    # Proslijedi sve argumente dalje
    return func(*args, **kwargs)
```


### 2. Logger funkcija:

```python
def log(message, *args, level="INFO", **kwargs):
    print(f"[{level}] {message}")
    print(f"Dodatni args: {args}")
    print(f"Dodatni kwargs: {kwargs}")

log("Greška", "file.txt", 123, user="Denis", error_code=404)
```


### 3. Fleksibilna funkcija:

```python
def kreira_osobu(ime, prezime, *hobiji, **dodatno):
    osoba = {
        "ime": ime,
        "prezime": prezime,
        "hobiji": list(hobiji),
        "dodatno": dodatno
    }
    return osoba

osoba = kreira_osobu(
    "Denis", "Horvat",
    "programiranje", "gitara",
    godine=30, grad="Zagreb"
)
# {
#   'ime': 'Denis',
#   'prezime': 'Horvat',
#   'hobiji': ['programiranje', 'gitara'],
#   'dodatno': {'godine': 30, 'grad': 'Zagreb'}
# }
```


## Ime nije bitno!

Možeš koristiti bilo koje ime, ali **konvencija je `args` i `kwargs`**:

```python
def funkcija(*brojevi, **info):  # Radi isto!
    print(sum(brojevi))
    print(info)
```

**Zaključak:** `*args` pakira pozicijske argumente u tuple, a `**kwargs` pakira keyword argumente u dictionary. Ovo omogućava izradu fleksibilnih funkcija koje primaju različit broj argumenata, što je posebno korisno kod dekoratora, wrapper funkcija i API-ja.
<span style="display:none">[^1][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://realpython.com/python-kwargs-and-args/

[^2]: https://www.geeksforgeeks.org/python/args-kwargs-python/

[^3]: https://www.reddit.com/r/learnpython/comments/7dsn1s/what_are_args_and_kwargs/

[^4]: https://www.w3schools.com/python/python_args_kwargs.asp

[^5]: https://www.scaler.com/topics/python/args-and-kwargs-in-python/

[^6]: https://www.programiz.com/python-programming/args-and-kwargs

[^7]: https://book.pythontips.com/en/latest/args_and_kwargs.html

[^8]: https://stackoverflow.com/questions/1769403/what-is-the-purpose-and-use-of-kwargs

[^9]: https://www.youtube.com/watch?v=Vh__2V2tXUM

