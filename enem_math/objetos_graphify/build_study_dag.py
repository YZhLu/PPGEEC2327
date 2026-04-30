#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import score_all
from graphify.export import to_html, to_json
from graphify.report import generate

from build_objetos_graphify import PDF_PATH, ROOT_LABEL, TAXONOMY

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "graphify-out"
SCRIPT_NAME = Path(__file__).name

STUDY_ROOT = "Trilha sugerida de estudo"

PHASES = [
    (
        "Fase 1 - Base numérica",
        [
            "Operações em conjuntos numéricos",
            "Divisibilidade",
            "Fatoração",
            "Desigualdades",
        ],
    ),
    (
        "Fase 2 - Proporção, variação e contagem",
        [
            "Razões e proporções",
            "Porcentagem e juros",
            "Relações de dependência entre grandezas",
            "Sequências e progressões",
            "Princípios de contagem",
        ],
    ),
    (
        "Fase 3 - Dados e probabilidade",
        [
            "Representação e análise de dados",
            "Medidas de tendência central",
            "Desvios e variância",
            "Noções de probabilidade",
        ],
    ),
    (
        "Fase 4 - Geometria plana e medidas",
        [
            "Características das figuras geométricas planas e espaciais",
            "Grandezas, unidades de medida e escalas",
            "Comprimentos, áreas e volumes",
            "Ângulos",
            "Posições de retas",
            "Simetrias de figuras planas ou espaciais",
        ],
    ),
    (
        "Fase 5 - Triângulos, círculos e trigonometria",
        [
            "Teorema de Tales",
            "Congruência e semelhança de triângulos",
            "Relações métricas nos triângulos",
            "Circunferências",
            "Trigonometria do ângulo agudo",
        ],
    ),
    (
        "Fase 6 - Álgebra e plano cartesiano",
        [
            "Plano cartesiano",
            "Retas",
            "Paralelismo e perpendicularidade",
            "Gráficos e funções",
            "Equações e inequações",
            "Sistemas de equações",
        ],
    ),
    (
        "Fase 7 - Funções e integração algébrica",
        [
            "Funções algébricas do 1.º e do 2.º graus",
            "Funções polinomiais",
            "Funções racionais",
            "Funções exponenciais e logarítmicas",
            "Relações no ciclo trigonométrico e funções trigonométricas",
        ],
    ),
]

PHASE_REASONS = [
    (
        "Fase 1 - Base numérica",
        "Fase 2 - Proporção, variação e contagem",
        "Proporção e contagem dependem de conforto com operações, comparação e decomposição numérica.",
    ),
    (
        "Fase 2 - Proporção, variação e contagem",
        "Fase 3 - Dados e probabilidade",
        "Probabilidade e leitura quantitativa de dados usam razão, porcentagem e princípios de contagem.",
    ),
    (
        "Fase 2 - Proporção, variação e contagem",
        "Fase 4 - Geometria plana e medidas",
        "Escalas, medidas e semelhança geométrica exigem raciocínio proporcional.",
    ),
    (
        "Fase 4 - Geometria plana e medidas",
        "Fase 5 - Triângulos, círculos e trigonometria",
        "Trigonometria e relações métricas surgem depois de ângulos, retas e figuras básicas.",
    ),
    (
        "Fase 1 - Base numérica",
        "Fase 6 - Álgebra e plano cartesiano",
        "Álgebra escolar exige domínio de operações, desigualdades e manipulação simbólica básica.",
    ),
    (
        "Fase 2 - Proporção, variação e contagem",
        "Fase 6 - Álgebra e plano cartesiano",
        "Funções e gráficos modelam dependência entre grandezas já introduzida na fase 2.",
    ),
    (
        "Fase 6 - Álgebra e plano cartesiano",
        "Fase 7 - Funções e integração algébrica",
        "As famílias de funções vêm depois de equações, gráficos e leitura no plano cartesiano.",
    ),
    (
        "Fase 5 - Triângulos, círculos e trigonometria",
        "Fase 7 - Funções e integração algébrica",
        "O ciclo trigonométrico integra trigonometria, circunferência e representação algébrica.",
    ),
]

