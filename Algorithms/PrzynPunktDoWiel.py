from PrzynPunktDoOdc import *

def CzyNalezyDoWielokata(n, tab, punkt) -> bool:
    for i in range(n):
        if CzynalezyDoOdcinka(tab[i], tab[i+1], punkt, False):
            return True

#доделать