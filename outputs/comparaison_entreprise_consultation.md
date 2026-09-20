## Documents consultés

### Consultation
- `/consultation/01_besoin.md`
- `/consultation/02_conditions.md`
- `/consultation/annexes/03_exigences_securite.md`

### Entreprise
- `/entreprise/01_presentation.md`
- `/entreprise/02_equipe_competences.md`
- `/entreprise/03_references.md`
- `/entreprise/04_plan_charge.md`
- `/entreprise/05_tarifs.md`
- `/entreprise/06_methodes_qualite.md`
- `/entreprise/07_hebergement_securite.md`
- `/entreprise/08_support_maintenance.md`
- `/entreprise/09_justificatifs.md`
- `/entreprise/10_preferences.md`

> Les données de la consultation et de l’entreprise sont explicitement fictives et utilisées à des fins pédagogiques ou de test.

## Matrice de comparaison

| Identifiant | Exigence | Nature | Élément entreprise | Constat | Sources |
|---|---|---|---|---|---|
| CMP-01 | Créer un portail permettant de consulter les commandes, télécharger des documents et gérer les accès des collaborateurs | Besoin fonctionnel | L’entreprise se positionne sur les portails clients et applications métier. La référence A-R01 couvre les comptes clients, le suivi de commandes et une connexion à un ERP ; A-R02 couvre les documents privés et les rôles. | **Couvert par des éléments déclaratifs**, avec des périmètres proches documentés dans deux références. La gestion précise des collaborateurs reste à détailler. | Consultation : `/consultation/01_besoin.md`, § Besoin. Entreprise : `/entreprise/01_presentation.md`, § Activité ; `/entreprise/03_references.md`, § A-R01 et A-R02. |
| CMP-02 | Échanger des données avec un ERP existant via une API REST | Exigence fonctionnelle et technique | L’entreprise déclare des compétences en API REST. A-R01 mentionne une connexion à un ERP et utilise Symfony, Vue.js et PostgreSQL. | **Couvert par des éléments déclaratifs** et une référence proche. Les caractéristiques de l’ERP et de son API ne sont toutefois pas encore connues. | Consultation : `/consultation/01_besoin.md`, § Besoin et § Informations à préciser. Entreprise : `/entreprise/01_presentation.md`, § Activité ; `/entreprise/02_equipe_competences.md`, § Compétences ; `/entreprise/03_references.md`, § A-R01. |
| CMP-03 | Développement avec Symfony et Vue.js | Exigence obligatoire | Symfony et Vue.js figurent parmi les technologies principales. Les références A-R01 et A-R02 documentent leur utilisation. | **Couvert par des éléments déclaratifs**. Les documents ne fournissent pas de preuve indépendante, mais font état d’usages en projet. | Consultation : `/consultation/01_besoin.md`, § Exigences obligatoires. Entreprise : `/entreprise/01_presentation.md`, § Activité ; `/entreprise/02_equipe_competences.md`, § Compétences ; `/entreprise/03_references.md`, § A-R01 et A-R02. |
| CMP-04 | Présenter au moins une référence comparable de portail clients | Exigence obligatoire | A-R01 est un portail de suivi des commandes avec comptes clients et 450 comptes. A-R02 est un extranet avec documents privés, rôles et 1 200 comptes. | **Couvert par des éléments déclaratifs**. Les références sont comparables, mais aucune attestation client ni procès-verbal de recette indépendant n’est fourni. | Consultation : `/consultation/01_besoin.md`, § Exigences obligatoires. Entreprise : `/entreprise/03_references.md`, § A-R01 et A-R02 ; `/entreprise/09_justificatifs.md`, § État documentaire de simulation. |
| CMP-05 | Identifier un chef de projet et les compétences mobilisées | Exigence obligatoire | L’équipe comprend un chef de projet, six développeurs, un UX, un QA et un DevOps. Le profil pme_a-CP01 est décrit comme chef de projet ayant participé à A-R02. | **Couvert par des éléments déclaratifs**. Les personnes effectivement affectées et leurs disponibilités doivent encore être validées. | Consultation : `/consultation/01_besoin.md`, § Exigences obligatoires. Entreprise : `/entreprise/02_equipe_competences.md`, § Répartition et § Profils individuels ; `/entreprise/04_plan_charge.md`, § Décision d’affectation. |
| CMP-06 | Assurer un support du lundi au vendredi, de 9 h à 18 h, heure de Paris | Exigence obligatoire | L’entreprise indique une couverture du lundi au vendredi, de 9 h à 18 h, heure de Paris, hors jours fériés français. | **Partiellement couvert ou à confirmer** : les horaires correspondent, mais l’exclusion des jours fériés français doit être confrontée aux attentes contractuelles précises de l’acheteur. Les délais de prise en charge sont documentés, sans garantie de résolution. | Consultation : `/consultation/01_besoin.md`, § Exigences obligatoires. Entreprise : `/entreprise/08_support_maintenance.md`, § Couverture et § Qualification des incidents. |
| CMP-07 | Livrer le code source et la documentation technique | Exigence obligatoire | Les livrables déclarés comprennent le code source, la documentation d’installation, les résultats de tests et le compte rendu de recette. | **Couvert par des éléments déclaratifs**. La correspondance exacte entre la documentation attendue et la documentation technique demandée doit être confirmée dans la proposition ou le cadrage. | Consultation : `/consultation/01_besoin.md`, § Exigences obligatoires. Entreprise : `/entreprise/06_methodes_qualite.md`, § Livrables. |
| CMP-08 | Expérience d’intégration avec un ERP | Élément souhaité et critère d’analyse | A-R01 mentionne une connexion à un ERP dans un portail de suivi de commandes. | **Couvert par des éléments déclaratifs**, sur la base d’une référence unique dans le corpus. La nature de l’ERP et les modalités techniques d’intégration ne sont pas précisées. | Consultation : `/consultation/01_besoin.md`, § Éléments souhaités ; `/consultation/02_conditions.md`, § Critères d’analyse. Entreprise : `/entreprise/03_references.md`, § A-R01. |
| CMP-09 | Pouvoir organiser des ateliers ponctuels à Lyon | Élément souhaité | L’entreprise est implantée à Lyon et indique réaliser des ateliers ponctuels sur site, avec des déplacements en France métropolitaine. | **Couvert par des éléments déclaratifs**. Les modalités et la fréquence des ateliers restent à définir. | Consultation : `/consultation/01_besoin.md`, § Éléments souhaités. Entreprise : `/entreprise/01_presentation.md`, § Clients et mode d’intervention et § Positionnement commercial. |
| CMP-10 | Respecter un budget maximal de 160 000 EUR HT pour le développement initial | Contrainte financière obligatoire | L’entreprise annonce une fourchette de développement initial de 60 000 à 220 000 EUR HT. Elle dispose de tarifs par rôle, mais aucun chiffrage spécifique de cette consultation n’est établi. | **Partiellement couvert ou à confirmer** : la fourchette commerciale inclut des projets sous le plafond, mais peut également le dépasser. Une estimation détaillée est nécessaire ; il ne faut pas assimiler la fourchette commerciale au budget client. | Consultation : `/consultation/01_besoin.md`, § Budget et calendrier ; `/consultation/02_conditions.md`, § Conditions financières. Entreprise : `/entreprise/01_presentation.md`, § Positionnement commercial ; `/entreprise/05_tarifs.md`, § Grille et § Construction d’une estimation. |
| CMP-11 | Chiffrer séparément l’hébergement et la maintenance | Exigence de réponse et contrainte financière | L’entreprise indique que la maintenance est facturée en complément. Les prix d’hébergement ne sont pas fournis et un devis doit être obtenu. | **Partiellement couvert ou à confirmer** : la séparation commerciale est compatible, mais les montants d’hébergement et, à ce stade, de maintenance ne sont pas documentés. | Consultation : `/consultation/01_besoin.md`, § Budget et calendrier ; `/consultation/02_conditions.md`, § Modalités de réponse et § Conditions financières. Entreprise : `/entreprise/05_tarifs.md`, § Construction d’une estimation ; `/entreprise/01_presentation.md`, § Positionnement commercial. |
| CMP-12 | Démarrage souhaité en octobre 2026 et mise en service visée en mars 2027 | Calendrier souhaité / objectif client | Le plan de charge fournit des disponibilités uniquement pour octobre, novembre et décembre 2026. Il indique qu’aucune disponibilité n’est fournie après décembre. | **Partiellement couvert ou à confirmer** : certaines capacités existent au démarrage, mais la faisabilité jusqu’à mars 2027 ne peut pas être établie avec le corpus actuel. | Consultation : `/consultation/01_besoin.md`, § Budget et calendrier ; `/consultation/02_conditions.md`, § Calendrier. Entreprise : `/entreprise/04_plan_charge.md`, tableau de capacité et § Décision d’affectation. |
| CMP-13 | Fournir une présentation de l’approche, des références, de l’équipe, du planning et du budget | Exigence de réponse | L’entreprise documente une méthode de cadrage, un découpage en lots, des démonstrations, des tests, une recette et un passage en maintenance ; elle dispose de références, d’une équipe et d’une grille tarifaire. | **Partiellement couvert ou à confirmer** : les éléments nécessaires existent en partie, mais aucun planning ni budget spécifique à la consultation n’est calculé. La disponibilité après décembre 2026 manque. | Consultation : `/consultation/01_besoin.md`, § Réponse attendue ; `/consultation/02_conditions.md`, § Modalités de réponse. Entreprise : `/entreprise/06_methodes_qualite.md`, § Déroulement ; `/entreprise/03_references.md` ; `/entreprise/04_plan_charge.md` ; `/entreprise/05_tarifs.md`. |
| CMP-14 | Transmettre la réponse en français au plus tard le 30 septembre 2026 à 17 h, heure de Paris | Échéance de réponse imposée | Les documents de l’entreprise ne précisent ni préparation de la réponse ni validation de cette échéance. | **Preuve ou information non fournie** dans le corpus entreprise. Il s’agit toutefois d’une échéance de la consultation, non d’une capacité technique. | Consultation : `/consultation/02_conditions.md`, § Modalités de réponse. |
| CMP-15 | Utiliser HTTPS pour tous les échanges | Exigence obligatoire de sécurité | L’entreprise décrit des connexions chiffrées dans son architecture de référence. | **Couvert par des éléments déclaratifs**, sous réserve de la conception et de la vérification de la configuration effective. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Exigences obligatoires, point 1. Entreprise : `/entreprise/07_hebergement_securite.md`, § Contrôles internes de scénario. |
| CMP-16 | Gérer des comptes nominatifs et des droits différenciés selon les rôles | Exigence obligatoire de sécurité | L’entreprise déclare des accès nominatifs et des droits minimaux. A-R02 documente des rôles sur un extranet. | **Couvert par des éléments déclaratifs**, avec une expérience proche. Les rôles attendus par l’acheteur restent à définir. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Exigences obligatoires, point 2 ; § Informations à préciser. Entreprise : `/entreprise/07_hebergement_securite.md`, § Contrôles internes ; `/entreprise/03_references.md`, § A-R02. |
| CMP-17 | Journaliser les connexions et les principales actions d’administration | Exigence obligatoire de sécurité | L’entreprise indique une journalisation des accès administratifs. | **Partiellement couvert ou à confirmer** : les accès administratifs sont mentionnés, mais la journalisation des connexions utilisateur et le périmètre des principales actions ne sont pas explicitement détaillés. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Exigences obligatoires, point 3. Entreprise : `/entreprise/07_hebergement_securite.md`, § Contrôles internes. |
| CMP-18 | Protéger les données personnelles conformément aux obligations applicables | Exigence obligatoire de sécurité et de protection des données | L’entreprise indique que les obligations relatives aux données et aux sous-traitants doivent être examinées pour chaque dossier, sans conclure à une conformité générale. | **Preuve ou information non fournie** permettant de conclure à la conformité pour cette consultation. Il n’y a pas d’écart explicite, mais une analyse spécifique est nécessaire. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Exigences obligatoires, point 4. Entreprise : `/entreprise/07_hebergement_securite.md`, § Sauvegarde et reprise. |
| CMP-19 | Documenter l’architecture, l’authentification et les procédures de déploiement | Exigence obligatoire de sécurité | L’entreprise propose une architecture conteneurisée et liste des livrables de documentation d’installation. Elle mentionne les accès nominatifs et le MFA pour les consoles d’administration. | **Partiellement couvert ou à confirmer** : l’architecture et l’installation sont documentées au niveau général, mais la documentation complète des mécanismes d’authentification et des procédures de déploiement reste à confirmer. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Exigences obligatoires, point 5. Entreprise : `/entreprise/06_methodes_qualite.md`, § Livrables ; `/entreprise/07_hebergement_securite.md`, § Architecture et § Contrôles internes. |
| CMP-20 | Signaler à l’acheteur tout incident de sécurité identifié pendant la prestation | Exigence obligatoire de sécurité | Le corpus décrit une organisation de support et un suivi des incidents, mais ne prévoit pas explicitement la procédure de notification des incidents de sécurité à l’acheteur. | **Preuve ou information non fournie**. Une procédure et des délais de notification doivent être définis contractuellement. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Exigences obligatoires, point 6. Entreprise : `/entreprise/08_support_maintenance.md`, § Organisation ; `/entreprise/07_hebergement_securite.md`, § Sauvegarde et reprise. |
| CMP-21 | Héberger les données dans l’Union européenne | Élément souhaité | Une région France est envisagée chez un prestataire à sélectionner ; aucun contrat ni qualification de l’hébergeur n’est fourni. | **Partiellement couvert ou à confirmer** : l’option France serait compatible avec le souhait UE, mais l’hébergeur n’est pas sélectionné ni qualifié dans le corpus. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Éléments souhaités. Entreprise : `/entreprise/07_hebergement_securite.md`, § Architecture de référence proposée ; `/entreprise/09_justificatifs.md`, § État documentaire. |
| CMP-22 | Réaliser une revue de sécurité avant mise en service | Élément souhaité | L’entreprise indique que ses contrôles internes ne constituent pas un audit de sécurité indépendant. Aucun test d’intrusion indépendant n’est fourni. | **Preuve ou information non fournie** pour une revue indépendante. Les contrôles internes peuvent constituer un point de départ, mais ne démontrent pas la réalisation de la revue souhaitée. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Éléments souhaités. Entreprise : `/entreprise/06_methodes_qualite.md`, § Limites ; `/entreprise/07_hebergement_securite.md`, § Pièces absentes ; `/entreprise/09_justificatifs.md`. |
| CMP-23 | Sensibiliser l’équipe projet aux principaux risques applicatifs | Élément souhaité | Le corpus décrit des pratiques de revue de code, de tests et de contrôle, mais ne documente pas une action formalisée de sensibilisation. | **Preuve ou information non fournie**. La capacité à organiser cette sensibilisation doit être confirmée. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Éléments souhaités. Entreprise : `/entreprise/06_methodes_qualite.md`, § Déroulement et § Limites. |
| CMP-24 | Exigences de sécurité à préciser pendant le cadrage : rôles, SSO/MFA, conservation des journaux et documents, interlocuteurs incidents | Informations à préciser par l’acheteur | L’entreprise prévoit un atelier de cadrage couvrant notamment les utilisateurs, interfaces, hypothèses et critères de recette. Elle dispose d’un MFA pour les consoles d’administration, mais le SSO/MFA du portail n’est pas défini. | **Partiellement couvert ou à confirmer** : la méthode de cadrage est pertinente, mais les paramètres de sécurité dépendent des réponses de l’acheteur et d’une conception à établir. | Consultation : `/consultation/annexes/03_exigences_securite.md`, § Informations à préciser. Entreprise : `/entreprise/06_methodes_qualite.md`, § Déroulement ; `/entreprise/07_hebergement_securite.md`, § Contrôles internes. |
| CMP-25 | Préciser le nombre d’utilisateurs, les pics de connexion, l’API ERP et le volume documentaire | Informations à préciser par l’acheteur | L’entreprise dispose de références allant jusqu’à 450 et 1 200 comptes, mais aucune capacité documentée ne permet de conclure pour les volumes et pics de cette consultation. | **Preuve ou information non fournie** pour le besoin spécifique. Ces données sont nécessaires au dimensionnement, au chiffrage et au planning. | Consultation : `/consultation/01_besoin.md`, § Informations à préciser. Entreprise : `/entreprise/03_references.md`, § A-R01 et A-R02 ; `/entreprise/10_preferences.md`, § Points déclenchant une clarification. |
| CMP-26 | Préciser la disponibilité de l’équipe proposée | Information à préciser / condition de faisabilité | Le plan de charge indique, pour octobre à décembre 2026, 8 à 10 jours de chef de projet par mois, 42 à 60 jours de développeurs, 6 à 8 jours d’UX, 8 à 10 jours de QA et 4 à 6 jours de DevOps. Aucune disponibilité n’est documentée après décembre. | **Partiellement couvert ou à confirmer** : des capacités agrégées sont disponibles au début de la période, mais aucune ressource n’est réservée et la période janvier-mars 2027 n’est pas couverte. | Consultation : `/consultation/01_besoin.md`, § Informations à préciser ; `/consultation/02_conditions.md`, § Modalités de réponse. Entreprise : `/entreprise/04_plan_charge.md`, tableau et § Décision d’affectation. |
| CMP-27 | Fournir une estimation argumentée du planning jusqu’à la mise en service | Exigence de réponse | La méthode prévoit cadrage, lots, démonstrations, tests, recette et livraison, mais le dossier ne contient pas de durée estimée par phase ni de planning jusqu’en mars 2027. | **Preuve ou information non fournie**. Le planning doit être construit après clarification du périmètre, des volumes et de la capacité disponible. | Consultation : `/consultation/01_besoin.md`, § Réponse attendue ; `/consultation/02_conditions.md`, § Modalités de réponse. Entreprise : `/entreprise/06_methodes_qualite.md`, § Déroulement ; `/entreprise/04_plan_charge.md`, § Décision d’affectation. |
| CMP-28 | Les modalités de contractualisation, facturation et recette seront précisées après sélection | Information de procédure | L’entreprise travaille au forfait après cadrage et sous enveloppe de jours pour la maintenance ; le temps de pilotage et de recette doit être valorisé. | **Partiellement couvert ou à confirmer** : les modalités commerciales sont compatibles en principe, mais les conditions précises de contractualisation, de facturation et de recette restent à négocier ou préciser. | Consultation : `/consultation/02_conditions.md`, § Informations à préciser par l’acheteur. Entreprise : `/entreprise/05_tarifs.md`, § Modalités commerciales ; `/entreprise/06_methodes_qualite.md`, § Déroulement. |

