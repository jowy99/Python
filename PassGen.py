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
