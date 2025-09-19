
# jan -> Januar
# feb -> Februar
# ako ne postoji kljuć, da dobijemo standardnu vrijednost

konverzija_mjeseci = {
    "jan": "Januar",
    "feb": "Februar",
    "apr": "April",
    "mar": "Mart",
    "maj": "Maj",
    "jun": "Juni",
    "jul": "Juli",
    "aug": "August",
    "sep": "Septembar",
    "oct": "Oktobar",
    "nov": "Novembar",
    "dec": "Decembar"
}

print(konverzija_mjeseci["apr"])                                # Aprril
print(konverzija_mjeseci["jun"])                                # Juni
print(konverzija_mjeseci.get("lim","Nepostoji takav mjesec"))   # Nepostoji takav mjesec     