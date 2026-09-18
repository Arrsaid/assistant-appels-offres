from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI


def creer_agent(instructions: str, nom_modele: str):
    modele = ChatOpenAI(model=nom_modele)

    agent = create_deep_agent(
        model=modele,
        system_prompt=instructions,
        tools=[],
        memory=["/AGENTS.md"],
        skills=["/skills/"],
        name="assistant-appels-offres",
    )

    return agent
