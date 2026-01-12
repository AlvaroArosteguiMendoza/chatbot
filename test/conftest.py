import sys
from pathlib import Path

# Añade la raíz del proyecto al PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))
