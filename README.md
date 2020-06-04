# ExerciciosdaOBI2009
LIsta de exercicio da OBI2009

QUESTÃO 01

Para descontrair os alunos após as provas da OBI, a Diretora da escola organizou um campeonato de aviões de papel. Cada aluno participante receberá uma certa quantidade de folhas de um papel especial para fazer os seus modelos de aviões. A quantidade de folhas que cada aluno deverá receber ainda não foi determinada: ela será decidida pelos juízes do campeonato.

A diretora convidou, para atuarem como juízes, engenheiros da Embraer, uma das mais bem sucedidas empresas brasileiras, que vende aviões com tecnologia brasileira no mundo todo. O campeonato está programado para começar logo após a prova da OBI, mas os juízes ainda não chegaram à escola. A diretora está aflita, pois comprou uma boa quantidade de folhas de papel especial, mas não sabe se a quantidade comprada vai ser suficiente.

Considere, por exemplo, que a Diretora comprou 100 folhas de papel especial, e que há 33 competidores. Se os juízes decidirem que cada competidor tem direito a três folhas de papel, a quantidade comprada pela diretora é suficiente. Mas se os juízes decidirem que cada competidor tem direito a quatro folhas, a quantidade comprada pela diretora não seria suficiente.

Você deve escrever uma função chamada *avioes_de_papel* que, dados o número de competidores, o número de folhas de papel especial compradas pela Diretora e o número de folhas que cada competidor deve receber, determine se o número de folhas comprado pela Diretora é suficiente.

A sua função vai receber três números inteiros como argumentos. O primeiro argumento representa o número de competidores, o segundo argumento a quantidade de folhas de papel especial compradas pela Diretora e o terceiro argumento a quantidade de folhas de papel especial que cada competidor deve receber.

Sua função deve retornar True se a quantidade de folhas compradas pela Diretora é suficiente, ou False caso contrário.

Chamada da função ----------------------------------------->>>>Retorno da função 

avioes_de_papel(10,100,10)--------------------------------->>>>>> True 

avioes_de_papel(10,90,10)---------------------------------->>>>>> False 

avioes_de_papel(5,40,2)------------------------------------->>>>>> True




QUESTÃO 02

Aldo é um garoto muito esperto que adora promoções e sorteios. Como já participou de muitas promoções da forma
`para participar, envie n rótulos de produtos ...", Aldo tem o costume de guardar o rótulo de todos os produtos que
compra. Dessa forma, sempre que uma empresa faz uma promoção ele já tem um monte de rótulos para mandar.

A SBC (Super Balas e Caramelos) está fazendo uma nova promoção, e, como era de se esperar, Aldo quer
participar. Para participar da promoção é preciso enviar um envelope contendo um rótulo de cada tipo de bala que a
SBC produz. Por exemplo, se a SBC produz 3 tipos de balas, A, B, C, e uma pessoa tem 3 rótulos de A, 3 de B e 2
de C, ela pode enviar no máximo 2 envelopes, já que falta um rótulo de C para compor o terceiro envelope. Não há
limite para o número de envelopes que uma pessoa pode enviar.

Balas são a segunda coisa de que Aldo mais gosta (a primeira como você sabe são promoções). Por causa disso a
quantidade de rótulos de balas que ele tem é muito grande, e ele não está conseguindo determinar a quantidade
máxima de envelopes que ele pode enviar.

Como você é o melhor amigo de Aldo ele pediu sua ajuda para fazer o cálculo, de modo que ele compre o número
exato de envelopes. Você deve escrever uma função chamada *numero_envelopes* que, a partir da lista de rótulos
de Aldo, calcula o número máximo de envelopes válidos que ele pode enviar.

A sua função vai receber uma lista de números inteiros como o único argumento dela. Cada número nessa lista
representa uma quantidade de rótulos de balas que Aldo tem. O primeiro número nessa lista representa a
quantidade de rótulos do tipo 1 que Aldo possui, o segundo número representa a quantidade de rótulos do tipo 2, e
assim por diante, até o último número.

Sua função deve retornar um número inteiro que represente o número máximo de envelopes válidos que Ido pode
enviar.

Exemplos:
Chamada da função --------------->>>>>  Retorno da função

numero_envelopes([5,3,6,2])-------------------------->>>>>      2

numero_envelopes([10,5,21,3,0,11])-------------------->>>>      0


