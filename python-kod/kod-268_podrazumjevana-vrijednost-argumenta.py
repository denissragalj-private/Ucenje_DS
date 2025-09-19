# def opseg_kruga(radijus, pi=3.14):
#     obujam = 2 * (radijus * pi)
#     return obujam


# print(opseg_kruga(3))

def pozdrav(naziv_karaktera=" Goku ", broj=2):
    print((naziv_karaktera) * broj)

pozdrav()                               #   Goku  Goku 

pozdrav(" Krilin ")                     #   Krilin  Krilin

pozdrav(" Belma ", broj = 4)            #   Belma  Belma  Belma  Belma

# iz ovoga vidimo da preddefinirane vrijednosti se kod korištenja mogu mijenjati !