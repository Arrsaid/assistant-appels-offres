from pathlib import Path


def lire_document(chemin: Path) -> str:
    return chemin.read_text(encoding="utf-8")
