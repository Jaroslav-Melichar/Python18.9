List=[5,6,77,45,22,12,24]

def NejvetsiCislo(list):
    nejvetsi=0
    for i in list:
        if i>nejvetsi:
            nejvetsi=i
    return nejvetsi
print(NejvetsiCislo(List))
################################################
List=[5,6,77,45,22,12,24]

def NejmensiCislo(list):
    nejmensi=list[0]
    for i in list:
        if i<nejmensi:
            nejmensi=i
    return nejmensi
print(NejmensiCislo(List))