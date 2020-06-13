QUESTÃO 01

def avioes_de_papel(competidores, compradas, recebidas ):
    falhou = False
    verdadeiro = True
    total = competidores * recebidas
    #
    if total > compradas:
      return falhou
    else:
      return verdadeiro

#print(avioes_de_papel (10,100,10))

#print(avioes_de_papel (10,90,10))

#print(avioes_de_papel(5, 40, 2))
