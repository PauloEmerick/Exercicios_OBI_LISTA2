QUESTÃO 03

def overflow(NM, string):
    resultado = eval(string)
    if NM >= resultado:
        return True
    else:
        return False

print(overflow(10,'5 + 5'))

print(overflow(44,'23 * 2'))

print(overflow(323500,'42 * 35'))
