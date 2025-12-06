# Python na Engenharia Química
Aprender programação em Python é uma ferramente indispensável para engenheiros químicos pois permite modelar, simular e otimizar processos com muito mais rapidez, precisão e autonomia.

A linguagem oferece bibliotecas robustas para cálculos numéricos, análise de dados e simulação, podendo ser utilizadas para resolução de problemas de fenômenos
de transporte, projeto de equipamentos, métodos iterativos e integração de balanços de massa e energia, além de ferramentas para machine learning aplicadas
ao desenvolvimento de soft sensors e controle avançado de processos.

Dominar Python possibilita substituir cálculos manuais repetitivos por rotinas confiáveis, automatizar análises laboratoriais, interpretar grandes volumes de
dados industriais, validar modelos termodinâmicos e cinéticos e criar interfaces e ferramentas próprias para tomada de decisão. Em um cenário onde a indústria 4.0
exige engenheiros capazes de integrar conhecimento técnico a habilidades computacionais, Python se torna uma competência central e diferencial na prática profissional
da engenharia química.

# Trocador de Calor Bitubular
O processo de aquecimento e resfriamento de fluidos é de extrema importância
para a indústria química, uma vez que garante condições adequadas de operação e maior
eficiência nos processos. Para tal finalidade, empregam-se os trocadores de calor,
equipamentos simples e de baixo custo, que possibilitam a transferência de energia térmica
entre dois fluidos de diferentes temperaturas, sem que haja contato direto entre eles.
(ÇENGEL, 2009).

Devido ao seu potencial de operação em larga escala, os trocadores de calor são
amplamente utilizados na indústria química, seja no controle de temperatura para otimizar
as taxas de reação, no ajuste das propriedades físicas de substâncias para garantir
segurança e eficiência, ou ainda na recuperação de calor proveniente de vapor residual de
plantas industriais (INCROPERA, 2019).

Com isso, realizou-se a modelagem de um trocador de calor bitubular, implementada em Python. O código calcula a eficiência térmica do trocador nos arranjos paralelo
e contracorrente e estima as temperaturas de saída das correntes quente e fria com base nos balanços de energia e na correlação efetividade–NTU correspondente ao tipo
de escoamento. O programa também permite interpolar propriedades da água quando necessário, automatizando as etapas de cálculo e fornecendo previsões consistentes
para diferentes condições operacionais.

<img src="https://i.imgur.com/QIK0RLr.jpeg" width="500">

# Resultados
O caso de estudo adotado para verificar a consistência do código foi o Experimento 4 da UC, permitindo comparar os resultados obtidos em Python com aqueles registrados na planilha Excel.
As diferenças observadas foram pequenas e podem ser atribuídas à precisão limitada dos dados de propriedades da água, declaradas apenas em intervalos de 20 °C, desconsiderando sua variação não linear com a temperatura,
a utilização da correlação de Reynolds simplicada, que causa grandes erros, além de possíveis inconsistências na definição das variáveis durante o cálculo.
Apesar dessas limitações, o código apresentou desempenho adequado, reproduzindo valores muito próximos dos experimentais e confirmando sua confiabilidade para aplicações didáticas e de modelagem térmica, como também,
a possibilidade de otimização para a implantação para prever a eficiencia esperada em uma linha de processos.

<img src="https://i.imgur.com/AQxl0YX.jpeg">
