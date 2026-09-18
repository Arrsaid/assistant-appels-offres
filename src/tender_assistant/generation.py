from langchain_openai import ChatOpenAI


def generer_resume(
    texte: str,
    instructions: str,
    nom_modele: str,
) -> str:
    modele = ChatOpenAI(model=nom_modele)

    reponse = modele.invoke(
        [
            ("system", instructions),
            ("human", texte),
        ]
    )

    if not isinstance(reponse.content, str):
        raise TypeError("Le modèle n'a pas renvoyé un contenu textuel simple.")

    return reponse.content