OBJECT_REASONS = [
    (
        "Operações em conjuntos numéricos",
        "Divisibilidade",
        "Divisibilidade nasce da manipulação de inteiros e decomposição de operações.",
    ),
    (
        "Divisibilidade",
        "Fatoração",
        "Fatoração usa critérios de divisibilidade e decomposição em fatores.",
    ),
    (
        "Operações em conjuntos numéricos",
        "Desigualdades",
        "Comparar números e interpretar intervalos depende de domínio dos conjuntos numéricos.",
    ),
    (
        "Operações em conjuntos numéricos",
        "Razões e proporções",
        "Razões exigem cálculo com frações, múltiplos e equivalências numéricas.",
    ),
    (
        "Razões e proporções",
        "Porcentagem e juros",
        "Porcentagem é uma razão especial e juros usa variação percentual.",
    ),
    (
        "Razões e proporções",
        "Relações de dependência entre grandezas",
        "Dependência entre grandezas normalmente é apresentada com proporcionalidade direta ou inversa.",
    ),
    (
        "Operações em conjuntos numéricos",
        "Sequências e progressões",
        "Sequências usam padrões numéricos e recorrência sobre operações básicas.",
    ),
    (
        "Princípios de contagem",
        "Noções de probabilidade",
        "Probabilidade elementar costuma começar pela contagem de casos possíveis e favoráveis.",
    ),
    (
        "Representação e análise de dados",
        "Medidas de tendência central",
        "Ler e organizar dados vem antes de resumir a distribuição por média, moda ou mediana.",
    ),
    (
        "Medidas de tendência central",
        "Desvios e variância",
        "Variância e desvio são medidas de dispersão calculadas a partir do centro da distribuição.",
    ),
    (
        "Grandezas, unidades de medida e escalas",
        "Comprimentos, áreas e volumes",
        "Antes de calcular medidas geométricas, o aluno precisa dominar unidades e escalas.",
    ),
    (
        "Características das figuras geométricas planas e espaciais",
        "Simetrias de figuras planas ou espaciais",
        "Reconhecer formas e propriedades vem antes de analisar simetrias.",
    ),
    (
        "Ângulos",
        "Posições de retas",
        "Retas paralelas, concorrentes e perpendiculares são estudadas com base nas relações angulares.",
    ),
    (
        "Razões e proporções",
        "Teorema de Tales",
        "Tales depende de proporcionalidade entre segmentos.",
    ),
    (
        "Posições de retas",
        "Teorema de Tales",
        "O teorema é usualmente apresentado em feixes de retas paralelas cortadas por transversais.",
    ),
    (
        "Teorema de Tales",
        "Congruência e semelhança de triângulos",
        "Tales ajuda a motivar e operacionalizar semelhança em triângulos.",
    ),
    (
        "Congruência e semelhança de triângulos",
        "Relações métricas nos triângulos",
        "Relações métricas ficam mais naturais depois de semelhança e propriedades de triângulos.",
    ),
    (
        "Relações métricas nos triângulos",
        "Trigonometria do ângulo agudo",
        "Seno, cosseno e tangente no triângulo retângulo dependem de relações métricas.",
    ),
    (
        "Ângulos",
        "Circunferências",
        "Arcos, setores e ângulos centrais pedem um repertório angular já consolidado.",
    ),
    (
        "Plano cartesiano",
        "Retas",
        "O estudo analítico da reta usa coordenadas e leitura no plano cartesiano.",
    ),
    (
        "Retas",
        "Paralelismo e perpendicularidade",
        "Paralelismo e perpendicularidade analíticos são estudados a partir de retas e inclinação.",
    ),
    (
        "Relações de dependência entre grandezas",
        "Gráficos e funções",
        "Função costuma aparecer como formalização da dependência entre variáveis.",
    ),
    (
        "Plano cartesiano",
        "Gráficos e funções",
        "Gráficos dependem da leitura de pares ordenados no plano cartesiano.",
    ),
    (
        "Desigualdades",
        "Equações e inequações",
        "Inequações formalizam comparações algébricas já iniciadas nas desigualdades.",
    ),
    (
        "Equações e inequações",
        "Sistemas de equações",
        "Sistemas prolongam a resolução de equações para mais de uma incógnita.",
    ),
    (
        "Gráficos e funções",
        "Funções algébricas do 1.º e do 2.º graus",
        "Funções afim e quadrática são o primeiro aprofundamento natural do estudo de funções.",
    ),
    (
        "Equações e inequações",
        "Funções algébricas do 1.º e do 2.º graus",
        "Resolver raízes, sinais e problemas exige equações associadas às funções básicas.",
    ),
    (
        "Funções algébricas do 1.º e do 2.º graus",
        "Funções polinomiais",
        "Polinomiais ampliam o repertório das funções algébricas básicas.",
    ),
    (
        "Funções algébricas do 1.º e do 2.º graus",
        "Funções racionais",
        "Funções racionais ficam mais fáceis depois que o aluno domina zeros, gráficos e taxas de variação simples.",
    ),
    (
        "Funções algébricas do 1.º e do 2.º graus",
        "Funções exponenciais e logarítmicas",
        "Exponenciais e logaritmos entram melhor quando o aluno já entende famílias de funções e seus gráficos.",
    ),
    (
        "Circunferências",
        "Relações no ciclo trigonométrico e funções trigonométricas",
        "O ciclo trigonométrico usa a circunferência como suporte geométrico.",
    ),
    (
        "Trigonometria do ângulo agudo",
        "Relações no ciclo trigonométrico e funções trigonométricas",
        "As funções trigonométricas generalizam o que foi estudado no triângulo retângulo.",
    ),
]


