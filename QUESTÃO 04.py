QUESTÃO 04

def garcom(entregar, lista):
    quebrados = 0
    for c in lista:
        lata = c[0]
        copo = c[1]
        if lata > copo:
           quebrados += copo
    return quebrados

#print(garcom (3, [(10,5),(6,8),(3,3)]))

#print(garcom (4, [(10,6),(8,8),(5,1),(100,100)]) )