## Points favorables documentés

- **Adéquation technologique déclarée** : Symfony, Vue.js, PHP, PostgreSQL, API REST et Docker sont mentionnés comme technologies principales de l’entreprise (`/entreprise/01_presentation.md`, § Activité).
- **Référence très proche du besoin** : A-R01 concerne un portail de suivi des commandes, avec comptes clients et connexion à un ERP, pour 450 comptes (`/entreprise/03_references.md`, § A-R01).
- **Complémentarité des compétences** : chef de projet, développement, UX, QA et DevOps sont présents dans l’organisation documentée (`/entreprise/02_equipe_competences.md`).
- **Processus de réalisation structuré** : cadrage, découpage en lots, démonstrations, revue de code, tests, recette, documentation et transfert sont prévus (`/entreprise/06_methodes_qualite.md`, § Déroulement et § Livrables).
- **Support aligné sur les horaires demandés** : couverture annoncée du lundi au vendredi, 9 h–18 h, heure de Paris (`/entreprise/08_support_maintenance.md`, § Couverture).
- **Possibilité d’ateliers à Lyon** : entreprise implantée à Lyon et ateliers ponctuels sur site annoncés (`/entreprise/01_presentation.md`, § Clients et mode d’intervention).
- **Contrôles de sécurité pertinents documentés** : connexions chiffrées, accès nominatifs, droits minimaux, MFA pour consoles d’administration, secrets hors dépôt et journalisation des accès administratifs (`/entreprise/07_hebergement_securite.md`, § Contrôles internes).
- **Livraison du code source prévue** dans les livrables déclarés (`/entreprise/06_methodes_qualite.md`, § Livrables).

