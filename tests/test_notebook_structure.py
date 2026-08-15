import json
from pathlib import Path


def test_repository_contains_valid_notebook():
    notebooks = sorted(Path(__file__).resolve().parents[1].glob("*.ipynb"))
    assert notebooks, "Expected at least one notebook in the repository root."
    notebook = json.loads(notebooks[0].read_text(encoding="utf-8"))
    assert isinstance(notebook.get("cells"), list)
    assert notebook["cells"], "Notebook must contain at least one cell."
    assert all(isinstance(cell.get("source", []), list) for cell in notebook["cells"])
