import subprocess
import sys
from pathlib import Path

RACINE_PROJET = Path(__file__).resolve().parents[2]


def test_les_rapports_respectent_les_attendus():
    resultat = subprocess.run(
        [sys.executable, "evals/run_evaluation.py"],
        cwd=RACINE_PROJET,
        capture_output=True,
        text=True,
        check=False,
    )

    assert resultat.returncode == 0, resultat.stdout + resultat.stderr
