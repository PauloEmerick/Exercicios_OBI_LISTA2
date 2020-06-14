QUESTÃO 05

def sedex(diametro, altura, largura, profundidade):
  for i in range(diametro):
    if altura < diametro:
      return False
    elif largura < diametro:
      return False
    elif profundidade < diametro:
      return False
    else:
      return True

#print(sedex(3,2,3,5))

#print(sedex(5,5,5,5))

#print(sedex(9,15,9,10))
