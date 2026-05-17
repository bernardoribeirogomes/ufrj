#Comentários realizados pelos alunos Bernardo Ribeiro e Gabriel Santiago

import numpy as np  # Importa o NumPy, porque o enunciado pede uma matriz NumPy, não uma lista comum.

# Cria a matriz de dados.
# Cada linha representa um sensor.
# Cada coluna representa uma leitura daquele sensor ao longo do dia.
dados = np.array([
    [25, 30, 35],   # Sensor 0
    [10, 85, 20],   # Sensor 1
    [45, 55, 60],   # Sensor 2
    [-5, 20, 25]    # Sensor 3
])

instaveis = []  # Lista onde vamos guardar apenas os índices dos sensores instáveis.

# Usamos for i in range(len(dados)) porque o exercício quer os índices dos sensores.
# Como cada linha da matriz é um sensor, i vai assumir os valores 0, 1, 2 e 3. | Bernardo
for i in range(len(dados)):

    # Guardamos dados[i] em uma variável chamada leituras para o código ficar mais legível.
    # Assim, evitamos repetir dados[i] várias vezes ao longo do programa.
    leituras = dados[i]

    # Criamos uma lista vazia de motivos.
    # Isso é importante porque um mesmo sensor pode ser instável por mais de um motivo.
    motivos = []

    # np.any(...) é usado quando queremos saber se existe pelo menos um valor
    # que viola a regra.
    # Aqui, verificamos se existe alguma leitura acima de 80°C.
    if np.any(leituras > 80):
        # Além de verificar se existe uma leitura acima de 80,
        # também salvamos exatamente quais valores causaram esse problema.
        valores_acima_80 = [int(valor) for valor in leituras[leituras > 80]]
        motivos.append(f"Leitura acima de 80°C: {valores_acima_80}")

    # Novamente usamos np.any(...), agora para verificar
    # se existe alguma leitura abaixo de 0°C.
    if np.any(leituras < 0):
        # Convertemos cada valor para int comum do Python
        # para a exibição não aparecer como np.int64(...)
        valores_abaixo_0 = [int(valor) for valor in leituras[leituras < 0]]
        motivos.append(f"Leitura abaixo de 0°C: {valores_abaixo_0}")

    # np.mean(...) calcula a média das leituras.
    # Usamos essa função porque um dos critérios de instabilidade
    # é ter média maior que 50°C.
    media = np.mean(leituras)

    if media > 50:
        # Guardamos a média formatada com duas casas decimais
        # para a saída ficar mais clara e mais bonita.
        motivos.append(f"Média instável: {media:.2f}°C")

    # Se a lista de motivos não estiver vazia,
    # significa que o sensor foi considerado instável por pelo menos um critério.
    if len(motivos) > 0:
        # Guardamos o índice do sensor na lista de instáveis,
        # porque o enunciado pede os índices.
        instaveis.append(i)

        # Exibimos o número do sensor.
        print(f"Sensor {i} está instável por:")

        # Percorremos todos os motivos encontrados para esse sensor.
        # Isso é importante porque um sensor pode falhar por mais de um motivo.
        for motivo in motivos:
            print(f"  - {motivo}")

# Ao final, mostramos a lista com os índices de todos os sensores instáveis.
print(f"Índices dos sensores instáveis: {instaveis}")
