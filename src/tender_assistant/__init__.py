import os
from pathlib import Path

from deepagents.backends.utils import create_file_data
from dotenv import load_dotenv

from tender_assistant.agent import creer_agent
from tender_assistant.tools.documents import lire_document


def obtenir_tache(mode: str) -> tuple[str, str] | None:
    taches = {
        "consultation": (
            (
                "Analyse la consultation sélectionnée. "
                "Commence par lire intégralement le skill "
                "/skills/analyse-consultation/SKILL.md avec read_file, "
                "puis applique sa méthode. "
                "Pour cette tâche, consulte uniquement les documents "
                "sous /consultation/, sans lire ceux de /entreprise/. "
                "Si le skill est inaccessible, signale le problème "
                "au lieu de produire l'analyse."
            ),
            "analyse_consultation.md",
        ),
        "entreprise": (
            (
                "Réalise une synthèse de l’entreprise sélectionnée. "
                "Commence par lire intégralement le skill "
                "/skills/resume-entreprise/SKILL.md avec read_file, "
                "puis applique sa méthode. "
                "Pour cette tâche, consulte uniquement les documents "
                "sous /entreprise/, sans lire ceux de /consultation/. "
                "Si le skill est inaccessible, signale le problème "
                "au lieu de produire la synthèse."
            ),
            "resume_entreprise.md",
        ),
        "comparaison": (
            (
                "Compare l’entreprise sélectionnée à la consultation sélectionnée. "
                "Commence par lire intégralement le skill "
                "/skills/comparaison-entreprise-consultation/SKILL.md "
                "avec read_file, puis applique sa méthode. "
                "Consulte les documents sous /consultation/ et sous /entreprise/. "
                "Ne prends pas la décision de répondre à la consultation. "
                "Si le skill est inaccessible, signale le problème "
                "au lieu de produire la comparaison."
            ),
            "comparaison_entreprise_consultation.md",
        ),
    }

    return taches.get(mode)


def demander_mode() -> str:
    choix_vers_mode = {
        "1": "consultation",
        "2": "entreprise",
        "3": "comparaison",
    }

    print("\nQue souhaitez-vous faire ?")
    print("1. Analyser une consultation")
    print("2. Synthétiser une entreprise")
    print("3. Comparer une entreprise à une consultation")

    while True:
        choix = input("\nVotre choix (1, 2 ou 3) : ").strip()

        mode = choix_vers_mode.get(choix)

        if mode:
            return mode

        print("Choix invalide. Saisissez 1, 2 ou 3.")


def choisir_dossier(racine: Path, titre: str) -> Path | None:
    if not racine.is_dir():
        print(f"Dossier introuvable : {racine}")
        return None

    dossiers = sorted(
        (chemin for chemin in racine.iterdir() if chemin.is_dir()),
        key=lambda chemin: chemin.name.lower(),
    )

    if not dossiers:
        print(f"Aucun dossier disponible dans : {racine}")
        return None

    print(f"\n{titre} disponibles :")

    for numero, dossier in enumerate(dossiers, start=1):
        print(f"{numero}. {dossier.name}")

    while True:
        choix = input(f"\nVotre choix (1 à {len(dossiers)}) : ").strip()

        if choix.isdigit():
            index = int(choix) - 1

            if 0 <= index < len(dossiers):
                return dossiers[index]

        print("Choix invalide. Réessayez.")


def main() -> None:

    racine_projet = Path(__file__).resolve().parents[2]
    load_dotenv(racine_projet / ".env")

    if not os.getenv("OPENAI_API_KEY"):
        print("Clé OpenAI absente : vérifiez votre fichier .env.")
        return

    print("Clé OpenAI chargée.")

    mode = demander_mode()
    tache = obtenir_tache(mode)

    if tache is None:
        print(f"Mode inconnu : {mode}")
        return

    message_utilisateur, nom_fichier_sortie = tache

    dossier_entreprise: Path | None = None

    if mode in {"entreprise", "comparaison"}:
        entreprise = choisir_dossier(
            racine_projet / "data" / "synthetic" / "companies",
            "Entreprises",
        )

        if entreprise is None:
            return

        dossier_entreprise = entreprise / "documents"

        if not dossier_entreprise.is_dir():
            print(f"Dossier de documents introuvable : {dossier_entreprise}")
            return

    dossier_consultation: Path | None = None

    if mode in {"consultation", "comparaison"}:
        consultation = choisir_dossier(
            racine_projet / "data" / "synthetic" / "consultations",
            "Consultations",
        )

        if consultation is None:
            return

        dossier_consultation = consultation

    chemin_prompt = Path(__file__).resolve().parent / "prompts" / "systeme.md"
    instruction_systeme = lire_document(chemin_prompt)

    agent = creer_agent(
        instructions=instruction_systeme,
        nom_modele=os.getenv("OPENAI_MODEL", "gpt-5-nano"),
    )

    chemin_manuel = Path(__file__).resolve().parent / "AGENTS.md"
    manuel = lire_document(chemin_manuel)

    fichiers_agent = {
        "/AGENTS.md": create_file_data(manuel),
    }

    if dossier_entreprise is not None:
        for chemin in sorted(dossier_entreprise.rglob("*")):
            if not chemin.is_file() or chemin.suffix.lower() != ".md":
                continue

            if not chemin.resolve().is_relative_to(dossier_entreprise):
                continue

            chemin_relatif = chemin.relative_to(dossier_entreprise).as_posix()
            chemin_virtuel = f"/entreprise/{chemin_relatif}"

            fichiers_agent[chemin_virtuel] = create_file_data(lire_document(chemin))

    dossier_skills = Path(__file__).resolve().parent / "skills"

    for chemin in sorted(dossier_skills.rglob("*")):
        if chemin.is_file():
            chemin_relatif = chemin.relative_to(dossier_skills).as_posix()

            fichiers_agent[f"/skills/{chemin_relatif}"] = create_file_data(
                lire_document(chemin)
            )

    if dossier_consultation is not None:
        for chemin in sorted(dossier_consultation.rglob("*")):
            if not chemin.is_file() or chemin.suffix.lower() != ".md":
                continue

            if not chemin.resolve().is_relative_to(dossier_consultation):
                continue

            chemin_relatif = chemin.relative_to(dossier_consultation).as_posix()

            fichiers_agent[f"/consultation/{chemin_relatif}"] = create_file_data(
                lire_document(chemin)
            )

    resultat = agent.invoke(
        {
            "files": fichiers_agent,
            "messages": [
                {
                    "role": "user",
                    "content": message_utilisateur,
                }
            ],
        }
    )
    resume = resultat["messages"][-1].content

    print("\nAppels d’outils effectués :")

    for message in resultat["messages"]:
        for appel in getattr(message, "tool_calls", []):
            print(appel["name"], appel["args"])

    # enregistrement du résumé dans un fichier de sortie
    dossier_sortie = racine_projet / "outputs"
    dossier_sortie.mkdir(exist_ok=True)

    fichier_resume = dossier_sortie / nom_fichier_sortie

    fichier_resume.write_text(resume, encoding="utf-8")

    print(f"\nRésumé enregistré dans : {fichier_resume}")
