# DAG de estudos de Matematica para o ENEM

Este DAG organiza uma sequencia de estudos para Matematica e suas Tecnologias no ENEM. A lista de conteudos parte do arquivo `objetos_de_conhecimento.pdf`; a orientacao das dependencias usa como fonte de verdade o grafo em `graphify-out/graph.json`, filtrando apenas nos matematicos e ignorando os nos oriundos de `CLAUDE.md`.

As arestas devem ser lidas como:

```text
pre-requisito -> conteudo dependente
```

## Metodologia

- O grafo menor de metadados/coding foi removido: `Behavioral Guidelines`, `Think Before Coding`, `Simplicity First`, `Surgical Changes`, `Goal-Driven Execution` e relacionados.
- Conteudos oficiais muito amplos foram fragmentados para melhorar a granularidade de estudo.
- Quando o graphify apresentou uma associacao forte entre dois conteudos, a dependencia foi orientada do conteudo mais elementar para o mais aplicado.
- Quando a aresta do graphify era associativa, mas nao definia direcao, a direcao foi definida por pre-requisito matematico e pelo texto oficial do PDF.
- Pesos e hiperarestas citados na tabela vieram de `graphify-out/graph.json`.

## Nos raiz

Estes conteudos nao possuem pais no DAG e podem iniciar o estudo:

- Aritmetica
- Plano cartesiano
- Teoria dos conjuntos
- Leitura de tabelas

## Nos terminais

Estes conteudos nao possuem filhos no DAG e representam pontos de chegada da trilha:

- Circunferencias
- Circunferencia no plano
- Dispersao: desvios e variancia
- Funcao quadratica
- Funcao logaritmica
- Funcao trigonometrica
- Inequacoes
- Matematica financeira
- Paralelismo e perpendicularidade
- Probabilidade
- Progressao aritmetica
- Simetrias planas e espaciais
- Geometria espacial

## Ordem topologica sugerida

### Bloco 1 - Fundamentos

1. Aritmetica
2. Plano cartesiano
3. Teoria dos conjuntos
4. Leitura de tabelas
5. Sistemas de numeracao
6. Numeros naturais e inteiros

### Bloco 2 - Numeros, proporcoes e medidas

1. Numeros racionais e fracoes
2. Numeros reais
3. Divisibilidade, MMC e MDC
4. Potenciacao e radiciacao
5. Razao e proporcao
6. Grandezas, medidas e escalas
7. Porcentagem e juros

### Bloco 3 - Algebra basica e representacoes

1. Equacoes
2. Sequencias e series
3. Principios de contagem
4. Interpretacao de graficos
5. Sistemas de equacoes
6. Graficos e funcoes
7. Inequacoes

### Bloco 4 - Funcoes e progressoes

1. Funcao afim
2. Funcao quadratica
3. Progressao aritmetica
4. Progressao geometrica
5. Funcao exponencial
6. Logaritmos
7. Funcao logaritmica
8. Matematica financeira

### Bloco 5 - Geometria

1. Geometria plana
2. Angulos e posicoes de retas
3. Semelhanca, congruencia e Tales
4. Relacoes metricas nos triangulos
5. Trigonometria do angulo agudo
6. Ciclo trigonometrico
7. Funcao trigonometrica
8. Circunferencias
9. Simetrias planas e espaciais
10. Geometria espacial

### Bloco 6 - Estatistica, probabilidade e geometria analitica

1. Estatistica descritiva
2. Media, moda e mediana
3. Desvios e variancia
4. Analise combinatoria
5. Probabilidade
6. Geometria analitica
7. Retas no plano
8. Paralelismo e perpendicularidade
9. Circunferencia no plano

## Arestas do DAG

