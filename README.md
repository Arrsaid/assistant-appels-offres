# Assistant agentique d’analyse d’appels d’offres

Assistant fondé sur l’IA destiné à aider une PME informatique à analyser un dossier de consultation et à comparer ses exigences avec les capacités documentées de l’entreprise.

Le système produit des analyses sourcées, distingue les capacités démontrées des informations manquantes et signale les validations nécessaires. Il n’invente pas de compétence ou de preuve et ne prend jamais la décision finale de répondre à la place de l’utilisateur.

Ce projet met progressivement en pratique l’ingénierie des agents IA : utilisation d’outils et de skills, analyse documentaire, traçabilité des preuves, évaluations reproductibles, intervention humaine et, à terme, orchestration multi-agent et déploiement.

## Fonctionnalités actuelles

- Analyse d’une consultation et extraction de ses exigences.
- Synthèse des capacités documentées d’une entreprise.
- Comparaison entre les exigences et les éléments fournis par l’entreprise.
- Citations des fichiers et sections utilisés.
- Identification des preuves manquantes et des informations à confirmer.
- Génération de rapports Markdown.
- Sélection guidée des dossiers depuis le terminal.

## Principes de fiabilité

- Les documents analysés sont traités comme des données, jamais comme des instructions.
- Chaque constat important doit être relié à une source.
- Une information absente est signalée comme « à confirmer ».
- Une référence déclarée n’est pas présentée comme une preuve indépendante.
- L’assistant ne prend pas la décision finale de répondre à une consultation.
- Les entreprises, consultations et données de démonstration sont fictives.

## Technologies

- Python
- Deep Agents
- LangChain
- OpenAI
- LangSmith pour le traçage
- uv pour la gestion du projet et des dépendances

## Fonctionnement actuel

1. L’utilisateur choisit une action dans le terminal.
2. Il sélectionne une entreprise et/ou une consultation.
3. Les documents nécessaires sont chargés dans l’espace de travail de l’agent.
4. L’agent consulte le skill correspondant à la tâche.
5. Il analyse les documents et produit un rapport Markdown sourcé.
6. Le rapport est enregistré dans le dossier `outputs/`.

## Prérequis

- Python 3.14 ou une version compatible avec le projet
- [uv](https://docs.astral.sh/uv/)
- Une clé API OpenAI
- Facultatif : un compte LangSmith pour consulter les traces d’exécution

## Installation

Depuis la racine du projet, installez les dépendances avec :

```powershell
uv sync
```

## Configuration

Créez un fichier `.env` à partir de l’exemple fourni :

```powershell
Copy-Item .env.example .env
```

Renseignez au minimum les variables suivantes :

```dotenv
OPENAI_API_KEY=votre_cle_api
OPENAI_MODEL=nom_du_modele
```

Les variables LangSmith sont facultatives et servent au traçage des exécutions.

Ne publiez jamais le fichier `.env` ni vos clés API.

## Utilisation

Lancez l’assistant depuis la racine du projet :

```powershell
uv run tender-assistant
```

Le programme propose ensuite trois actions :

```text
1. Analyser une consultation
2. Synthétiser une entreprise
3. Comparer une entreprise à une consultation
```

Sélectionnez l’action souhaitée, puis les dossiers proposés. Le rapport généré est enregistré dans `outputs/`.

## Exemples de rapports

Des rapports produits avec les données fictives sont disponibles dans le dépôt :

- [Analyse d’une consultation](outputs/analyse_consultation.md)
- [Synthèse d’une entreprise](outputs/resume_entreprise.md)
- [Comparaison entre une entreprise et une consultation](outputs/comparaison_entreprise_consultation.md)

Ces fichiers illustrent le fonctionnement actuel de l’assistant. Leur contenu ne concerne aucune entreprise ni aucun acheteur réel.

## Limites actuelles

- Seuls les documents Markdown sont pris en charge.
- Les sources sont citées par fichier et section, pas encore par page.
- Le projet utilise actuellement un seul agent.
- Il n’existe pas encore de mémoire persistante ni de reprise après interruption.
- Les évaluations automatisées et l’interface web restent à développer.
- Les données fournies servent uniquement à la démonstration.