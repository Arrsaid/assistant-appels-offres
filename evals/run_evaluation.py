import json
from pathlib import Path

RACINE_PROJET = Path(__file__).resolve().parents[1]

RAPPORTS_PAR_MODE = {
    "consultation": "analyse_consultation.md",
    "entreprise": "resume_entreprise.md",
    "comparaison": "comparaison_entreprise_consultation.md",
}


def charger_jsonl(chemin: Path) -> list[dict]:
    return [
        json.loads(ligne)
        for ligne in chemin.read_text(encoding="utf-8").splitlines()
        if ligne.strip()
    ]


def normaliser(texte: str) -> str:
    texte = texte.casefold()
    texte = texte.replace("\u202f", " ").replace("\xa0", " ")
    return " ".join(texte.split())


def main() -> None:
    cas = charger_jsonl(RACINE_PROJET / "evals" / "datasets" / "cases.jsonl")
    attendus = charger_jsonl(
        RACINE_PROJET / "evals" / "datasets" / "expected_results.jsonl"
    )
    attendus_par_id = {resultat["case_id"]: resultat for resultat in attendus}

    nombre_echecs = 0

    for scenario in cas:
        attendu = attendus_par_id[scenario["id"]]
        nom_rapport = RAPPORTS_PAR_MODE[scenario["mode"]]
        chemin_rapport = RACINE_PROJET / "outputs" / nom_rapport
        rapport = normaliser(chemin_rapport.read_text(encoding="utf-8"))

        faits_manquants = [
            fait
            for fait in attendu["required_facts"]
            if normaliser(fait) not in rapport
        ]
        sources_manquantes = [
            source
            for source in attendu["required_sources"]
            if normaliser(source) not in rapport
        ]
        termes_interdits = [
            terme
            for terme in attendu["forbidden_terms"]
            if normaliser(terme) in rapport
        ]

        reussi = not faits_manquants and not sources_manquantes and not termes_interdits

        print(f"\nCas : {scenario['id']}")
        print(f"Résultat : {'RÉUSSI' if reussi else 'ÉCHEC'}")
        print(f"Faits manquants : {faits_manquants}")
        print(f"Sources manquantes : {sources_manquantes}")
        print(f"Termes interdits trouvés : {termes_interdits}")

        if not reussi:
            nombre_echecs += 1

    raise SystemExit(1 if nombre_echecs else 0)


if __name__ == "__main__":
    main()
