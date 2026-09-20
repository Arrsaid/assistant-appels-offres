# Analyse de la consultation

> **Nature de la consultation :** consultation fictive à usage pédagogique, lancée par l’acheteur fictif **Distribution Démo**.  
> **Périmètre documentaire consulté :** uniquement les documents sous `/consultation/`.  
> **Documents consultés :**  
> - `/consultation/01_besoin.md`  
> - `/consultation/02_conditions.md`  
> - `/consultation/annexes/03_exigences_securite.md`

## 1. Besoin

La consultation porte sur la **création d’un portail clients destiné aux clients professionnels** de Distribution Démo.

Le portail devra permettre aux utilisateurs de :

- consulter leurs commandes ;
- télécharger leurs documents ;
- gérer les accès de leurs collaborateurs.

Il devra également :

- échanger des données avec un ERP existant au moyen d’une **API REST** ;
- être développé avec **Symfony et Vue.js** ;
- intégrer des mécanismes de sécurité et de protection des données ;
- être livré avec le code source et la documentation technique ;
- faire l’objet d’un support en semaine, de 9 h à 18 h, heure de Paris.

La documentation de l’API de l’ERP sera fournie lors du cadrage. Les documents demandent également une présentation de l’approche, des références comparables, de l’équipe envisagée, de sa disponibilité, ainsi qu’une estimation argumentée du planning et du budget.

**Sources :** `/consultation/01_besoin.md`, sections « Besoin », « Exigences obligatoires », « Éléments souhaités » et « Réponse attendue » ; `/consultation/02_conditions.md`, sections « Modalités de réponse » et « Critères d’analyse des réponses ».

## 2. Exigences

| Identifiant | Exigence | Nature | Source |
|---|---|---|---|
| EX-01 | Le portail doit permettre aux clients professionnels de consulter leurs commandes. | obligatoire | `/consultation/01_besoin.md`, section « Besoin » |
| EX-02 | Le portail doit permettre aux clients professionnels de télécharger leurs documents. | obligatoire | `/consultation/01_besoin.md`, section « Besoin » |
| EX-03 | Le portail doit permettre de gérer les accès des collaborateurs des clients. | obligatoire | `/consultation/01_besoin.md`, section « Besoin » |
| EX-04 | Le portail doit échanger des données avec l’ERP existant via une API REST. La documentation de l’API sera fournie lors du cadrage. | obligatoire | `/consultation/01_besoin.md`, section « Besoin » |
| EX-05 | Le développement doit être réalisé avec Symfony et Vue.js. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-06 | La réponse doit présenter au moins une référence comparable de portail clients. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-07 | La réponse doit identifier un chef de projet et les compétences mobilisées. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-08 | Un support doit être assuré du lundi au vendredi, de 9 h à 18 h, heure de Paris. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-09 | Le code source et la documentation technique doivent être livrés. | obligatoire | `/consultation/01_besoin.md`, section « Exigences obligatoires » |
| EX-10 | Une expérience d’intégration avec un ERP est souhaitée. | souhaitée | `/consultation/01_besoin.md`, section « Éléments souhaités » |
| EX-11 | La possibilité d’organiser des ateliers ponctuels à Lyon est souhaitée. | souhaitée | `/consultation/01_besoin.md`, section « Éléments souhaités » |
| EX-12 | Les échanges entre les utilisateurs, le portail et les services exposés doivent utiliser HTTPS. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires », point 1 |
| EX-13 | Le portail doit gérer des comptes nominatifs et des droits d’accès différenciés selon les rôles. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires », point 2 |
| EX-14 | Les connexions et les principales actions d’administration doivent être journalisées. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires », point 3 |
| EX-15 | Les données personnelles doivent être protégées conformément aux obligations applicables. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires », point 4 |
| EX-16 | L’architecture technique, les mécanismes d’authentification et les procédures de déploiement doivent être documentés. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires », point 5 |
| EX-17 | Tout incident de sécurité identifié pendant la prestation doit être signalé à l’acheteur. | obligatoire | `/consultation/annexes/03_exigences_securite.md`, section « Exigences obligatoires », point 6 |
| EX-18 | L’hébergement des données au sein de l’Union européenne est souhaité. | souhaitée | `/consultation/annexes/03_exigences_securite.md`, section « Éléments souhaités » |
| EX-19 | Une revue de sécurité avant la mise en service est souhaitée. | souhaitée | `/consultation/annexes/03_exigences_securite.md`, section « Éléments souhaités » |
| EX-20 | Une sensibilisation de l’équipe projet aux principaux risques applicatifs est souhaitée. | souhaitée | `/consultation/annexes/03_exigences_securite.md`, section « Éléments souhaités » |
| EX-21 | La réponse doit être rédigée en français. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-22 | La réponse doit contenir une présentation de l’approche proposée. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-23 | La réponse doit contenir les références comparables. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-24 | La réponse doit présenter l’équipe envisagée et sa disponibilité. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-25 | La réponse doit fournir une estimation argumentée du planning. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-26 | La réponse doit fournir une estimation argumentée du budget. | obligatoire | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| EX-27 | L’hébergement et la maintenance doivent faire l’objet d’un chiffrage séparé. | obligatoire | `/consultation/01_besoin.md`, section « Budget et calendrier » ; `/consultation/02_conditions.md`, sections « Modalités de réponse » et « Conditions financières » |
| EX-28 | La réponse doit présenter une estimation argumentée du planning et du budget, en cohérence avec le besoin. | obligatoire | `/consultation/01_besoin.md`, section « Réponse attendue » |
| EX-29 | Le portail doit prendre en compte les rôles utilisateurs attendus, à préciser pendant le cadrage. | non précisée | `/consultation/annexes/03_exigences_securite.md`, section « Informations à préciser » |
| EX-30 | Les exigences d’authentification, notamment le besoin éventuel de SSO ou de MFA, doivent être précisées pendant le cadrage. | non précisée | `/consultation/annexes/03_exigences_securite.md`, section « Informations à préciser » |
| EX-31 | La durée de conservation des journaux doit être précisée pendant le cadrage. | non précisée | `/consultation/annexes/03_exigences_securite.md`, section « Informations à préciser » |
| EX-32 | Les règles de conservation et de suppression des documents doivent être précisées pendant le cadrage. | non précisée | `/consultation/annexes/03_exigences_securite.md`, section « Informations à préciser » |
| EX-33 | Les interlocuteurs à prévenir en cas d’incident doivent être précisés pendant le cadrage. | non précisée | `/consultation/annexes/03_exigences_securite.md`, section « Informations à préciser » |

