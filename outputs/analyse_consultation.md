# Analyse de la consultation

> Consultation explicitement fictive, à usage pédagogique, concernant l’acheteur fictif **Distribution Démo**.  
> Sources consultées exclusivement sous `/consultation/`.

## Besoin

La consultation porte sur la **création d’un portail clients destiné aux clients professionnels**.

Le portail devra permettre :

- la consultation des commandes ;
- le téléchargement des documents ;
- la gestion des accès des collaborateurs ;
- l’échange de données avec un ERP existant au moyen d’une API REST.

La documentation de l’API ERP sera fournie lors du cadrage. Le projet devra également intégrer des exigences de sécurité, de gestion des droits, de traçabilité et de protection des données.

La réponse attendue doit présenter l’approche proposée, les références comparables, l’équipe envisagée, sa disponibilité, ainsi qu’une estimation argumentée du planning et du budget. Un chiffrage séparé est demandé pour l’hébergement et la maintenance.

**Sources :**

- `/consultation/01_besoin.md`, sections « Besoin », « Exigences obligatoires », « Éléments souhaités » et « Réponse attendue » ;
- `/consultation/annexes/03_exigences_securite.md`, sections « Exigences obligatoires » et « Éléments souhaités ».

## Exigences

| Identifiant | Exigence | Nature | Source |
|---|---|---|---|
| EX-01 | Permettre aux clients professionnels de consulter leurs commandes. | obligatoire | `/consultation/01_besoin.md`, section « Besoin » |
| EX-02 | Permettre aux clients professionnels de télécharger leurs documents. | obligatoire | `/consultation/01_besoin.md`, section « Besoin » |
| EX-03 | Permettre aux clients de gérer les accès de leurs collaborateurs. | obligatoire | `/consultation/01_besoin.md`, section « Besoin » |
| EX-04 | Échanger des données avec l’ERP existant via une API REST. La documentation de l’API sera fournie lors du cadrage. | obligatoire | `/consultation/01_besoin.md`, section « Besoin » |
| EX-05 | Développer le portail avec Symfony et Vue.js. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-06 | Présenter au moins une référence comparable de portail clients. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-07 | Identifier un chef de projet et les compétences mobilisées. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-08 | Assurer un support du lundi au vendredi, de 9 h à 18 h, heure de Paris. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-09 | Livrer le code source et la documentation technique. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-10 | Présenter une expérience d’intégration avec un ERP. | souhaitée | `/consultation/01_besoin.md`, section « Éléments souhaités » |
| EX-11 | Permettre l’organisation d’ateliers ponctuels à Lyon. | souhaitée | `/consultation/01_besoin.md`, section « Éléments souhaités » |
| EX-12 | Utiliser HTTPS pour tous les échanges entre les utilisateurs, le portail et les services exposés. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires » |
| EX-13 | Gérer des comptes nominatifs et des droits d’accès différenciés selon les rôles. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires » |
| EX-14 | Journaliser les connexions et les principales actions d’administration. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires » |
| EX-15 | Protéger les données personnelles conformément aux obligations applicables. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires » |
| EX-16 | Documenter l’architecture technique, les mécanismes d’authentification et les procédures de déploiement. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires » |
| EX-17 | Signaler à l’acheteur tout incident de sécurité identifié pendant la prestation. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires » |
| EX-18 | Héberger les données au sein de l’Union européenne. | souhaitée | `/consultation/annexes/03_exigences_securite.md`, section « Éléments souhaités » |
| EX-19 | Réaliser une revue de sécurité avant la mise en service. | souhaitée | `/consultation/annexes/03_exigences_securite.md`, section « Éléments souhaités » |
| EX-20 | Sensibiliser l’équipe projet aux principaux risques applicatifs. | souhaitée | `/consultation/annexes/03_exigences_securite.md`, section « Éléments souhaités » |
| EX-21 | Rédiger la réponse en français. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-22 | Présenter dans la réponse l’approche proposée. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-23 | Présenter dans la réponse les références comparables. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-24 | Présenter l’équipe envisagée et sa disponibilité. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-25 | Fournir une estimation argumentée du planning. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-26 | Fournir une estimation argumentée du budget. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-27 | Fournir un chiffrage séparé pour l’hébergement et la maintenance. | obligatoire | `/consultation/02_conditions.md`, sections « Modalités de réponse » et « Conditions financières » |
| EX-28 | Respecter les critères d’analyse annoncés : compréhension du besoin et approche proposée — 35 %. | non précisée | `/consultation/02_conditions.md`, section « Critères d’analyse des réponses » |
| EX-29 | Références comparables et expérience d’intégration ERP — pondération de 25 %. | non précisée | `/consultation/02_conditions.md`, section « Critères d’analyse des réponses » |
| EX-30 | Organisation, équipe et disponibilité — pondération de 20 %. | non précisée | `/consultation/02_conditions.md`, section « Critères d’analyse des réponses » |
| EX-31 | Cohérence du planning et du budget — pondération de 20 %. | non précisée | `/consultation/02_conditions.md`, section « Critères d’analyse des réponses » |

