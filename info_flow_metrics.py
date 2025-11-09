import os
import ast
import json
import networkx as nx

# --- Folders to analyze ---
SRC_DIRS = ["models", "services"]

def get_imports_from_file(filepath):
    """Extract import statements using AST."""
    imports = set()
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=filepath)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)
    except Exception as e:
        print(f"⚠️ Error reading {filepath}: {e}")
    return imports

def build_dependency_graph(src_dirs):
    """Build dependency graph based on imports."""
    G = nx.DiGraph()
    py_files = []

    # Map file modules to actual file paths (e.g., models.vehicle -> models/vehicle.py)
    module_map = {}

    for src in src_dirs:
        for root, _, files in os.walk(src):
            for f in files:
                if f.endswith(".py"):
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, os.getcwd())
                    module_name = rel_path[:-3].replace("/", ".")
                    module_map[module_name] = rel_path
                    py_files.append(rel_path)

    # Add nodes and edges
    for file in py_files:
        file_name = os.path.relpath(file, os.getcwd())
        G.add_node(file_name)
        imports = get_imports_from_file(file)

        for imp in imports:
            for mod_name, target_path in module_map.items():
                # Match both exact and prefix forms (models.vehicle, services.db_service)
                if imp == mod_name or imp.startswith(mod_name + "."):
                    G.add_edge(file_name, target_path)

    return G

def compute_information_metrics(G):
    metrics = []
    for node in G.nodes:
        fan_in = len(list(G.predecessors(node)))
        fan_out = len(list(G.successors(node)))
        info_value = fan_in * (fan_out ** 2)
        metrics.append({
            "file": node,
            "fanIn": fan_in,
            "fanOut": fan_out,
            "informationValue": info_value
        })

    summary = {
        "totalFiles": len(metrics),
        "maxInfo": max((m["informationValue"] for m in metrics), default=0),
        "avgInfo": round(sum(m["informationValue"] for m in metrics) / len(metrics), 2) if metrics else 0
    }
    return {"metrics": metrics, "summary": summary}

if __name__ == "__main__":
    print("🔍 Scanning project for dependencies...")
    G = build_dependency_graph(SRC_DIRS)
    result = compute_information_metrics(G)

    os.makedirs("docs", exist_ok=True)
    output_file = "docs/information-metrics.json"
    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)

    print(f"✅ Information flow metrics saved → {output_file}")