## 3. Budget

- Le **budget maximal du développement initial** est de **160 000 EUR HT**.
- Ce montant constitue un **plafond**, et non une simple estimation.
- Il couvre uniquement le **développement initial**.
- L’**hébergement** et la **maintenance** sont explicitement exclus de ce plafond.
- Ces deux postes doivent être présentés dans un **chiffrage séparé**.
- Aucune ventilation détaillée du plafond entre les différents lots ou fonctionnalités n’est fournie.

**Sources :**  
- `/consultation/01_besoin.md`, section « Budget et calendrier » ;  
- `/consultation/02_conditions.md`, sections « Modalités de réponse » et « Conditions financières ».

## 4. Calendrier

| Échéance ou date | Nature | Source |
|---|---|---|
| 30 septembre 2026 à 17 h, heure de Paris | Échéance imposée de remise de la réponse | `/consultation/02_conditions.md`, section « Modalités de réponse » |
| Semaine 41 de 2026 | Date visée pour la décision de sélection ; le jour exact n’est pas précisé | `/consultation/02_conditions.md`, section « Calendrier » |
| Octobre 2026 | Date souhaitée de démarrage ; le jour exact n’est pas précisé | `/consultation/01_besoin.md`, section « Budget et calendrier » ; `/consultation/02_conditions.md`, section « Calendrier » |
| Mars 2027 | Objectif de mise en service ; le jour exact n’est pas précisé | `/consultation/01_besoin.md`, section « Budget et calendrier » ; `/consultation/02_conditions.md`, section « Calendrier » |

Le délai envisagé entre le démarrage souhaité en octobre 2026 et l’objectif de mise en service en mars 2027 est d’environ cinq à six mois selon les dates effectives retenues, mais la consultation ne fixe pas de date journalière précise.