## Risques, écarts et validations nécessaires

### Écarts explicites

Aucun écart explicite n’est documenté par rapport aux exigences obligatoires de la consultation.

Cela ne signifie pas que toutes les exigences sont démontrées. Plusieurs points restent non prouvés ou dépendent de validations.

### Preuves ou informations manquantes

- Aucun planning documenté ne couvre janvier à mars 2027 ; le plan de charge ne fournit des données que jusqu’à décembre 2026 (`/entreprise/04_plan_charge.md`).
- Aucune estimation spécifique ne démontre le respect du plafond de **160 000 EUR HT** pour le développement initial (`/entreprise/05_tarifs.md`).
- Les prix d’hébergement ne sont pas fournis ; un devis doit être obtenu (`/entreprise/05_tarifs.md`).
- Le prix de maintenance spécifique à cette consultation n’est pas chiffré.
- Les références sont uniquement déclaratives ; aucune attestation client ni procès-verbal de recette indépendant n’est fourni (`/entreprise/03_references.md`, `/entreprise/09_justificatifs.md`).
- La conformité spécifique en matière de protection des données n’est pas démontrée (`/entreprise/07_hebergement_securite.md`).
- La procédure de notification des incidents de sécurité à l’acheteur n’est pas documentée.
- La revue de sécurité indépendante avant mise en service n’est pas fournie.
- La qualification de l’hébergeur et la preuve d’un hébergement effectivement situé dans l’Union européenne ne sont pas fournies.
- Les besoins de capacité — utilisateurs, pics de connexion et volume documentaire — ne sont pas connus.
- L’API de l’ERP, ses contraintes et ses mécanismes d’authentification ne sont pas documentés.
- La disponibilité de l’équipe après décembre 2026 n’est pas documentée.

