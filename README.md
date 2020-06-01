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