## 5. Points à clarifier

### 5.1 Informations explicitement demandées dans la consultation

Les informations suivantes sont explicitement indiquées comme devant être précisées :

- le nombre d’utilisateurs et les pics de connexion ;
- les caractéristiques et contraintes de l’API de l’ERP ;
- le volume des documents à stocker ;
- la disponibilité de l’équipe proposée ;
- les rôles utilisateurs attendus ;
- les exigences d’authentification, notamment le besoin éventuel de SSO ou de MFA ;
- la durée de conservation des journaux ;
- les règles de conservation et de suppression des documents ;
- les interlocuteurs à prévenir en cas d’incident ;
- les modalités de contractualisation ;
- les modalités de facturation ;
- les modalités de recette.

**Sources :**  
- `/consultation/01_besoin.md`, section « Informations à préciser » ;  
- `/consultation/annexes/03_exigences_securite.md`, section « Informations à préciser » ;  
- `/consultation/02_conditions.md`, section « Informations à préciser par l’acheteur ».

### 5.2 Ambiguïtés ou contradictions relevées

Aucune contradiction explicite n’a été relevée entre les documents consultés.

Les points suivants restent toutefois non précisés ou à encadrer :

- Le périmètre exact des « documents » téléchargeables n’est pas défini.
- Le nombre d’utilisateurs, les pics de connexion et le volume de stockage ne sont pas fournis.
- Les caractéristiques techniques et contraintes de l’API REST de l’ERP ne sont pas encore disponibles ; sa documentation doit être fournie lors du cadrage.
- Les rôles, les droits détaillés et le modèle d’habilitation ne sont pas définis.
- Le besoin éventuel de SSO ou de MFA n’est pas tranché.
- La durée de conservation des journaux et les règles de conservation ou suppression des documents ne sont pas indiquées.
- Le niveau de service attendu pour le support — notamment les délais de prise en charge et de résolution — n’est pas précisé, au-delà des plages horaires.
- Les modalités de contractualisation, de facturation et de recette sont annoncées comme devant être précisées après sélection.
- La consultation ne précise pas si les ateliers à Lyon impliquent des frais, une fréquence ou un nombre maximal de participants.
- La composition détaillée des chiffrages d’hébergement et de maintenance n’est pas définie.

Ces éléments constituent des informations manquantes, et non des exigences implicitement obligatoires.

### 5.3 Suggestions de l’agent, non formulées dans la consultation

- Quel est le périmètre fonctionnel exact de la gestion des commandes : consultation uniquement, recherche, filtres, historique, téléchargement de bons de commande ou d’autres actions ?
- Quels types de documents seront accessibles et quels contrôles d’autorisation devront s’appliquer à chacun ?
- L’ERP impose-t-il des contraintes de fréquence, de disponibilité, de pagination, de volumétrie ou de limitation des appels API ?
- Quel niveau de disponibilité et de performance est attendu pour le portail ?
- Quels sont les délais cibles de prise en charge et de résolution des incidents pendant les horaires de support ?
- Une reprise ou un import de données existantes est-il prévu ?
- Quels environnements doivent être fournis : développement, recette, préproduction et production ?
- Quels sont les critères d’acceptation et les scénarios de recette attendus ?
- Quelles obligations ou politiques internes s’appliquent à la protection des données personnelles ?
- Les coûts récurrents d’hébergement et de maintenance doivent-ils être présentés mensuellement, annuellement ou selon plusieurs scénarios ?
- La revue de sécurité souhaitée doit-elle être réalisée par l’équipe projet ou par un tiers indépendant ?

## 6. Critères d’analyse des réponses

Les réponses seront examinées selon les pondérations suivantes :

| Critère | Pondération |
|---|---:|
| Compréhension du besoin et approche proposée | 35 % |
| Références comparables et expérience d’intégration ERP | 25 % |
| Organisation, équipe et disponibilité | 20 % |
| Cohérence du planning et du budget | 20 % |

**Source :** `/consultation/02_conditions.md`, section « Critères d’analyse des réponses ».

Aucune conclusion n’est formulée ici sur les capacités d’une entreprise ou sur l’opportunité de répondre, conformément au périmètre de la consultation.