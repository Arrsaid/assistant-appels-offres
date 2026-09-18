from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI

from tender_assistant.tools.documents import (
    consulter_document_pme,
    lister_documents,
)


def creer_agent(instructions: str, nom_modele: str):
    modele = ChatOpenAI(model=nom_modele)

    agent = create_deep_agent(
        model=modele,
        system_prompt=instructions,
        tools=[lister_documents, consulter_document_pme],
        memory=["/AGENTS.md"],
        name="assistant-appels-offres",
    )

    return agent
