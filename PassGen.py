# -------------------------------------------------------------

print("\nPassword Generator")

# -------------------------------------------------------------

import random
import string

# -------------------------------------------------------------

##
#@fn list_to_string(list_to_convert)
#@brief This function converts "list_to_convert" in a string of characters.
#@param [list] list_to_convert
#@return [str] Returns the content of the list into a string.

def list_to_string(list_to_convert):
    converted = ""

    for i in list_to_convert:
        converted += str(i)
    return converted

##
#@fn ascii_lower(cantidad)
#@brief Esta función crea una lista de todas las letras minúsculas del abecedario.
#@param [int] cantidad -> Cantidad de letras que queremos que devuelva.
#@return [list] Devuelve una lista con letras random en minúscula.

def ascii_lower(cantidad):
    lista = []
    for i in range(0, cantidad):
        lower = random.randint(97, 122)
        lista.append(chr(lower))
    return lista

##
#@fn ascii_uppercase(cantidad)
#@brief Esta función crea una lista de todas las letras minúsculas del abecedario.
#@param [int] cantidad -> Cantidad de letras que queremos que devuelva.
#@return [list] Devuelve una lista con letras random en minúscula.

def ascii_uppercase(cantidad):
    lista = []
    for i in range(0, cantidad):
        uppercase = random.randint(65, 90)
        lista.append(chr(uppercase))
    return lista

def ascii_digit(cantidad):
    lista = []
    for i in range(0, cantidad):
        digit = random.randint(48, 57)
        lista.append(chr(digit))
    return lista

def ascii_symbols(cantidad):
    lista = []
    for i in range(0, cantidad):
        symbols = random.randint(33, 47)
        symbol_2 = random.randint(58, 64)
        symbol_3 = random.randint(91, 96)
        symbol_4 = random.randint(123, 126)
        lista.append(chr(symbols))
        lista.append(chr(symbol_2))
        lista.append(chr(symbol_3))
        lista.append(chr(symbol_4))
    return lista

# -------------------------------------------------------------

# Pin movil

randomlist = random.sample(range(0, 9), 6)
randomlist = list_to_string(randomlist)

print("\nContraseña móvil: %s" % randomlist)

# -------------------------------------------------------------

# Contraseña ordenador

length = 8
all = string.ascii_lowercase + string.digits
password = "".join(random.sample(all, length))

print("Contraseña ordenador: %s\n" % password)

# -------------------------------------------------------------

cantidad = 7
lower = ascii_lower(cantidad)
lower = list_to_string(lower)

cantidad = 3
upper = ascii_uppercase(cantidad)
upper = list_to_string(upper)

cantidad = 1
digit = ascii_digit(cantidad)
digit = list_to_string(digit)

cantidad = 1
symbol = ascii_symbols(cantidad)
symbol = list_to_string(symbol)

password = lower + upper + digit + symbol

print("\nContraseña ordenador: %s" % password)

# -------------------------------------------------------------

# print(string.punctuation)