Les critères EX-28 à EX-31 sont des critères d’analyse et ne sont pas formulés comme des prestations techniques ou des conditions d’éligibilité. Leur nature est donc indiquée comme **non précisée** plutôt que comme obligatoire.

## Budget

- Le budget maximal du développement initial est de **160 000 EUR HT**.
- Ce plafond couvre uniquement le **développement initial**.
- L’hébergement et la maintenance sont explicitement exclus de ce plafond.
- L’hébergement et la maintenance doivent faire l’objet d’un **chiffrage séparé**.
- Aucune ventilation budgétaire détaillée n’est fournie.
- Le document demande une estimation argumentée du budget, sans préciser de format de décomposition ou de taux journalier attendu.

**Sources :**

- `/consultation/01_besoin.md`, section « Budget et calendrier » ;
- `/consultation/02_conditions.md`, sections « Modalités de réponse » et « Conditions financières ».

## Calendrier

### Échéance imposée

- La réponse doit être transmise au plus tard le **30 septembre 2026 à 17 h, heure de Paris**.

**Source :** `/consultation/02_conditions.md`, section « Modalités de réponse ».

### Date visée

- La décision de sélection est visée en **semaine 41 de 2026**. Le jour exact n’est pas précisé.

**Source :** `/consultation/02_conditions.md`, section « Calendrier ».

### Dates souhaitées ou objectifs

- Démarrage souhaité : **octobre 2026**.
- Objectif de mise en service : **mars 2027**.

Ces dates ne sont pas présentées comme des échéances contractuelles fermes dans les documents consultés.

**Sources :**

- `/consultation/01_besoin.md`, section « Budget et calendrier » ;
- `/consultation/02_conditions.md`, section « Calendrier ».

## Points à clarifier

### Informations explicitement demandées dans la consultation

La consultation demande de préciser :

- le nombre d’utilisateurs ;
- les pics de connexion ;
- les caractéristiques et contraintes de l’API de l’ERP ;
- le volume des documents à stocker ;
- la disponibilité de l’équipe proposée.

**Source :** `/consultation/01_besoin.md`, section « Informations à préciser ».

L’annexe sécurité indique également que l’acheteur devra préciser pendant le cadrage :

- les rôles utilisateurs attendus ;
- les exigences d’authentification, notamment l’éventuel besoin de SSO ou de MFA ;
- la durée de conservation des journaux ;
- les règles de conservation et de suppression des documents ;
- les interlocuteurs à prévenir en cas d’incident.

**Source :** `/consultation/annexes/03_exigences_securite.md`, section « Informations à préciser ».

Enfin, les modalités de contractualisation, de facturation et de recette seront précisées après sélection.

**Source :** `/consultation/02_conditions.md`, section « Informations à préciser par l’acheteur ».

### Ambiguïtés ou contradictions relevées

Aucune contradiction explicite n’a été relevée entre les documents consultés.

Les points suivants restent toutefois non précisés :

- le nombre exact d’utilisateurs et les niveaux de charge attendus ;
- les caractéristiques techniques de l’API REST de l’ERP ;
- les rôles utilisateurs et la matrice détaillée des droits ;
- le besoin éventuel de SSO ou de MFA ;
- la durée de conservation des journaux ;
- les règles de conservation et de suppression des documents ;
- le volume des documents à stocker ;
- les modalités précises de contractualisation, de facturation et de recette ;
- le détail des niveaux de service attendus pour le support ;
- la définition opérationnelle de la « mise en service » de mars 2027 ;
- le jour exact correspondant à la semaine 41 de 2026 ;
- le périmètre exact de la documentation technique et des procédures de déploiement ;
- le détail des prestations incluses dans le développement initial plafonné à 160 000 EUR HT.

### Suggestions de l’agent, non formulées dans la consultation

- Demander si les utilisateurs finaux devront bénéficier d’une interface d’administration distincte.
- Clarifier les systèmes et flux ERP concernés : commandes, documents, comptes utilisateurs et éventuels statuts de traitement.
- Demander les exigences de disponibilité, de temps de réponse et de reprise après incident.
- Préciser les environnements attendus : développement, recette, préproduction et production.
- Définir les modalités de validation fonctionnelle et les critères d’acceptation.
- Clarifier les responsabilités respectives de l’acheteur et du prestataire pour l’exploitation, la supervision et le traitement des incidents.
- Demander si des contraintes d’accessibilité, de compatibilité navigateurs ou de responsive design sont attendues.
- Préciser les modalités de transfert de compétences et de remise des livrables au terme du projet.

## Synthèse

La consultation vise un portail clients professionnel connecté à un ERP par API REST, développé avec Symfony et Vue.js, intégrant des fonctions de consultation de commandes, téléchargement de documents et gestion des accès collaborateurs. Les exigences de sécurité et de protection des données sont détaillées dans une annexe dédiée.

Le développement initial est plafonné à **160 000 EUR HT**, hors hébergement et maintenance. La réponse est exigée avant le **30 septembre 2026 à 17 h**, pour un démarrage souhaité en **octobre 2026** et une mise en service visée en **mars 2027**.