| Pre-requisito | Conteudo | Evidencia |
|---|---|---|
| Aritmetica | Sistemas de numeracao | PDF: conhecimentos numericos; graphify liga sistemas de numeracao a contagem/potencias |
| Aritmetica | Numeros naturais e inteiros | PDF: operacoes em conjuntos numericos |
| Numeros naturais e inteiros | Numeros racionais e fracoes | PDF: progressao dos conjuntos numericos |
| Numeros racionais e fracoes | Numeros reais | PDF: progressao dos conjuntos numericos |
| Numeros naturais e inteiros | Divisibilidade, MMC e MDC | PDF: divisibilidade; graphify inclui MMC e MDC |
| Numeros reais | Potenciacao e radiciacao | Graphify: numeros reais + potenciacao |
| Divisibilidade, MMC e MDC | Razao e proporcao | Pre-requisito operacional para simplificacao de razoes |
| Numeros racionais e fracoes | Razao e proporcao | Graphify: fracoes + razao e proporcao |
| Razao e proporcao | Porcentagem e juros | Graphify peso 6 |
| Porcentagem e juros | Matematica financeira | Graphify peso 5 |
| Razao e proporcao | Matematica financeira | Graphify peso 7 |
| Potenciacao e radiciacao | Funcao exponencial | Pre-requisito matematico; graphify liga potenciacao/radicacao a funcoes avancadas |
| Potenciacao e radiciacao | Logaritmos | Graphify: potencias + logaritmo |
| Aritmetica | Sequencias e series | PDF: sequencias e progressoes |
| Sequencias e series | Progressao aritmetica | Graphify: PA + sequencias |
| Sequencias e series | Progressao geometrica | Graphify peso 3 |
| Potenciacao e radiciacao | Progressao geometrica | Graphify: potenciacao + PG |
| Progressao geometrica | Funcao exponencial | Graphify peso 4 |
| Aritmetica | Principios de contagem | PDF: principios de contagem |
| Sistemas de numeracao | Principios de contagem | Graphify: sistemas de numeracao + contagem |
| Principios de contagem | Analise combinatoria | Fragmentacao natural do objeto oficial |
| Potenciacao e radiciacao | Analise combinatoria | Graphify hyperedge he_008 |
| Aritmetica | Equacoes | Pre-requisito algebrico |
| Equacoes | Inequacoes | PDF: equacoes e inequacoes |
| Equacoes | Sistemas de equacoes | Graphify peso 2 |
| Razao e proporcao | Sistemas de equacoes | Graphify peso 2 |
| Equacoes | Graficos e funcoes | Pre-requisito algebrico |
| Plano cartesiano | Graficos e funcoes | PDF: graficos e funcoes; plano cartesiano |
| Graficos e funcoes | Funcao afim | PDF: funcao algebrica do 1o grau |
| Equacoes | Funcao afim | Graphify peso 1 |
| Funcao afim | Funcao quadratica | Graphify peso 5 |
| Equacoes | Funcao quadratica | Graphify peso 7 |
| Logaritmos | Funcao logaritmica | PDF: funcao logaritmica |
| Funcao exponencial | Funcao logaritmica | Graphify peso 2 |
| Trigonometria do angulo agudo | Ciclo trigonometrico | PDF: trigonometria e ciclo trigonometrico |
| Ciclo trigonometrico | Funcao trigonometrica | PDF: relacoes no ciclo e funcoes trigonometricas |
| Razao e proporcao | Grandezas, medidas e escalas | Graphify peso 6 |
| Grandezas, medidas e escalas | Geometria plana | Graphify peso 6 |
| Geometria plana | Angulos e posicoes de retas | PDF: angulos e posicoes de retas |
| Angulos e posicoes de retas | Semelhanca, congruencia e Tales | PDF: semelhanca, congruencia e Tales |
| Razao e proporcao | Semelhanca, congruencia e Tales | Graphify liga razao/proporcao a semelhanca |
| Semelhanca, congruencia e Tales | Relacoes metricas nos triangulos | PDF: relacoes metricas nos triangulos |
| Relacoes metricas nos triangulos | Trigonometria do angulo agudo | PDF: trigonometria do angulo agudo |
| Geometria plana | Circunferencias | PDF: circunferencias |
| Geometria plana | Simetrias planas e espaciais | PDF: simetrias |
| Grandezas, medidas e escalas | Geometria espacial | Graphify peso 1 |
| Geometria plana | Geometria espacial | Graphify peso 1 |
| Trigonometria do angulo agudo | Geometria espacial | Graphify peso 4 |
| Leitura de tabelas | Interpretacao de graficos | Graphify peso 2 |
| Interpretacao de graficos | Estatistica descritiva | Graphify peso 2 |
| Estatistica descritiva | Media, moda e mediana | PDF: medidas de tendencia central |
| Media, moda e mediana | Desvios e variancia | PDF: desvios e variancia |
| Teoria dos conjuntos | Probabilidade | Graphify peso 3 |
| Analise combinatoria | Probabilidade | Graphify hyperedge he_001 |
| Leitura de tabelas | Probabilidade | Graphify peso 9 |
| Interpretacao de graficos | Probabilidade | Graphify peso 8 |
| Estatistica descritiva | Probabilidade | Graphify: estatistica + probabilidade |
| Plano cartesiano | Geometria analitica | PDF: plano cartesiano |
| Geometria plana | Geometria analitica | Graphify peso 2 |
| Geometria analitica | Retas no plano | PDF: retas |
| Retas no plano | Paralelismo e perpendicularidade | PDF: paralelismo e perpendicularidade |
| Geometria analitica | Circunferencia no plano | PDF: circunferencias no plano |
| Sistemas de equacoes | Geometria analitica | PDF: sistemas de equacoes em contexto algebrico-geometrico |
| Funcao afim | Geometria analitica | Graphify peso 3 |
| Grandezas, medidas e escalas | Interpretacao de graficos | Graphify peso 4 |
| Funcao afim | Matematica financeira | Graphify peso 6 |
| Progressao geometrica | Matematica financeira | Graphify peso 3 |

## Cobertura dos objetos oficiais

- Conhecimentos numericos: cobertos por aritmetica, conjuntos numericos, divisibilidade, razao/proporcao, porcentagem/juros, sequencias/progressoes e contagem.
- Conhecimentos geometricos: cobertos por grandezas/medidas, geometria plana, angulos/retas, semelhanca/Tales, relacoes metricas, circunferencias, trigonometria, simetrias e geometria espacial.
- Estatistica e probabilidade: cobertos por tabelas, graficos, estatistica descritiva, tendencia central, dispersao, teoria dos conjuntos, combinatoria e probabilidade.
- Conhecimentos algebricos: cobertos por equacoes, inequacoes, graficos/funcoes e funcoes afim, quadratica, exponencial, logaritmica e trigonometrica.
- Conhecimentos algebrico-geometricos: cobertos por plano cartesiano, geometria analitica, retas, circunferencias, paralelismo/perpendicularidade e sistemas de equacoes.

## Arquivos renderizaveis

O grafo interativo esta em:

```text
dag_estudos_enem_math.html
```

O grafo DOT/Graphviz esta em:

```text
dag_estudos_enem_math.dot
```
