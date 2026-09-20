# Synthèse de l’entreprise

> **Entreprise fictive** : les informations ci-dessous proviennent d’un dossier de scénario et ne décrivent pas une entreprise réelle.

## Activité

Atelier Portail est une entreprise de services numériques implantée à Lyon et créée en 2019. Elle intervient principalement dans la conception de portails clients et d’applications métier sur mesure, pour des PME et des organisations de services.

Ses principales technologies déclarées sont :

- Symfony et PHP ;
- Vue.js ;
- PostgreSQL ;
- API REST ;
- Docker.

L’intervention combine réalisation à distance et ateliers ponctuels sur site, principalement en France métropolitaine. La méthode de réalisation comprend notamment le cadrage, le découpage en lots, les démonstrations bimensuelles, la revue de code, les tests, la recette et le transfert en maintenance.  
**Sources :** `/entreprise/01_presentation.md`, `/entreprise/02_equipe_competences.md`, `/entreprise/06_methodes_qualite.md`.

## Capacités

### Effectif et organisation

L’effectif déclaré est de **12 salariés**, répartis comme suit :

- 1 personne en direction et commercial ;
- 1 chef de projet ;
- 6 développeurs ;
- 1 UX ;
- 1 QA ;
- 1 DevOps ;
- 1 personne en administration.

Le chef de projet couvre les ateliers, le suivi des risques, le budget et la recette. Le profil QA intervient sur les scénarios de test, les campagnes de non-régression et le suivi des anomalies. Le DevOps est chargé des environnements, des livraisons et des sauvegardes.  
**Source :** `/entreprise/02_equipe_competences.md`.

### Périmètre technique et opérationnel

L’entreprise déclare des compétences en développement web, conception d’API, bases de données relationnelles, conteneurisation, tests, déploiement et maintenance applicative. Son architecture de référence prévoit des environnements de test et de production séparés, une application conteneurisée et une base PostgreSQL.

Les contrôles internes décrits comprennent notamment les accès nominatifs, les droits minimaux, l’authentification multifacteur pour les consoles d’administration, le chiffrement des connexions et la journalisation des accès administratifs. Les objectifs internes annoncés sont une sauvegarde quotidienne avec rétention de 30 jours, une perte de données maximale de 24 heures et une remise en service cible de deux jours ouvrés. Ces objectifs doivent être contractualisés et ne constituent pas un engagement général de disponibilité.  
**Sources :** `/entreprise/06_methodes_qualite.md`, `/entreprise/07_hebergement_securite.md`.

### Capacité disponible documentée

Les disponibilités sont exprimées en jours-personnes agrégés et ne sont fournies que jusqu’à décembre 2026 :

| Fonction | Octobre 2026 | Novembre 2026 | Décembre 2026 |
|---|---:|---:|---:|
| Chef de projet | 8 | 10 | 10 |
| Développeurs | 42 | 54 | 60 |
| UX | 6 | 8 | 8 |
| QA | 8 | 10 | 10 |
| DevOps | 4 | 6 | 6 |

Les fonctions direction/commercial et administration ne sont pas mobilisables pour la production. Les jours ne sont pas transférables entre métiers et aucune ressource n’est réservée automatiquement par l’analyse d’un dossier. Une validation de la production est nécessaire avant tout engagement.  
**Source :** `/entreprise/04_plan_charge.md`.

### Positionnement commercial

L’entreprise se positionne sur :

- des développements initiaux de **60 000 à 220 000 € HT** ;
- des prestations de maintenance en complément ;
- des projets au forfait après cadrage ;
- de la maintenance sous enveloppe de jours.

Cette fourchette constitue un **positionnement commercial déclaré**, et non une preuve de capacité technique ou de disponibilité. Les tarifs journaliers de simulation sont compris entre 550 € et 750 € HT selon le rôle. Les coûts d’hébergement, d’audit externe, de licences, de déplacements et de sous-traitance restent à déterminer séparément.  
**Sources :** `/entreprise/01_presentation.md`, `/entreprise/05_tarifs.md`, `/entreprise/10_preferences.md`.

## Références

Les trois références sont présentées comme des **expériences déclaratives** : aucune attestation client indépendante ni procès-verbal de recette n’est fourni dans le corpus. Les clients et projets sont fictifs.

### A-R01 — Portail de suivi des commandes

- **Objet :** comptes clients, catalogue, suivi de commandes et connexion à un ERP ;
- **Période :** février à août 2024 ;
- **Montant :** 145 000 € HT ;
- **Charge :** 210 jours-personnes ;
- **Technologies :** Symfony, Vue.js, PostgreSQL ;
- **Volume :** 450 comptes ;
- **Limite documentée :** aucune haute disponibilité contractuelle ;
- **Caractère de l’information :** fiche déclarative non attestée par un tiers ;
- **Source :** `/entreprise/03_references.md`.

### A-R02 — Extranet adhérents

- **Objet :** gestion des adhésions, documents privés, rôles et exports ;
- **Période :** janvier à mai 2025 ;
- **Montant :** 88 000 € HT ;
- **Charge :** 130 jours-personnes ;
- **Technologies :** Symfony, Vue.js ;
- **Volume :** 1 200 comptes ;
- **Limite documentée :** aucun audit externe d’accessibilité livré ;
- **Caractère de l’information :** fiche déclarative non attestée par un tiers ;
- **Source :** `/entreprise/03_references.md`.

### A-R03 — Maintenance de portail métier

- **Objet :** corrections et petites évolutions ;
- **Période :** juillet 2025 à juin 2026 ;
- **Montant :** 42 000 € HT ;
- **Charge :** 60 jours-personnes ;
- **Technologies :** PHP, PostgreSQL ;
- **Résultat déclaré :** 38 tickets clos ;
- **Limite documentée :** support uniquement pendant les heures de service ;
- **Caractère de l’information :** fiche déclarative non attestée par un tiers ;
- **Source :** `/entreprise/03_references.md`.

## Limites

Les restrictions explicitement documentées sont les suivantes :

- pas d’astreinte ni de couverture 24 h/24 ;
- support limité du lundi au vendredi, de 9 h à 18 h, heure de Paris, hors jours fériés ;
- pas de référence documentée en migration Java ;
- aucune certification ISO 27001 détenue dans le scénario ;
- aucun audit externe d’accessibilité fourni ;
- aucun audit indépendant de sécurité ou test d’intrusion fourni ;
- aucun engagement de disponibilité en pourcentage fixé ;
- aucun contrat d’hébergement signé ni qualification d’hébergeur fournie ;
- aucune assurance professionnelle, pièce d’immatriculation ou attestation sociale et fiscale produite dans le corpus ;
- aucun taux de couverture de tests ni résultat d’audit réel communiqué ;
- aucune disponibilité documentée au-delà de décembre 2026.

Ces éléments distinguent une **capacité explicitement limitée ou non détenue** — par exemple l’absence d’astreinte 24 h/24 ou de certification ISO 27001 — d’une **preuve simplement non fournie**, comme l’assurance professionnelle, la qualification de l’hébergeur ou les attestations clients.  
**Sources :** `/entreprise/01_presentation.md`, `/entreprise/02_equipe_competences.md`, `/entreprise/04_plan_charge.md`, `/entreprise/07_hebergement_securite.md`, `/entreprise/08_support_maintenance.md`, `/entreprise/09_justificatifs.md`.

Cette synthèse décrit les capacités et déclarations présentes dans le dossier fictif ; elle ne conclut pas à l’aptitude de l’entreprise à répondre à une consultation particulière.