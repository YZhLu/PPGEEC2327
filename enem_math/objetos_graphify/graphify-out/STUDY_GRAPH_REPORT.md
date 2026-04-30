# Graph Report - /Users/yzhlu/Documents/PHD/2026-1/PPGEEC2327_-_topicos_4_-_T01/enem/objetos_graphify  (2026-04-24)

## Corpus Check
- Study DAG is pedagogical inference built on top of the extracted taxonomy.

## Summary
- 43 nodes · 82 edges · 7 communities detected
- Extraction: 0% EXTRACTED · 100% INFERRED · 0% AMBIGUOUS · INFERRED: 82 edges (avg confidence: 0.83)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Fase 1 - Base numérica|Fase 1 - Base numérica]]
- [[_COMMUNITY_Fase 2 - Proporção, variação e contagem|Fase 2 - Proporção, variação e contagem]]
- [[_COMMUNITY_Fase 3 - Dados e probabilidade|Fase 3 - Dados e probabilidade]]
- [[_COMMUNITY_Fase 4 - Geometria plana e medidas|Fase 4 - Geometria plana e medidas]]
- [[_COMMUNITY_Fase 5 - Triângulos, círculos e trigonometria|Fase 5 - Triângulos, círculos e trigonometria]]
- [[_COMMUNITY_Fase 6 - Álgebra e plano cartesiano|Fase 6 - Álgebra e plano cartesiano]]
- [[_COMMUNITY_Fase 7 - Funções e integração algébrica|Fase 7 - Funções e integração algébrica]]

## God Nodes (most connected - your core abstractions)
1. `Fase 2 - Proporção, variação e contagem` - 10 edges
2. `Fase 6 - Álgebra e plano cartesiano` - 10 edges
3. `Fase 4 - Geometria plana e medidas` - 9 edges
4. `Fase 5 - Triângulos, círculos e trigonometria` - 8 edges
5. `Fase 7 - Funções e integração algébrica` - 8 edges
6. `Trilha sugerida de estudo` - 7 edges
7. `Fase 1 - Base numérica` - 7 edges
8. `Fase 3 - Dados e probabilidade` - 6 edges
9. `Funções algébricas do 1.º e do 2.º graus` - 6 edges
10. `Operações em conjuntos numéricos` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Fase 1 - Base numérica` --study_block_contains--> `Fatoração`  [INFERRED]
  build_study_dag.py → objetos_de_conhecimento.pdf
- `Fase 2 - Proporção, variação e contagem` --study_block_contains--> `Porcentagem e juros`  [INFERRED]
  build_study_dag.py → objetos_de_conhecimento.pdf
- `Fase 2 - Proporção, variação e contagem` --study_block_contains--> `Sequências e progressões`  [INFERRED]
  build_study_dag.py → objetos_de_conhecimento.pdf
- `Fase 2 - Proporção, variação e contagem` --study_block_contains--> `Princípios de contagem`  [INFERRED]
  build_study_dag.py → objetos_de_conhecimento.pdf
- `Fase 3 - Dados e probabilidade` --study_block_contains--> `Representação e análise de dados`  [INFERRED]
  build_study_dag.py → objetos_de_conhecimento.pdf

## Communities

### Community 0 - "Fase 1 - Base numérica"
Cohesion: 0.7
Nodes (5): Fase 1 - Base numérica, Operações em conjuntos numéricos, Divisibilidade, Fatoração, Desigualdades

### Community 1 - "Fase 2 - Proporção, variação e contagem"
Cohesion: 0.47
Nodes (6): Fase 2 - Proporção, variação e contagem, Razões e proporções, Porcentagem e juros, Relações de dependência entre grandezas, Sequências e progressões, Princípios de contagem

### Community 2 - "Fase 3 - Dados e probabilidade"
Cohesion: 0.6
Nodes (5): Fase 3 - Dados e probabilidade, Representação e análise de dados, Medidas de tendência central, Desvios e variância, Noções de probabilidade

### Community 3 - "Fase 4 - Geometria plana e medidas"
Cohesion: 0.43
Nodes (7): Fase 4 - Geometria plana e medidas, Características das figuras geométricas planas e espaciais, Grandezas, unidades de medida e escalas, Comprimentos, áreas e volumes, Ângulos, Posições de retas, Simetrias de figuras planas ou espaciais

### Community 4 - "Fase 5 - Triângulos, círculos e trigonometria"
Cohesion: 0.53
Nodes (6): Fase 5 - Triângulos, círculos e trigonometria, Teorema de Tales, Congruência e semelhança de triângulos, Relações métricas nos triângulos, Circunferências, Trigonometria do ângulo agudo

### Community 5 - "Fase 6 - Álgebra e plano cartesiano"
Cohesion: 0.48
Nodes (7): Fase 6 - Álgebra e plano cartesiano, Plano cartesiano, Retas, Paralelismo e perpendicularidade, Gráficos e funções, Equações e inequações, Sistemas de equações

### Community 6 - "Fase 7 - Funções e integração algébrica"
Cohesion: 0.53
Nodes (6): Fase 7 - Funções e integração algébrica, Funções algébricas do 1.º e do 2.º graus, Funções polinomiais, Funções racionais, Funções exponenciais e logarítmicas, Relações no ciclo trigonométrico e funções trigonométricas

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fase 2 - Proporção, variação e contagem` connect `Fase 2 - Proporção, variação e contagem` to `Community None`, `Fase 1 - Base numérica`, `Fase 3 - Dados e probabilidade`, `Fase 4 - Geometria plana e medidas`, `Fase 6 - Álgebra e plano cartesiano`?**
  _High betweenness centrality (0.285) - this node is a cross-community bridge._
- **Why does `Trilha sugerida de estudo` connect `unknown` to `Fase 1 - Base numérica`, `Fase 2 - Proporção, variação e contagem`, `Fase 3 - Dados e probabilidade`, `Fase 4 - Geometria plana e medidas`, `Fase 5 - Triângulos, círculos e trigonometria`, `Fase 6 - Álgebra e plano cartesiano`, `Fase 7 - Funções e integração algébrica`?**
  _High betweenness centrality (0.259) - this node is a cross-community bridge._
- **Why does `Fase 4 - Geometria plana e medidas` connect `Fase 4 - Geometria plana e medidas` to `Community None`, `Fase 2 - Proporção, variação e contagem`, `Fase 5 - Triângulos, círculos e trigonometria`?**
  _High betweenness centrality (0.254) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `Fase 2 - Proporção, variação e contagem` (e.g. with `Trilha sugerida de estudo` and `Razões e proporções`) actually correct?**
  _`Fase 2 - Proporção, variação e contagem` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `Fase 6 - Álgebra e plano cartesiano` (e.g. with `Trilha sugerida de estudo` and `Plano cartesiano`) actually correct?**
  _`Fase 6 - Álgebra e plano cartesiano` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Fase 4 - Geometria plana e medidas` (e.g. with `Trilha sugerida de estudo` and `Características das figuras geométricas planas e espaciais`) actually correct?**
  _`Fase 4 - Geometria plana e medidas` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `Fase 5 - Triângulos, círculos e trigonometria` (e.g. with `Trilha sugerida de estudo` and `Teorema de Tales`) actually correct?**
  _`Fase 5 - Triângulos, círculos e trigonometria` has 8 INFERRED edges - model-reasoned connections that need verification._