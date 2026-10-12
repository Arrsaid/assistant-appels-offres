from pathlib import Path

import pymupdf


def lire_pdf(chemin: Path) -> str:
    pages = []

    with pymupdf.open(chemin) as document:
        for numero_page, page in enumerate(document, start=1):
            texte = page.get_text("text", sort=True).strip()
            pages.append(f"--- Page {numero_page} ---\n\n{texte}")

    return "\n\n".join(pages)


def lire_document(chemin: Path) -> str:
    if chemin.suffix.lower() == ".pdf":
        return lire_pdf(chemin)

    return chemin.read_text(encoding="utf-8")


def preparer_document_agent(
    chemin: Path,
    chemin_source: str,
) -> tuple[str, str]:
    contenu = lire_document(chemin)

    if chemin.suffix.lower() == ".pdf":
        contenu = (
            f"Source originale : `{chemin_source}`\n\n"
            "Texte extrait du PDF. Les marqueurs indiquent "
            "les numéros de page du document original.\n\n"
            f"{contenu}"
        )
        return f"{chemin_source}.md", contenu

    return chemin_source, contenu
