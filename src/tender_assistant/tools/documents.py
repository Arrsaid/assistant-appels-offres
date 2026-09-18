import os
from pathlib import Path

from langchain.tools import tool


def lire_document(chemin: Path) -> str:
    return chemin.read_text(encoding="utf-8")


@tool
def consulter_document_pme(nom_document: str) -> str:
    """Lit un document Markdown de l'entreprise sélectionnée.

    Utiliser un chemin relatif obtenu avec lister_documents.
    """
    dossier = obtenir_dossier_entreprise()
    chemin_relatif = Path(nom_document)

    if chemin_relatif.is_absolute() or chemin_relatif.drive:
        return "Utilisez un chemin relatif obtenu avec lister_documents."

    chemin = (dossier / chemin_relatif).resolve()

    if not chemin.is_relative_to(dossier):
        return "Accès refusé : le document est hors du dossier sélectionné."

    if chemin.suffix.lower() != ".md":
        return "Format non pris en charge : seuls les fichiers Markdown sont acceptés."

    if not chemin.is_file():
        return "Document introuvable. Utilisez lister_documents pour vérifier son nom."

    contenu = lire_document(chemin)
    return f"Source : {nom_document}\n\n{contenu}"


def obtenir_dossier_entreprise() -> Path:
    valeur = os.getenv("DOSSIER_ENTREPRISE")

    if not valeur:
        raise ValueError("La variable DOSSIER_ENTREPRISE est absente.")

    dossier = Path(valeur)

    if not dossier.is_absolute():
        racine_projet = Path(__file__).resolve().parents[3]
        dossier = racine_projet / dossier

    dossier = dossier.resolve()

    if not dossier.is_dir():
        raise ValueError(f"Dossier d'entreprise introuvable : {dossier}")

    return dossier


@tool
def lister_documents() -> str:
    """Liste les documents Markdown disponibles pour l'entreprise sélectionnée.

    Renvoie leurs chemins relatifs, utilisables pour demander leur lecture.
    """
    dossier = obtenir_dossier_entreprise()

    documents = sorted(
        fichier.relative_to(dossier).as_posix()
        for fichier in dossier.rglob("*")
        if fichier.is_file()
        and fichier.suffix.lower() == ".md"
        and fichier.resolve().is_relative_to(dossier)
    )

    if not documents:
        return "Aucun document Markdown disponible."

    return "\n".join(documents)
