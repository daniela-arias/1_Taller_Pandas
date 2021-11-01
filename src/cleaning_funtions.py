import re
def limpiar(x):
    diccionario = {"White shark":re.search(".*[Ww](hite|HITE).*",str(x)),
                   "Blue shark":re.search(".*[Bb](lue|LUE).*",str(x)),
                   "Tiger shark":re.search(".*[Tt](iger|IGER).*",str(x)),
                   "Lemon shark":re.search(".*[Ll](emon|EMON).*",str(x)),
                   "Grey shark":re.search(".*[Gg](rey|REY).*",str(x)),
                   "Wobbegong shark":re.search(".*[Ww](obbegong|OBBEGONG).*",str(x)),
                   "Galapagos shark":re.search(".*[Gg](alapagos|ALAPAGOS).*",str(x)),
                   "Nurse shark":re.search(".*[Nn](urse|URSE).*",str(x)),
                   "Porbeagle shark":re.search(".*[Pp](orbeagle|ORBEAGLE).*",str(x)),
                   "Sandtiger shark":re.search(".*[Ss](andtiger|ANDTIGER).*",str(x)),
                   "Unconfirmed shark attack":re.search(".*[Ii](nvovlement|NVOVLEMENT).*",str(x)),
                   "Sevengill shark":re.search(".*[Ss](evengill|EVENGILL).*",str(x)),
                   "Caribbean shark":re.search(".*[Cc](aribbean|ARIBBEAN).*",str(x))
                  }

    for key,values in diccionario.items():
        if values:
            return key
    return 'Others'