### Validations humaines nécessaires

- Faire valider par la production les personnes pouvant être effectivement affectées et leurs compétences précises.
- Établir un plan de charge complet jusqu’à mars 2027.
- Construire un chiffrage par rôle, avec hypothèses, réserve de risques et distinction entre développement initial, hébergement, licences, déplacements et maintenance.
- Vérifier la compatibilité de l’offre avec le plafond de 160 000 EUR HT.
- Définir les engagements de support, notamment les jours fériés, les niveaux de service et les délais de résolution.
- Définir les responsabilités relatives à la protection des données, aux sous-traitants et à l’hébergement.
- Formaliser la procédure de notification et de traitement des incidents de sécurité.
- Déterminer si une revue de sécurité indépendante et une sensibilisation applicative peuvent être réalisées, en interne ou avec un intervenant externe.
- Vérifier les justificatifs administratifs, l’assurance professionnelle et la qualification de l’hébergeur si ces pièces sont requises.

## Questions à poser

### Questions destinées à l’acheteur

Ces questions sont des suggestions d’analyse et ne constituent pas de nouvelles exigences client :

1. Quel est le nombre cible d’utilisateurs, et quels sont les pics de connexions attendus ?
2. Quelle est la technologie de l’ERP, sa version et la documentation disponible pour l’API REST ?
3. Quels mécanismes d’authentification l’API ERP impose-t-elle ?
4. Le portail doit-il prendre en charge un SSO ou une MFA pour les utilisateurs finaux, en plus des administrateurs ?
5. Quels rôles utilisateurs sont attendus et quelles permissions doivent être associées à chacun ?
6. Quelle est la durée de conservation des journaux de connexion et d’administration ?
7. Quelles sont les règles de conservation, d’archivage et de suppression des documents ?
8. Quel volume de documents est attendu, avec quelles tailles maximales et quelles contraintes de recherche ou de téléchargement ?
9. Le support demandé couvre-t-il les jours fériés français ?
10. Quel niveau de détail est attendu pour la revue de sécurité avant mise en service : contrôle interne, audit indépendant, test d’intrusion ou autre ?
11. Quelles sont les modalités et délais attendus pour la notification des incidents de sécurité ?
12. Quelles sont les modalités de recette, de facturation et de contractualisation envisagées ?

