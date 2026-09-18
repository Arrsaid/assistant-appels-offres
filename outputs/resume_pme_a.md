Voici une analyse structurée de la consultation sélectionnée, en restant strictement sur les documents fournis et sans comparaison avec une entreprise. Sources indiquées entre chaque élément.

Constats préalables
- Cadre documentaire: les éléments proviennent des documents fictifs de PME A — Atelier Portail.
  - Présentation de l’entreprise: activité, limites et cadre technique ( /entreprise/01_presentation.md ).
  - Références de missions: exemples de périmètres et livrables passés ( /entreprise/03_references.md ).
- Note sur le caractère fictif: les documents précisent que les données et scénarios sont synthétiques et destinés au test.

1) Besoin (objet de la consultation)
- Besoin apparent et cadre général:
  - Le document indique que l’entreprise est active dans le développement de « portails clients et applications métier sur mesure », ce qui situe le champ des prestations attendues ( /entreprise/01_presentation.md, section Activité ).
  - Le scénario mentionne « PME A — Atelier Portail », suggérant un besoin de développement/portail dans le cadre d’un projet portails client et/ou portail métier ( /entreprise/01_presentation.md, section Identité de scénario et Activité ).
- Formulation du besoin (hypothèse fondée sur les documents):
  - Développement initial d’un portail client et/ou portail métier sur mesure, avec maintenance en complément (cf. Positionnement commercial : « Développement initial de 60 000 à 220 000 EUR HT ; maintenance en complément ») ( /entreprise/01_presentation.md).
- Source des éléments: 
  - /entreprise/01_presentation.md — Activité; Limites explicites; Positionnement commercial.

2) Exigences (détaillées)
Remarque: les documents ne donnent pas une liste explicite “EXIGENCES” sous forme de cahier des charges, mais on peut en déduire des éléments fonctionnels et des contraintes à partir des descriptions de missions et des limites. Ci-dessous, chaque exigence est identifiée avec une source et une nature marquée comme “non précisée” lorsque non explicitée dans les textes.

- Exigence EX-01
  - Intitulé: Portail de suivi des commandes et intégration potentielle à un ERP (périmètre et limites observés dans les projets référencés).
  - Nature: non précisée
  - Source: /entreprise/03_references.md — A-R01, section Périmètre et limites (Portail de suivi des commandes; integração ERP évoquée).
- Exigence EX-02
  - Intitulé: Gestion des comptes clients, catalogue et exports (capacité d’export et gestion des comptes), comme exemples de périmètre dans des missions similaires.
  - Nature: non précisée
  - Source: /entreprise/03_references.md — A-R01, section Périmètre et limites (comptes clients, catalogue, suivi, connexion à ERP; 450 comptes).
- Exigence EX-03
  - Intitulé: Maintenance du portail métier (corrective et évolutive sur un périmètre défini).
  - Nature: non précisée
  - Source: /entreprise/03_references.md — A-R03, section Périmètre et limites (Maintenance portail métier; 60 tickets clos; support en heures de service).
- Exigence EX-04
  - Intitulé: Adhésions/exports et gestion associée (définition de rôles et exports; pertinence des comptes dans les modules d’adhésion dans des exemples de mission).
  - Nature: non précisée
  - Source: /entreprise/03_references.md — A-R02, section Périmètre et limites (Extranet adhérents; 1 200 comptes; adhésions, documents privés, etc.).

3) Budget
- Budget de la consultation (à préciser lors du cadrage, selon les documents):
  - Développement initial: 60 000 à 220 000 EUR HT (domaine “Développement initial” indiqué comme couverture budgétaire du lancement du portail) ( /entreprise/01_presentation.md, section Positionnement commercial ).
  - Maintenance: mentionnée comme complément au développement initial (mêmes sources).
- Budget des projets de référence (pour contexte, sans intention de ventilation):
  - A-R01 Portail de suivi des commandes: 145 000 EUR HT ( /entreprise/03_references.md, A-R01 ).
  - A-R02 Extranet adhérents: 88 000 EUR HT ( /entreprise/03_references.md, A-R02 ).
  - A-R03 Maintenance portail métier: 42 000 EUR HT ( /entreprise/03_references.md, A-R03 ).

4) Calendrier (échéances et timing)
- Calendrier explicite dans la consultation: pas d échéance client explicitement indiquée dans les documents fournis pour la présente consultation.
- Éléments temporels disponibles dans les documents de référence (pour contexte et comparaison):
  - A-R01 Portail de suivi des commandes: période 2024-02 à 2024-08 ( /entreprise/03_references.md, A-R01 ).
  - A-R02 Extranet adhérents: période 2025-01 à 2025-05 ( /entreprise/03_references.md, A-R02 ).
  - A-R03 Maintenance portail métier: période 2025-07 à 2026-06 ( /entreprise/03_references.md, A-R03 ).
