# Computação 1 | UFRJ

## Professor Francisco José Rodrigues da Silva Junior

### Período 2026.1

Repositório destinado à organização das atividades práticas, exercícios, desafios e trabalhos desenvolvidos na disciplina **Computação 1**, cursada na UFRJ.

O objetivo deste repositório é registrar minha evolução na linguagem **Python**, reunindo códigos, anotações e resoluções comentadas ao longo do período.

---

## Sobre a disciplina

A disciplina de **Computação 1** introduz conceitos fundamentais de programação, com foco em raciocínio lógico, construção de algoritmos e implementação de soluções utilizando Python.

Durante as aulas e atividades práticas, são trabalhados temas como:

- entrada e saída de dados;
- variáveis e tipos de dados;
- conversão de tipos;
- operações matemáticas;
- expressões booleanas;
- estruturas condicionais;
- listas, tuplas e dicionários;
- funções básicas do Python;
- uso de bibliotecas;
- aplicações computacionais em problemas científicos e de engenharia.

---

## Tecnologias utilizadas

```bash
Python 3
Google Colab
VS Code
Git
GitHub
```

---

## Como executar os arquivos

Para executar um arquivo Python pelo terminal, entre na pasta do projeto e use:

```bash
prompt> python3 nome_do_arquivo.py
```

Exemplo:

```bash
prompt> python3 calculadora_viagem_py.py
```

Algumas atividades também podem ser executadas em ambientes como **Google Colab** ou **Jupyter Notebook**.

---

## Organização do repositório

```bash
computacao-1-ufrj/
│
├── README.md
│
├── semana-01/
│   ├── desafio_primeiros_passos.py
│   └── calculadora_viagem_py.py
│
├── aula-04/
│   ├── exercicios_aula_4.py
│   └── calculando_desvio_padrao.py
│
├── aula-06/
│   └── listas_tuplas_dicionarios.py
│
├── aula-07/
│   └── pratica_listas_tuplas_dicionarios.py
│
└── avaliacao-01/
    └── trabalho_valendo_1_ponto.py
```

---

## Atividades práticas

| Atividade | Tema principal | Descrição |
|---|---|---|
| Desafio Primeiros Passos | Operações matemáticas e lógica | Exercícios introdutórios envolvendo precedência de operadores, valores booleanos e problemas aritméticos simples. |
| Calculadora de Viagem | Entrada de dados, casting e condicionais | Programa que calcula o custo total de uma viagem e verifica se o orçamento disponível é suficiente. |
| Exercícios Aula 4 | Estatística com Python | Cálculo de média, moda, desvio padrão, coeficiente de variação e histogramas. |
| Desvio Padrão | Estatística aplicada | Cálculo do desvio padrão amostral a partir de medições de radiação. |
| Aula 6 | Listas, tuplas e dicionários | Introdução aos principais tipos avançados de dados em Python. |
| Aula 7 | Prática com estruturas de dados | Aplicações envolvendo listas, tuplas e dicionários em problemas de química, física, engenharia e gestão. |
| Trabalho Avaliação 1 | Revisão geral | Lista prática com entrada de dados, operações matemáticas, listas, tuplas, algoritmos e estruturas de dados. |

---

# Semana 1 — Primeiros passos em Python

## Objetivo

A primeira etapa da disciplina foi voltada à familiarização com a linguagem Python, trabalhando operações matemáticas, tipos booleanos e resolução de problemas simples.

## Conceitos trabalhados

- operadores aritméticos;
- precedência de operadores;
- expressões booleanas;
- valores `True` e `False`;
- resolução sequencial de problemas;
- interpretação de enunciados.

## Exemplo de execução

```python
A_1 = (4 / 2) + (2 / 4)
A_2 = 4 / 2 + 2 / 4

print(A_1)
print(A_2)
```

## Comentário

Esse tipo de exercício é importante porque mostra que pequenos detalhes na escrita de uma expressão podem alterar, ou não, o resultado final. Em programação, entender a ordem das operações é essencial para evitar erros lógicos.

---

# Desafio — Sistema de Auxílio ao Orçamento de Viagens

## Descrição do programa

Este programa recebe dados de uma viagem e calcula se ela é financeiramente viável.

O usuário informa:

