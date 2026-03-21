from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

project = "dummy-gp"
author = "Sandbox"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]
autosummary_generate = True
autodoc_member_order = "bysource"
templates_path = ["_templates"]
exclude_patterns = ["_build"]
