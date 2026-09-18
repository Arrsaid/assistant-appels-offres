import os
from pathlib import Path

from deepagents.backends.utils import create_file_data
from dotenv import load_dotenv

from tender_assistant.agent import creer_agent
from tender_assistant.tools.documents import lire_document, obtenir_dossier_entreprise


def main() -> None:

    racine_projet = Path(__file__).resolve().parents[2]
    load_dotenv(racine_projet / ".env")

    if not os.getenv("OPENAI_API_KEY"):
        print("Clé OpenAI absente : vérifiez votre fichier .env.")
        return

    print("Clé OpenAI chargée.")

    dossier = racine_projet / "data" / "synthetic" / "companies" / "pme_a" / "documents"

    if not dossier.is_dir():
        print(f"Dossier introuvable : {dossier}")
        return

    chemin_prompt = Path(__file__).resolve().parent / "prompts" / "resume_entreprise.md"
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

    dossier_entreprise = obtenir_dossier_entreprise()

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

    valeur = os.getenv("DOSSIER_CONSULTATION")

    if not valeur:
        print("La variable DOSSIER_CONSULTATION est absente.")
        return

    dossier_consultation = Path(valeur)

    if not dossier_consultation.is_absolute():
        dossier_consultation = racine_projet / dossier_consultation

    dossier_consultation = dossier_consultation.resolve()

    if not dossier_consultation.is_dir():
        print(f"Dossier introuvable : {dossier_consultation}")
        return

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
                    "content": (
                        "Analyse la consultation sélectionnée : présente le besoin, "
                        "les exigences, le budget, le calendrier et les points "
                        "à clarifier, avec leurs sources. "
                        "Ne compare pas encore avec l'entreprise."
                    ),
                }
            ],
        }
    )

    # print("\nAppels d’outils effectués :")

    # for message in resultat["messages"]:
    #     for appel in getattr(message, "tool_calls", []):
    #         print(appel["name"], appel["args"])

    resume = resultat["messages"][-1].content

    # print("\nRésumé de la PME :")
    # print(resume)

    # enregistrement du résumé dans un fichier de sortie
    dossier_sortie = racine_projet / "outputs"
    dossier_sortie.mkdir(exist_ok=True)

    fichier_resume = dossier_sortie / "resume_pme_a.md"
    fichier_resume.write_text(resume, encoding="utf-8")

    print(f"\nRésumé enregistré dans : {fichier_resume}")