- orçamento disponível;
- destino desejado;
- valor da passagem;
- custo diário da hospedagem em euros;
- duração da viagem em dias.

A partir disso, o programa converte a hospedagem para reais, calcula o custo total da viagem e informa se o orçamento é suficiente.

## Exemplo de execução

```bash
prompt> python3 calculadora_viagem_py.py

Olá, Mariana! Planejando a próxima aventura? Deixa eu te ajudar com isso, digite o valor disponível, em reais: 8000
Hm, temos um bom orçamento para começar... e qual o destino dos sonhos que você cogitou? Digite aqui: Paris
Uauu, que sonho! Qual o valor da passagem para esse destino iradíssimo? Me conte aqui: 3500
Já consigo sentir o frio europeu daqui, agora me conte sobre o custo diário da hospedagem, em euros: 70
Para finalizar, Mariana! Quantos dias de aventura você está planejando? Fale por aqui: 5

===== RESUMO DA VIAGEM =====
Destino: Paris
Valor total da hospedagem em reais: R$ 2135.00
Custo total da viagem em reais: R$ 5635.00
Status do orçamento: Orçamento possível
Status final da viagem: Viável
Viável: True
Sobram R$ 2365.00 no orçamento.
```

## Conceitos aplicados

- `input()`;
- `float()`;
- `int()`;
- variáveis;
- operadores matemáticos;
- estruturas condicionais;
- operadores lógicos;
- f-strings;
- formatação de casas decimais.

---

# Aula 4 — Estatística com Python

## Objetivo

A Aula 4 trabalhou o uso de Python para resolver problemas de estatística básica e análise de dados.

## Conteúdos praticados

- média;
- moda;
- desvio padrão amostral;
- histogramas de frequência;
- coeficiente de variação;
- interpretação de estabilidade e variabilidade de dados.

## Aplicações desenvolvidas

Os exercícios envolveram situações aplicadas, como:

- análise de vazão de um poço de petróleo;
- validação de concentração de nitrato em água;
- resistência mecânica de uma liga metálica;
- velocidades experimentais de partículas;
- construção de histogramas.

## Exemplo de estrutura

```python
import numpy as np

dados = [2, 5, 3, 4, 6]

media = np.mean(dados)
desvio = np.std(dados, ddof=1)

print("Média:", media)
print("Desvio padrão amostral:", desvio)
```

## Comentário

Essa aula conecta programação com análise de dados. Para um estudante de engenharia, esse tipo de aplicação é importante porque permite interpretar medições, avaliar estabilidade de processos e identificar variações relevantes em experimentos.

---

# Aula 6 — Listas, tuplas e dicionários

## Objetivo

A Aula 6 apresentou estruturas de dados fundamentais em Python: listas, tuplas e dicionários.

## Lista

Listas são estruturas ordenadas e mutáveis. Isso significa que seus elementos podem ser acessados por posição e também podem ser alterados.

```python
frutas = ["apple", "banana", "cherries"]

print(frutas[1])
frutas.append("orange")
print(frutas)
```

## Tupla

Tuplas são estruturas ordenadas e imutáveis. Depois de criadas, seus valores não podem ser alterados diretamente.

```python
coordenadas = (4, 5, 6)

print(coordenadas[0])
print(type(coordenadas))
```

## Dicionário

Dicionários armazenam informações no formato chave-valor.

```python
instruments = {
    "john": "guitar",
    "paul": "bass"
}

print(instruments["john"])
print(instruments.keys())
print(instruments.values())
```

## Diferença entre lista, tupla e dicionário

| Estrutura | Característica principal | Exemplo de uso |
|---|---|---|
| Lista | Mutável e ordenada | Armazenar dados que podem mudar |
| Tupla | Imutável e ordenada | Armazenar medições fixas |
| Dicionário | Organizado por chave e valor | Relacionar nomes a informações |

---

# Aula 7 — Prática com listas, tuplas e dicionários

## Objetivo

A Aula 7 aplicou listas, tuplas e dicionários em problemas práticos, aproximando a programação de situações reais de ciência, engenharia e gestão.

## Exemplos de aplicações

- soma de listas;
- uso de `zip`;
- uso de `zip_longest`;
- consumo de reagentes químicos;
- crescimento de bactérias;
- tensões em materiais;
- velocidade de partículas;
- estoque de reagentes;
- controle de projetos ativos e inativos.