- Note: ces périodes servent de contexte sur des projets similaires et ne doivent pas être interprétées comme le calendrier de la consultation actuelle (document fictif ne précise pas de deadlines client).

5) Points à clarifier (à discuter avec le client)
- Clarifier le périmètre exact du portail et les intégrations:
  - Quelles sont les fonctionnalités attendues exactement (fournies par le besoin du client) et quelles interfaces doivent être connectées (ERP, catalogue, exports, etc.) ? (sources: A-R01 décrit un périmètre incluant comptes, catalogue, suivi des commandes et ERP; c’est une référence utile mais la liste exacte des attentes du client doit être confirmée) [ /entreprise/03_references.md, A-R01; /entreprise/01_presentation.md, Activité et Périmètre implicite ].
- Clarifier le niveau de disponibilité et le modèle de support:
  - Limites explicites indiquent qu’il n’y a pas d’astreinte 24/7; confirmer les niveaux de service attendus et les SLA (horaires de support, réactivité, etc.) [ /entreprise/01_presentation.md, Limites explicites ].
- Clarifier les exigences de sécurité et de conformité:
  - ISO 27001 n’est pas détenue par l’entreprise; y a-t-il des exigences de conformité spécifiques à la consultation (accès, logs, auditabilité, etc.) et/ ou un audit accessible à prévoir? [ /entreprise/01_presentation.md, Limites explicites ].
- Clarifier les exigences d’accessibilité et d’audit:
  - Aucun audit externe d’accessibilité fourni dans les références; des exigences WCAG ou équivalentes seront-elles nécessaires? [ /entreprise/01_presentation.md, Limites explicites ; /entreprise/03_references.md, A-R01 ].
- Clarifier le budget et les livrables attendus:
  - Confirmer l’enveloppe budgétaire et la ventilation attendue entre développement initial et maintenance, ainsi que les livrables (maquettes, code source, documentation, tests, recettes, etc.). [ /entreprise/01_presentation.md, Positionnement commercial ].
- Clarifier le calendrier et les jalons:
  - Définir les échéances imposées et les objectifs temporels (délivrables, recettes, mises en production). Les périodes historiques des projets de référence peuvent servir de repères, mais le calendrier client doit être établi explicitement [ /entreprise/03_references.md, A-R01/A-R02/A-R03 ].
- Modalités de collaboration et déploiement:
  - Mode de travail (remote vs sur site, ateliers, nombre d’intervenants, restitution intermédiaire), et localisation (Lyon est mentionné comme base dans la présentation, à confirmer pour le projet courant) [ /entreprise/01_presentation.md, Identité de scénario ].

Remarques et limites
- Les documents utilisés sont fictifs et destinés à des scénarios de test. Toute conclusion ou chiffre tiré de ces documents doit être validé avec le client réel lors du cadrage.
- L’objectif ici est uniquement de cartographier le besoin potentiel, les exigences, le cadre budgétaire et le calendrier, ainsi que les questions à clarifier, sans décider de la réponse à la consultation.

Sources utilisées
- /entreprise/01_presentation.md
  - Activité: Portails clients et applications métier sur mesure
  - Limites explicites: pas d’astreinte 24/7, pas de migration Java, pas de ISO 27001, pas d’audit externe d’accessibilité fourni
  - Positionnement commercial: Développement initial de 60 000 à 220 000 EUR HT; maintenance en complément
  - Dossier: PME A — Atelier Portail (scénario fictif)
- /entreprise/03_references.md
  - A-R01 — Portail de suivi des commandes: 145 000 EUR HT; période 2024-02 à 2024-08; 450 comptes; intégration ERP; périmètre incluant comptes, catalogue, suivi de commandes
  - A-R02 — Extranet adhérents: 88 000 EUR HT; période 2025-01 à 2025-05; 1 200 comptes; adhésions, documents privés, rôles et exports
  - A-R03 — Maintenance portail métier: 42 000 EUR HT; période 2025-07 à 2026-06; 60 tickets clos; support en heures de service

Souhaitez-vous que je reformule cette analyse sous forme d’un tableau clair EX-01, EX-02, etc., avec une mise en table directement exploitable pour un dossier de consultation ? Je peux aussi préparer une checklist de clarifications à envoyer au client.