def node_id(prefix: str, label: str) -> str:
    slug = (
        label.lower()
        .replace("º", "o")
        .replace("ª", "a")
        .replace("/", "_")
        .replace(".", "")
    )
    chars = []
    for ch in slug:
        if ch.isalnum():
            chars.append(ch)
        else:
            chars.append("_")
    while "__" in "".join(chars):
        chars = list("".join(chars).replace("__", "_"))
    return f"{prefix}_{''.join(chars).strip('_')}"


def phase_membership() -> dict[str, str]:
    result = {}
    for phase, objects in PHASES:
        for obj in objects:
            result[obj] = phase
    return result


def all_objects() -> list[str]:
    seen = []
    for objs in TAXONOMY.values():
        for obj in objs:
            if obj not in seen:
                seen.append(obj)
    return seen


def build_study_extraction() -> tuple[dict, dict[str, str]]:
    membership = phase_membership()
    objects = all_objects()
    extraction = {"nodes": [], "edges": [], "hyperedges": [], "input_tokens": 0, "output_tokens": 0}

    extraction["nodes"].append(
        {
            "id": "study_root",
            "label": STUDY_ROOT,
            "file_type": "document",
            "source_file": SCRIPT_NAME,
            "source_location": "pedagogical ordering",
            "source_url": None,
            "captured_at": None,
            "author": None,
            "contributor": None,
        }
    )

    phase_ids: dict[str, str] = {}
    for phase, phase_objects in PHASES:
        pid = node_id("phase", phase)
        phase_ids[phase] = pid
        extraction["nodes"].append(
            {
                "id": pid,
                "label": phase,
                "file_type": "document",
                "source_file": SCRIPT_NAME,
                "source_location": "pedagogical ordering",
                "source_url": None,
                "captured_at": None,
                "author": None,
                "contributor": None,
            }
        )
        extraction["edges"].append(
            {
                "source": "study_root",
                "target": pid,
                "relation": "recommended_before",
                "confidence": "INFERRED",
                "confidence_score": 0.9,
                "source_file": SCRIPT_NAME,
                "source_location": "phase scaffold",
                "weight": 1.0,
            }
        )
        for obj in phase_objects:
            extraction["nodes"].append(
                {
                    "id": node_id("obj", obj),
                    "label": obj,
                    "file_type": "paper",
                    "source_file": PDF_PATH.name,
                    "source_location": "page 1",
                    "source_url": None,
                    "captured_at": None,
                    "author": None,
                    "contributor": None,
                }
            )
            extraction["edges"].append(
                {
                    "source": pid,
                    "target": node_id("obj", obj),
                    "relation": "study_block_contains",
                    "confidence": "INFERRED",
                    "confidence_score": 0.85,
                    "source_file": SCRIPT_NAME,
                    "source_location": phase,
                    "weight": 1.0,
                }
            )

    for source, target, reason in PHASE_REASONS:
        extraction["edges"].append(
            {
                "source": phase_ids[source],
                "target": phase_ids[target],
                "relation": "recommended_before",
                "confidence": "INFERRED",
                "confidence_score": 0.85,
                "source_file": SCRIPT_NAME,
                "source_location": reason,
                "weight": 1.0,
            }
        )

    object_lookup = {obj: node_id("obj", obj) for obj in objects}
    for source, target, reason in OBJECT_REASONS:
        extraction["edges"].append(
            {
                "source": object_lookup[source],
                "target": object_lookup[target],
                "relation": "prerequisite_for",
                "confidence": "INFERRED",
                "confidence_score": 0.8,
                "source_file": SCRIPT_NAME,
                "source_location": reason,
                "weight": 1.0,
            }
        )

    return extraction, membership


