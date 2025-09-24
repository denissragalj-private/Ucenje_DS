import random

# Mapa zamjene slova sa brojevima
leet_map = {
    'a': '4', 'b': '8', 'e': '3', 'g': '6',
    'i': '1', 'o': '0', 's': '5', 't': '7',
    'z': '2'
}

def to_leetspeak(word):
    # Zamjena slova u riječi prema mapi
    return ''.join(leet_map.get(char.lower(), char) for char in word)

def tipoglycemia_transform(text):
    def shuffle_middle(word):
        # Ako je riječ prekratka, vrati je nepromjenjenom
        if len(word) <= 3:
            return word
        # Prvo i posljednje slovo ostaju isto, sredina se miješa
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    
    # Razdvajamo tekst na riječi i primjenjujemo funkcije
    words = text.split()
    transformed_words = [
        to_leetspeak(shuffle_middle(word)) for word in words
    ]
    # return ' '.join(transformed_words).upper()  # Vrača text kao UPER CASSE
    return ' '.join(transformed_words)

if __name__ == "__main__":
    print("UNESITE TEKST KOJI ŽELITE PRETVORITI U TIPOGLIKEMIJSKI FORMAT:")
    user_input = input()
    result = tipoglycemia_transform(user_input.upper())
    print("\nTIPOGLIKEMIJSKI TEKST:\n")
    print(result)
