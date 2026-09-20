# Synthèse de l’entreprise

**Atelier Portail — PME A** est une **entreprise fictive** créée pour un scénario de test ; les informations ci-dessous ne décrivent pas une société réelle. La situation documentaire est donnée au **18 septembre 2026**.  
Sources consultées exclusivement sous `/entreprise/`.

## Activité

Atelier Portail est une entreprise de services numériques implantée à Lyon, créée en 2019, spécialisée dans la réalisation de **portails clients et d’applications métier sur mesure**.

Technologies principales déclarées :

- Symfony et PHP ;
- Vue.js ;
- PostgreSQL ;
- API REST ;
- Docker.

L’entreprise intervient principalement auprès de PME et d’organisations de services, à distance et lors d’ateliers ponctuels sur site en France métropolitaine. Elle propose des projets au forfait après cadrage, ainsi que de la maintenance sous enveloppe de jours.  
Sources : `/entreprise/01_presentation.md`, `/entreprise/05_tarifs.md`.

La méthode de réalisation comprend notamment le cadrage, l’audit de l’existant, le découpage en lots, les démonstrations bimensuelles, la revue de code, les tests, la recette sur environnement dédié, la documentation et le transfert en maintenance.  
Source : `/entreprise/06_methodes_qualite.md`.

## Capacités

### Effectif et organisation

L’effectif déclaré est de **12 salariés**, répartis comme suit :

- direction et commercial : 1 ;
- chef de projet : 1 ;
- développeurs : 6 ;
- UX : 1 ;
- QA : 1 ;
- DevOps : 1 ;
- administration : 1.

Les compétences documentées couvrent notamment la conception d’API, les bases relationnelles, l’organisation d’ateliers, le suivi des risques, la recette, les tests de non-régression, la gestion des environnements, les livraisons et les sauvegardes.  
Source : `/entreprise/02_equipe_competences.md`.

### Périmètre technique et exploitation

L’architecture de référence envisagée repose sur une application conteneurisée, PostgreSQL et des environnements de test et de production séparés. Les contrôles internes déclarés incluent les accès nominatifs, les droits minimaux, l’authentification multifacteur pour les consoles d’administration, la gestion séparée des secrets, le chiffrement des connexions et la journalisation des accès administratifs.

Les objectifs internes de sauvegarde et de reprise sont :

- sauvegarde quotidienne ;
- rétention de 30 jours ;
- restauration testée trimestriellement ;
- perte de données maximale visée : 24 heures ;
- remise en service visée : 2 jours ouvrés.

Ces éléments sont présentés comme des objectifs internes à contractualiser, et non comme des engagements contractuels ou une certification.  
Source : `/entreprise/07_hebergement_securite.md`.

### Support et maintenance

Le support est déclaré disponible du lundi au vendredi, de 9 h à 18 h, heure de Paris, hors jours fériés français. Les objectifs de prise en charge sont :

- P1 : 4 heures de service ;
- P2 : 1 jour ouvré ;
- P3 : 3 jours ouvrés.

La prise en charge correspond à la qualification et au début de l’investigation, et non à une résolution garantie. Il n’existe pas de couverture de nuit, de week-end ou d’astreinte 24 h/24 incluse.  
Source : `/entreprise/08_support_maintenance.md`.

### Capacité disponible déclarée

Les disponibilités agrégées indiquées dans le plan de charge sont les suivantes :

| Fonction | Octobre 2026 | Novembre 2026 | Décembre 2026 |
|---|---:|---:|---:|
| Chef de projet | 8 j.h. | 10 j.h. | 10 j.h. |
| Développeurs | 42 j.h. | 54 j.h. | 60 j.h. |
| UX | 6 j.h. | 8 j.h. | 8 j.h. |
| QA | 8 j.h. | 10 j.h. | 10 j.h. |
| DevOps | 4 j.h. | 6 j.h. | 6 j.h. |

Aucune disponibilité n’est documentée après décembre 2026. Les capacités ne sont pas transférables entre métiers et aucune ressource n’est réservée par la seule analyse d’une consultation. Une validation de la production est nécessaire avant tout engagement.  
Source : `/entreprise/04_plan_charge.md`.

### Positionnement commercial

Le positionnement déclaré est le suivant :