## Exemplo com listas

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

soma = [a + b for a, b in zip(lista1, lista2)]

print("A soma é:", soma)
```

## Exemplo com tuplas

```python
v0 = (2.0, 3.0, 4.0)
a = (1.0, 0.5, -1.0)
t = 2

vf = tuple(v0_i + a_i * t for v0_i, a_i in zip(v0, a))

print("Velocidade final:", vf)
```

## Exemplo com dicionários

```python
estoque = {
    "NaCl": 500,
    "H2SO4": 300,
    "KOH": 200
}

consumo = {
    "NaCl": 50,
    "H2SO4": 100,
    "KOH": 50
}

estoque_pos_consumo = {
    reagente: estoque[reagente] - consumo[reagente]
    for reagente in estoque
}

print("Estoque após o consumo:", estoque_pos_consumo)
```

---

# Trabalho valendo 1 ponto — Avaliação 1

## Descrição

O trabalho da Avaliação 1 reúne exercícios de revisão sobre os principais conteúdos iniciais da disciplina.

## Questões trabalhadas

1. Ler um número inteiro e imprimi-lo.
2. Ler uma string e imprimi-la.
3. Ler três valores inteiros e imprimir o produto.
4. Converter temperatura de Celsius para Fahrenheit.
5. Diferenciar lista, tupla e dicionário.
6. Calcular aumento salarial de 25%.
7. Somar listas.
8. Calcular velocidade final de uma partícula em três dimensões.
9. Imprimir números pares de 0 a 50.
10. Definir algoritmo e algoritmo sequencial.

## Exemplo — conversão de Celsius para Fahrenheit

```python
celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * (9.0 / 5.0) + 32.0

print("Temperatura em Fahrenheit:", fahrenheit)
```

## Exemplo — aumento salarial

```python
salario = float(input("Digite o salário atual: "))

novo_salario = salario * 1.25

print("Novo salário:", novo_salario)
```

## Exemplo — números pares de 0 a 50

```python
pares = list(range(0, 51, 2))

print(pares)
```

---

# Perguntas teóricas

## O que é um algoritmo?

Um algoritmo é uma sequência organizada de passos criada para resolver um problema ou executar uma tarefa.

Na programação, o algoritmo funciona como o plano lógico antes ou durante a escrita do código. Ele define o que deve ser feito, em qual ordem e com quais condições.

Exemplo simples:

```text
1. Receber um número.
2. Multiplicar esse número por 2.
3. Mostrar o resultado.
```

## O que é um algoritmo sequencial?

Um algoritmo sequencial é aquele em que as instruções são executadas uma após a outra, na ordem em que aparecem.

Ele não possui desvios, repetições ou decisões complexas. O programa simplesmente segue uma sequência linear de comandos.

Exemplo:

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Nome:", nome)
print("Idade:", idade)
```

## Qual é a diferença entre `input()`, `int()` e `float()`?

A função `input()` recebe dados digitados pelo usuário, mas sempre retorna esses dados como texto, isto é, como uma string.

Quando precisamos fazer cálculos, usamos conversão de tipo:

```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

- `int()` converte para número inteiro;
- `float()` converte para número decimal;
- `input()` apenas lê o dado digitado.

## Por que listas, tuplas e dicionários são importantes?

Essas estruturas permitem armazenar vários dados em uma única variável.

- Listas são úteis quando os dados podem mudar.
- Tuplas são úteis quando os dados devem permanecer fixos.
- Dicionários são úteis quando queremos associar uma chave a um valor.

Essas estruturas tornam o código mais organizado e permitem resolver problemas mais próximos de situações reais.

---

# Principais aprendizados

Ao longo das atividades, foram praticados fundamentos importantes de programação em Python:

- escrever comandos básicos;
- receber dados do usuário;
- converter tipos;
- fazer operações matemáticas;
- trabalhar com listas, tuplas e dicionários;
- interpretar problemas aplicados;
- transformar enunciados em código;
- organizar soluções de forma clara;
- comentar códigos para facilitar a leitura.

---

# Observação

Este repositório será atualizado ao longo do período com novas atividades práticas, desafios semanais, trabalhos e projetos desenvolvidos na disciplina **Computação 1**.

