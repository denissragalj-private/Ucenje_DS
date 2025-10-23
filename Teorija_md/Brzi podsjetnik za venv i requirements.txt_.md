<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

### Brzi podsjetnik za venv i requirements.txt:

```bash
# === KREIRANJE I AKTIVACIJA VENV ===

# Kreiraj virtual environment
python -m venv venv

# Aktiviraj venv
# Na Windows:
venv\Scripts\activate

# Na Linux/Mac:
source venv/bin/activate

# Deaktiviraj venv (kada završiš)
deactivate


# === INSTALACIJA PAKETA ===

# Instaliraj pojedinačni paket
pip install naziv_paketa

# Instaliraj iz requirements.txt
pip install -r requirements.txt

# Ažuriraj paket
pip install --upgrade naziv_paketa

# Ažuriraj sve pakete
pip install --upgrade -r requirements.txt


# === REQUIREMENTS.TXT ===

# Kreiraj requirements.txt iz trenutnog venv-a
pip freeze > requirements.txt

# Vidi instalirane pakete
pip list

# Prikaži informacije o paketu
pip show naziv_paketa


# === BRISANJE ===

# Obriši paket
pip uninstall naziv_paketa

# Obriši sve pakete iz venv-a
pip freeze > to_delete.txt
pip uninstall -r to_delete.txt -y
rm to_delete.txt

# Obriši cijeli venv folder
# Na Windows:
rmdir /s venv

# Na Linux/Mac:
rm -rf venv
```

**Napomena:** Uvijek aktiviraj venv prije rada s paketima!