def communities_for_phases(extraction: dict, membership: dict[str, str]) -> tuple[dict[int, list[str]], dict[int, str]]:
    phase_index = {phase: idx for idx, (phase, _) in enumerate(PHASES)}
    communities = {idx: [] for idx in range(len(PHASES))}
    labels = {}

    for idx, (phase, _) in enumerate(PHASES):
        labels[idx] = phase

    for node in extraction["nodes"]:
        label = node["label"]
        if label in membership:
            communities[phase_index[membership[label]]].append(node["id"])
        elif label in phase_index:
            communities[phase_index[label]].append(node["id"])

    return communities, labels


def write_study_outputs(extraction: dict, communities: dict[int, list[str]], labels: dict[int, str]) -> None:
    G = build_from_json(extraction)
    cohesion = score_all(G, communities)
    gods = god_nodes(G)
    surprises = surprising_connections(G, communities)
    questions = suggest_questions(G, communities, labels)

    detection = {
        "files": {
            "code": [],
            "document": [SCRIPT_NAME],
            "paper": [PDF_PATH.name],
            "image": [],
            "video": [],
        },
        "total_files": 1,
        "total_words": 151,
        "needs_graph": False,
        "warning": "Study DAG is pedagogical inference built on top of the extracted taxonomy.",
        "skipped_sensitive": [],
        "graphifyignore_patterns": 0,
    }

    report = generate(
        G,
        communities,
        cohesion,
        labels,
        gods,
        surprises,
        detection,
        {"input": 0, "output": 0},
        str(ROOT),
        suggested_questions=questions,
    )
    (OUT_DIR / "STUDY_GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_json(G, communities, str(OUT_DIR / "study_graph.json"))
    to_html(G, communities, str(OUT_DIR / "study_graph.html"), community_labels=labels)

    (OUT_DIR / "study_analysis.json").write_text(
        json.dumps(
            {
                "communities": {str(k): v for k, v in communities.items()},
                "labels": {str(k): v for k, v in labels.items()},
                "cohesion": {str(k): v for k, v in cohesion.items()},
                "gods": gods,
                "surprises": surprises,
                "questions": questions,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def write_mermaid_and_plan(membership: dict[str, str]) -> None:
    graph = nx.DiGraph()
    graph.add_node("study_root", label=STUDY_ROOT)

    phase_ids = {phase: node_id("phase", phase) for phase, _ in PHASES}
    object_ids = {obj: node_id("obj", obj) for obj in membership}

    for phase, objects in PHASES:
        graph.add_node(phase_ids[phase], label=phase)
        graph.add_edge("study_root", phase_ids[phase])
        for obj in objects:
            graph.add_node(object_ids[obj], label=obj)
            graph.add_edge(phase_ids[phase], object_ids[obj])

    for source, target, _ in PHASE_REASONS:
        graph.add_edge(phase_ids[source], phase_ids[target])
    for source, target, _ in OBJECT_REASONS:
        graph.add_edge(object_ids[source], object_ids[target])

    mermaid = ["flowchart TD", '  study_root["Trilha sugerida de estudo"]']
    for phase, objects in PHASES:
        pid = phase_ids[phase]
        mermaid.append(f'  {pid}["{phase}"]')
        mermaid.append(f"  study_root --> {pid}")
        for obj in objects:
            oid = object_ids[obj]
            mermaid.append(f'  {oid}["{obj}"]')
            mermaid.append(f"  {pid} --> {oid}")
    for source, target, _ in PHASE_REASONS:
        mermaid.append(f"  {phase_ids[source]} -.-> {phase_ids[target]}")
    for source, target, _ in OBJECT_REASONS:
        mermaid.append(f"  {object_ids[source]} --> {object_ids[target]}")

    (OUT_DIR / "study_dag.mmd").write_text("\n".join(mermaid) + "\n", encoding="utf-8")

    topo = list(nx.topological_sort(graph))
    reverse_lookup = {v: k for k, v in phase_ids.items()} | {v: k for k, v in object_ids.items()}
    topo_labels = [STUDY_ROOT if node == "study_root" else reverse_lookup[node] for node in topo]
    recommended_order = []
    for phase, objects in PHASES:
        recommended_order.append({"phase": phase, "objects": list(objects)})

    audit = {
        "assumption": "Sequência pedagógica inferida; não é uma ordem oficial do INEP.",
        "phase_count": len(PHASES),
        "object_count": len(object_ids),
        "phase_edges": [{"source": s, "target": t, "reason": r} for s, t, r in PHASE_REASONS],
        "prerequisite_edges": [{"source": s, "target": t, "reason": r} for s, t, r in OBJECT_REASONS],
        "topological_order": topo_labels,
        "recommended_order": recommended_order,
        "source_pdf": str(PDF_PATH),
    }
    (OUT_DIR / "study_dag_audit.json").write_text(
        json.dumps(audit, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    lines = [
        "# DAG de estudo sugerido",
        "",
        f"- Fonte conceitual: [{PDF_PATH.name}]({PDF_PATH})",
        "- Tipo de aresta: `recommended_before` e `prerequisite_for`",
        "- Regra de honestidade: esta ordem é uma inferência pedagógica, não uma sequência oficial do ENEM/INEP.",
        "",
        "## Fases sugeridas",
        "",
    ]
    for phase, objects in PHASES:
        lines.append(f"### {phase}")
        for obj in objects:
            lines.append(f"- {obj}")
        lines.append("")

    lines.extend(
        [
            "## Mermaid",
            "",
            "```mermaid",
            *mermaid,
            "```",
            "",
            "## Sequência recomendada",
            "",
        ]
    )
    counter = 1
    for phase, objects in PHASES:
        lines.append(f"### {phase}")
        for obj in objects:
            lines.append(f"{counter}. {obj}")
            counter += 1
        lines.append("")

    lines.extend(
        [
            "## Ordem topológica mínima",
            "",
            "Esta lista é a ordem técnica compatível com todas as dependências do DAG. Para estudar, prefira a sequência recomendada acima.",
            "",
        ]
    )
    for idx, label in enumerate(topo_labels[1:], start=1):
        lines.append(f"{idx}. {label}")

    lines.extend(
        [
            "",
            "## Pontes importantes",
            "",
            "- `Razões e proporções` abre tanto geometria de medidas quanto porcentagem e dependência entre grandezas.",
            "- `Princípios de contagem` é a ponte curta para `Noções de probabilidade`.",
            "- `Plano cartesiano` e `Relações de dependência entre grandezas` convergem em `Gráficos e funções`.",
            "- `Circunferências` e `Trigonometria do ângulo agudo` convergem em `Relações no ciclo trigonométrico e funções trigonométricas`.",
        ]
    )
    (OUT_DIR / "STUDY_DAG.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    extraction, membership = build_study_extraction()
    communities, labels = communities_for_phases(extraction, membership)

    (OUT_DIR / "study_extract.json").write_text(
        json.dumps(extraction, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    write_study_outputs(extraction, communities, labels)
    write_mermaid_and_plan(membership)

    print(
        json.dumps(
            {
                "study_nodes": len(extraction["nodes"]),
                "study_edges": len(extraction["edges"]),
                "study_phases": len(PHASES),
                "html": str(OUT_DIR / "study_graph.html"),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