### Validations à demander à l’entreprise

1. Confirmer l’identité et la disponibilité du chef de projet, des développeurs, de l’UX, du QA et du DevOps jusqu’à mars 2027.
2. Produire un planning prévisionnel détaillé couvrant le cadrage, le développement, les tests, la recette et la mise en service.
3. Produire un chiffrage spécifique inférieur ou égal au plafond de 160 000 EUR HT pour le développement initial, avec hypothèses explicites.
4. Fournir un chiffrage séparé de l’hébergement et de la maintenance.
5. Confirmer la portée exacte de l’expérience ERP de la référence A-R01 et les technologies d’authentification employées.
6. Décrire précisément la journalisation prévue pour les utilisateurs et les administrateurs.
7. Décrire la procédure de notification des incidents de sécurité.
8. Confirmer les mesures de protection des données personnelles et la répartition des responsabilités avec l’hébergeur.
9. Identifier l’hébergeur envisagé, sa localisation effective des données et les justificatifs disponibles.
10. Confirmer la possibilité de réaliser une revue de sécurité avant mise en service et, si nécessaire, une sensibilisation de l’équipe projet.
11. Indiquer si des attestations clients, procès-verbaux de recette ou autres preuves indépendantes peuvent être obtenus pour les références.
12. Vérifier les pièces administratives et d’assurance nécessaires avant contractualisation.

Cette comparaison met en évidence plusieurs correspondances documentées, mais aussi des éléments importants à confirmer. Elle ne constitue pas une décision de répondre ou de ne pas répondre à la consultation.