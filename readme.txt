Projeto Tech Challenge 3:

O projeto tem como objetivo analisar todos os voos que ocorreram nos EUA no ano de 2015, buscando insights sobre o sistema aéreo americano, principalmente em relação aos atrasos.
Como os arquivos são muito grandes, eles devem ser baixados e colocados na pasta 'raw'

Link para download: https://drive.google.com/drive/folders/1aS7exW5N0qq1uIxvIBcAfc18OHojOMjj

airlines.csv --> Planilha contendo o significado das siglaas
airports.csv --> Planilha contendo o significado dos aeroportos
flights.csv --> Planilha contendo as informações de voo

Após colocar esses arquivos na pasta 'raw', pode-se executar os seguintes passos em ordem:

1) pip install -r 'requirements.txt'
2) raw_analysis.py
3) pre_processing_raw.py
4) processed_analysis.py
5) PCA.py
6) ML.py

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

raw_analysis.py:

- Gera um arquivo raw_missing_values.txt, exibindo a quantidade de dados NaN em cada coluna de cada planilha.

Ao fazer uma análise dos dados brutos de airlies.csv, foi possível observar que não existem dados do tipo NaN
Ao fazer uma análise dos dados brutos de airports.csv, foi possível observar que faltavam os dados de Latitude e Longitude dos Aeroportos.
Ao fazer uma análise dos dados de flights.csv, foi possível observar que apesar de faltarem muitos dados, existem muitas colunas que podem ser tidas como desnecessárias, podendo serem excluidas sem que se percam dados valiosos.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

processing_raw.py

- Manipulação e processamento dos arquivos raw, gerando arquivos processados sem dados faltantes para as análises visuais e modelos de IA

Ao fazer o processamento de dados brutos de airlines.csv, renomeou-se as colunas e salvou o arquivo processado na pasta raw_processed.
Ao fazer o processamento de dados brutos de airports.csv, renomeou-se as colunas, então selecionou-se apenas as colunas: 'Código de Aeroporto', 'Aeroporto', 'Cidade' e 'Estado'. Salvou-se então o arquivo processado na pasta raw_processed.
Ao fazer o processamento de dados brutos de flights.csv, renomeou-se as colunas, então tomou-se as seguintes escolhas:

-- Excluiu-se a coluna: 'Ano' pois todas são referentes ao mesmo ano.
-- Excluiu-se a coluna 'Número do Voo', pois apesar de ser uma coluna boa para controle e consulta, é irrelevante para modelo de IA
-- Excluiu-se a coluna 'Número Aeronave' pois parece não haver correlação evidente entre a aeronave e o atraso
-- Excluiu-se a coluna 'Horário de Partida', pois o 'Horário Programado de Partida' já contem informação relevante e o 'Atraso de Partida' já contem a informação relativa ao atraso
-- Na coluna 'Atraso de Partida' preencheu-se os valores NaN com valor refernete a mediana
-- Excluiram-se as colunas: 'Tempo de Taxi até Decolagem' e 'Momento de Decolagem', POIS não parecem ser relevantes para explicar o atraso
-- As colunas 'Tempo de Voo Planejado', 'Tempo Total do Voo' e 'Tempo em Voo' parecem dizer as mesmas coisas, mas apenas 'Tempo de Voo Planejado' possui apenas 6 linhas faltando valores, então se removeu apenas essas linhas e excluiu-se as demais colunas.
-- Nas colunas 'Atraso de Chegada', 'Tempo de Atraso por Controle de Espaço Aéreo' e demais colunas de atraso, preencheu-se os valores NaN com valor referente a mediana
-- Retirou-se 0.5% dos dados de topo e 0.5% dos dados de fundo, tentando remover os outliers

Assim, manteve-se as colunas: 'Mês', 'Dia', 'Dia da Semana', 'Companhia Aérea', 'Aeroporto de Destino', 'Aeroporto de Origem', 'Horário Programado de Partida', 'Atraso de Partida', 'Tempo de Voo Planejado', 'Distância', 'Horário Previsto de Chegada', 'Atraso de Chegada', 'Cancelado'

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

processed_analysis.py

- A partir dos arquivo processed_flights.csv, calculou-se a média de atraso global e exibições visuais de correlações entre os dados que foram salvos na pasta 'processed_analysis'

insights:

-- Dia 17 e dia 18 parecem ter as maiores tendências de atraso.
-- Os meses Janeiro, Feveiro, Junho, Julho e Dezembro parecem ser meses com maior tendência a atrasos, provavelmente devido a ser uma época com mais voos
-- Junho parece ser o mês com maior tendência de atraso, enquanto setembro e outubro parecem mais propensos a adiantamentos
-- Domingo parece ser o dia com mais tendência de atraso
-- As companhias F9 (Frontier Airlines) e NK (Spirit Air Lines) parecem ter maior tendência a atrasos 
-- Quanto maior o tempo de voo, maior a tendência da aeronave atrasar muito ou adiantar muito
-- O heatmap parece indicar que existe uma correlação maior entre o horário da partida / horário da chegada e os atrasos
-- Os horários a partir de 17:00 até 20:00 parecem incidir em maiores atrasos, provavelmente devido ao transito que afeta tanto operadores de aeroporto, quanto tripulantes 

Além disso foi possível observar as correlações de cada coluna com a coluna alvo, sendo possível identificar as colunas mais interessantes para a construção de modelos de ML.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PCA.py




-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ML.py

Uma vez que a coluna 'Aeroporto de Origem' e 'Aeroporto de Destino' parecem ter misturas entre categorias e números, elas foram excluidas da análise.
Buscou-se trabalhar com um ML de classificação, ou seja, não tenta se prever quanto um voo poderia atrasar, mas se ele atrasaria ou não.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





