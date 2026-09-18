import os
from pathlib import Path

from deepagents.backends.utils import create_file_data
from dotenv import load_dotenv

from tender_assistant.agent import creer_agent
from tender_assistant.tools.documents import lire_document


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

    resultat = agent.invoke(
        {
            "files": {
                "/AGENTS.md": create_file_data(manuel),
            },
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Produis une synthèse sourcée de l'entreprise sélectionnée. "
                        "Découvre les documents disponibles, puis consulte ceux "
                        "nécessaires pour compléter les rubriques demandées."
                    ),
                }
            ],
        }
    )

    resume = resultat["messages"][-1].content

    print("\nRésumé de la PME :")
    print(resume)

    # enregistrement du résumé dans un fichier de sortie
    dossier_sortie = racine_projet / "outputs"
    dossier_sortie.mkdir(exist_ok=True)

    fichier_resume = dossier_sortie / "resume_pme_a.md"
    fichier_resume.write_text(resume, encoding="utf-8")

    print(f"\nRésumé enregistré dans : {fichier_resume}")
