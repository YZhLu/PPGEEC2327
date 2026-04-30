#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.detect import save_manifest
from graphify.export import to_html, to_json
from graphify.report import generate

ROOT = Path(__file__).resolve().parent
PDF_PATH = ROOT / "objetos_de_conhecimento.pdf"
TXT_PATH = ROOT / "graphify_corpus_objetos.txt"
OUT_DIR = ROOT / "graphify-out"
DETECT_PATH = ROOT / ".graphify_detect.json"
EXTRACT_PATH = ROOT / ".graphify_extract.json"
ANALYSIS_PATH = ROOT / ".graphify_analysis.json"
LABELS_PATH = ROOT / ".graphify_labels.json"

ROOT_LABEL = "Matemática e suas Tecnologias"

TAXONOMY = {
    "Conhecimentos numéricos": [
        "Operações em conjuntos numéricos",
        "Desigualdades",
        "Divisibilidade",
        "Fatoração",
        "Razões e proporções",
        "Porcentagem e juros",
        "Relações de dependência entre grandezas",
        "Sequências e progressões",
        "Princípios de contagem",
    ],
    "Conhecimentos geométricos": [
        "Características das figuras geométricas planas e espaciais",
        "Grandezas, unidades de medida e escalas",
        "Comprimentos, áreas e volumes",
        "Ângulos",
        "Posições de retas",
        "Simetrias de figuras planas ou espaciais",
        "Congruência e semelhança de triângulos",
        "Teorema de Tales",
        "Relações métricas nos triângulos",
        "Circunferências",
        "Trigonometria do ângulo agudo",
    ],
    "Conhecimentos de estatística e probabilidade": [
        "Representação e análise de dados",
        "Medidas de tendência central",
        "Desvios e variância",
        "Noções de probabilidade",
    ],
    "Conhecimentos algébricos": [
        "Gráficos e funções",
        "Funções algébricas do 1.º e do 2.º graus",
        "Funções polinomiais",
        "Funções racionais",
        "Funções exponenciais e logarítmicas",
        "Equações e inequações",
        "Relações no ciclo trigonométrico e funções trigonométricas",
    ],
    "Conhecimentos algébricos/geométricos": [
        "Plano cartesiano",
        "Retas",
        "Circunferências",
        "Paralelismo e perpendicularidade",
        "Sistemas de equações",
    ],
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def word_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def build_detection() -> dict:
    detection = {
        "files": {
            "code": [],
            "document": [TXT_PATH.name],
            "paper": [PDF_PATH.name],
            "image": [],
            "video": [],
        },
        "total_files": 1,
        "total_words": word_count(TXT_PATH),
        "needs_graph": False,
        "warning": None,
        "skipped_sensitive": [],
        "graphifyignore_patterns": 0,
    }
    DETECT_PATH.write_text(
        json.dumps(detection, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return detection


def base_node(node_id: str, label: str) -> dict:
    return {
        "id": node_id,
        "label": label,
        "file_type": "paper",
        "source_file": PDF_PATH.name,
        "source_location": "page 1",
        "source_url": None,
        "captured_at": None,
        "author": None,
        "contributor": None,
    }


def build_extraction() -> dict:
    nodes = []
    edges = []

    root_id = "matematica_tecnologias"
    nodes.append(base_node(root_id, ROOT_LABEL))

    object_ids: dict[str, str] = {}
    for category, objects in TAXONOMY.items():
        category_id = f"categoria_{slug(category)}"
        nodes.append(base_node(category_id, category))
        edges.append(
            {
                "source": root_id,
                "target": category_id,
                "relation": "contains",
                "confidence": "EXTRACTED",
                "confidence_score": 1.0,
                "source_file": PDF_PATH.name,
                "source_location": "page 1",
                "weight": 1.0,
            }
        )
        for obj in objects:
            object_id = object_ids.setdefault(obj, f"objeto_{slug(obj)}")
            if not any(n["id"] == object_id for n in nodes):
                nodes.append(base_node(object_id, obj))
            edges.append(
                {
                    "source": category_id,
                    "target": object_id,
                    "relation": "contains",
                    "confidence": "EXTRACTED",
                    "confidence_score": 1.0,
                    "source_file": PDF_PATH.name,
                    "source_location": "page 1",
                    "weight": 1.0,
                }
            )

    extraction = {
        "nodes": nodes,
        "edges": edges,
        "hyperedges": [],
        "input_tokens": 0,
        "output_tokens": 0,
    }
    EXTRACT_PATH.write_text(
        json.dumps(extraction, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (OUT_DIR / "dag_extract.json").write_text(
        json.dumps(extraction, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return extraction


def choose_labels(G, communities: dict[int, list[str]]) -> dict[int, str]:
    by_category = {category: set(objects) for category, objects in TAXONOMY.items()}
    labels: dict[int, str] = {}
    for cid, node_ids in communities.items():
        node_labels = {G.nodes[n].get("label", n) for n in node_ids}
        direct_match = [label for label in node_labels if label in TAXONOMY]
        if ROOT_LABEL in node_labels:
            labels[cid] = ROOT_LABEL
            continue
        if direct_match:
            labels[cid] = sorted(direct_match)[0]
            continue
        scores = {}
        for category, objects in by_category.items():
            scores[category] = len(node_labels.intersection(objects))
        best = max(scores, key=scores.get)
        labels[cid] = best if scores[best] else f"Community {cid}"
    return labels


def write_dag_files() -> None:
    mermaid_lines = ["flowchart TD"]
    root_id = "root"
    mermaid_lines.append(f'  {root_id}["{ROOT_LABEL}"]')

    shared = defaultdict(list)
    for category, objects in TAXONOMY.items():
        category_id = f"cat_{slug(category)}"
        mermaid_lines.append(f'  {category_id}["{category}"]')
        mermaid_lines.append(f"  {root_id} --> {category_id}")
        for obj in objects:
            object_id = f"obj_{slug(obj)}"
            mermaid_lines.append(f'  {object_id}["{obj}"]')
            mermaid_lines.append(f"  {category_id} --> {object_id}")
            shared[obj].append(category)

    dag_path = OUT_DIR / "objetos_dag.mmd"
    dag_path.write_text("\n".join(mermaid_lines) + "\n", encoding="utf-8")

    shared_objects = {
        obj: parents for obj, parents in shared.items() if len(set(parents)) > 1
    }
    audit = {
        "root": ROOT_LABEL,
        "category_count": len(TAXONOMY),
        "unique_object_count": len({obj for objs in TAXONOMY.values() for obj in objs}),
        "edge_count": len(TAXONOMY) + sum(len(objs) for objs in TAXONOMY.values()),
        "shared_objects": shared_objects,
        "source_file": str(PDF_PATH),
    }
    (OUT_DIR / "dag_audit.json").write_text(
        json.dumps(audit, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    lines = [
        "# DAG dos Objetos de Conhecimento",
        "",
        f"- Fonte: [{PDF_PATH.name}]({PDF_PATH})",
        f"- Categorias: {len(TAXONOMY)}",
        f"- Objetos únicos: {audit['unique_object_count']}",
        f"- Arestas do DAG: {audit['edge_count']}",
        "",
        "## Estrutura",
        "",
        "```mermaid",
        *mermaid_lines,
        "```",
        "",
        "## Observações",
        "",
        "- O DAG representa uma hierarquia curricular: área -> categoria -> objeto.",
        "- `Circunferências` aparece em duas categorias, então é um nó compartilhado com dois pais e continua acíclico.",
        "",
        "## Categorias",
        "",
    ]
    for category, objects in TAXONOMY.items():
        lines.append(f"### {category}")
        for obj in objects:
            lines.append(f"- {obj}")
        lines.append("")

    (OUT_DIR / "DAG_SUMMARY.md").write_text(
        "\n".join(lines).strip() + "\n", encoding="utf-8"
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    detection = build_detection()
    extraction = build_extraction()

    G = build_from_json(extraction)
    communities = cluster(G)
    cohesion = score_all(G, communities)
    gods = god_nodes(G)
    surprises = surprising_connections(G, communities)
    labels = choose_labels(G, communities)
    questions = suggest_questions(G, communities, labels)

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
    (OUT_DIR / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_json(G, communities, str(OUT_DIR / "graph.json"))
    to_html(G, communities, str(OUT_DIR / "graph.html"), community_labels=labels)

    analysis = {
        "communities": {str(k): v for k, v in communities.items()},
        "cohesion": {str(k): v for k, v in cohesion.items()},
        "gods": gods,
        "surprises": surprises,
        "questions": questions,
    }
    ANALYSIS_PATH.write_text(
        json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    LABELS_PATH.write_text(
        json.dumps({str(k): v for k, v in labels.items()}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    save_manifest(detection["files"], manifest_path=str(OUT_DIR / "manifest.json"))
    cost = {
        "runs": [
            {
                "date": "manual-graphify-build",
                "input_tokens": 0,
                "output_tokens": 0,
                "files": detection["total_files"],
            }
        ],
        "total_input_tokens": 0,
        "total_output_tokens": 0,
    }
    (OUT_DIR / "cost.json").write_text(
        json.dumps(cost, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    write_dag_files()

    print(
        json.dumps(
            {
                "nodes": G.number_of_nodes(),
                "edges": G.number_of_edges(),
                "communities": len(communities),
                "dag_summary": str(OUT_DIR / "DAG_SUMMARY.md"),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