- développement initial : **60 000 à 220 000 € HT** ;
- maintenance en complément ;
- déplacements ponctuels en France métropolitaine.

Cette fourchette constitue un **positionnement commercial** et ne constitue pas, à elle seule, une preuve de capacité technique ou de disponibilité.  
Sources : `/entreprise/01_presentation.md`, `/entreprise/10_preferences.md`.

Les tarifs journaliers de simulation sont compris entre **550 € et 750 € HT par jour-personne**, selon le rôle. Les prix d’hébergement et d’audit externe ne sont pas fournis.  
Source : `/entreprise/05_tarifs.md`.

## Références

Les trois références ci-dessous sont des **expériences déclarées** : aucune n’est étayée par un procès-verbal de recette ou une attestation client indépendante dans le corpus. Les clients sont eux-mêmes fictifs.  
Source principale : `/entreprise/03_references.md`.

### A-R01 — Portail de suivi des commandes

- **Objet :** comptes clients, catalogue, suivi de commandes et connexion à un ERP ;
- **Période :** février 2024 à août 2024 ;
- **Montant :** 145 000 € HT ;
- **Charge :** 210 jours-personnes ;
- **Technologies :** Symfony, Vue.js, PostgreSQL ;
- **Volume déclaré :** 450 comptes ;
- **Limite documentée :** aucune haute disponibilité contractuelle ;
- **Statut de preuve :** fiche déclarative uniquement, non attestée par un tiers.

### A-R02 — Extranet adhérents

- **Objet :** adhésions, documents privés, gestion des rôles et exports ;
- **Période :** janvier 2025 à mai 2025 ;
- **Montant :** 88 000 € HT ;
- **Charge :** 130 jours-personnes ;
- **Technologies :** Symfony, Vue.js ;
- **Volume déclaré :** 1 200 comptes ;
- **Limite documentée :** aucun audit externe d’accessibilité livré ;
- **Statut de preuve :** fiche déclarative uniquement, non attestée par un tiers.

### A-R03 — Maintenance portail métier

- **Objet :** corrections et petites évolutions ;
- **Période :** juillet 2025 à juin 2026 ;
- **Montant :** 42 000 € HT ;
- **Charge :** 60 jours-personnes ;
- **Technologies :** PHP, PostgreSQL ;
- **Résultat déclaré :** 38 tickets clos ;
- **Limite documentée :** support uniquement pendant les heures de service ;
- **Statut de preuve :** fiche déclarative uniquement, non attestée par un tiers.

Les montants des références sont présentés comme des hypothèses de scénario et ne peuvent pas être recalculés à partir du seul tarif journalier actuel.  
Source : `/entreprise/03_references.md`.

## Limites

Les restrictions explicitement documentées sont les suivantes :

- aucune astreinte ou couverture 24 h/24 ;
- aucune référence documentée de migration Java ;
- aucune certification ISO 27001 détenue ;
- aucun audit externe d’accessibilité fourni ;
- aucun audit de sécurité indépendant fourni ;
- aucun taux de couverture de tests documenté ;
- aucun engagement de disponibilité exprimé en pourcentage ;
- aucun contrat d’hébergement signé ni qualification d’un hébergeur ;
- aucun rapport indépendant de test d’intrusion ;
- aucune assurance professionnelle justificative fournie ;
- aucune pièce d’immatriculation ;
- aucune attestation sociale ou fiscale ;
- aucune disponibilité documentée après décembre 2026.

Il convient de distinguer une **capacité explicitement absente** — par exemple l’absence déclarée de certification ISO 27001 ou d’astreinte 24 h/24 — d’une **preuve non fournie**. Ainsi, l’absence d’un audit externe, d’une attestation client ou d’un justificatif administratif dans le corpus ne permet pas de conclure que la capacité ou le document n’existe pas, mais seulement qu’il n’est pas démontré ici.  
Sources : `/entreprise/01_presentation.md`, `/entreprise/02_equipe_competences.md`, `/entreprise/06_methodes_qualite.md`, `/entreprise/07_hebergement_securite.md`, `/entreprise/09_justificatifs.md`.

Cette synthèse ne conclut pas à l’aptitude de l’entreprise à répondre à une consultation particulière ; cette appréciation nécessiterait de comparer ces éléments aux exigences précises du dossier concerné.