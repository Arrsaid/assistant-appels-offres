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

Les documents indiquent qu’il s’agit de données synthétiques et fictives : l’acheteur, l’entreprise, les clients et les références ne sont pas réels.

## Matrice de comparaison

| Identifiant | Exigence | Nature | Élément entreprise | Constat | Sources |
|---|---|---|---|---|---|
| CMP-01 | Créer un portail permettant la consultation des commandes, le téléchargement de documents et la gestion des accès collaborateurs | Obligatoire — besoin fonctionnel | L’entreprise se positionne sur les portails clients et applications métier. La référence A-R01 couvre les comptes clients, le suivi de commandes et une connexion à un ERP. A-R02 couvre les documents privés et les rôles | **Couvert par des éléments déclaratifs**, avec une couverture fonctionnelle répartie entre deux références. Le périmètre exact du futur portail reste à cadrer | Consultation `/consultation/01_besoin.md`, sections « Besoin » et « Exigences obligatoires » ; entreprise `/entreprise/01_presentation.md`, « Activité » ; `/entreprise/03_references.md`, A-R01 et A-R02 |
| CMP-02 | Échange de données avec l’ERP existant via une API REST | Obligatoire — architecture/intégration | Les compétences déclarées incluent les API REST. A-R01 mentionne une connexion à un ERP. L’entreprise indique également Symfony, PHP, Vue.js et PostgreSQL | **Couvert par des éléments déclaratifs**. La compatibilité avec l’ERP réel ne peut pas être confirmée avant réception de sa documentation et analyse de ses contraintes | Consultation `/consultation/01_besoin.md`, « Besoin » et « Informations à préciser » ; entreprise `/entreprise/02_equipe_competences.md`, « Compétences et preuves » ; `/entreprise/03_references.md`, A-R01 |
| CMP-03 | Développement avec Symfony et Vue.js | Obligatoire — technologie | Ces technologies sont citées comme technologies principales. Elles apparaissent également dans les références A-R01 et A-R02 | **Couvert par des éléments déclaratifs**. La maîtrise est documentée au niveau de projets et de l’équipe, sans preuve indépendante fournie | Consultation `/consultation/01_besoin.md`, « Exigences obligatoires » ; entreprise `/entreprise/01_presentation.md`, « Activité » ; `/entreprise/02_equipe_competences.md`, « Compétences et preuves » ; `/entreprise/03_references.md`, A-R01 et A-R02 |
| CMP-04 | Présenter au moins une référence comparable de portail clients | Obligatoire — expérience | A-R01 est un portail de suivi des commandes avec comptes clients, 450 comptes et connexion à un ERP. A-R02 est un extranet avec documents privés et rôles, pour 1 200 comptes | **Couvert par des éléments déclaratifs**. La comparabilité est documentée, mais aucune attestation client, aucun procès-verbal de recette ni preuve tierce n’est fourni | Consultation `/consultation/01_besoin.md`, « Exigences obligatoires » ; entreprise `/entreprise/03_references.md`, A-R01 et A-R02 ; `/entreprise/09_justificatifs.md`, « Références de projets » |
| CMP-05 | Identifier un chef de projet et les compétences mobilisées | Obligatoire — organisation | Un chef de projet figure dans l’effectif. Ses missions déclarées couvrent ateliers, cadrage et recette. Sont aussi documentés des profils développeur, QA, UX et DevOps | **Couvert par des éléments déclaratifs**. Les personnes effectivement affectées et leur disponibilité doivent être validées par la production | Consultation `/consultation/01_besoin.md`, « Exigences obligatoires » et « Réponse attendue » ; entreprise `/entreprise/02_equipe_competences.md`, « Répartition » et « Profils individuels » ; `/entreprise/04_plan_charge.md`, « Décision d’affectation » |
| CMP-06 | Assurer un support du lundi au vendredi, de 9 h à 18 h, heure de Paris | Obligatoire — support | L’entreprise prévoit cette couverture, hors jours fériés français. Elle ne prévoit pas de couverture de nuit, de week-end ni d’astreinte 24 h/24 | **Couvert par des éléments déclaratifs**, sous réserve que l’exclusion des jours fériés soit compatible avec l’interprétation de l’acheteur. Aucun support 24 h/24 n’est requis dans la consultation | Consultation `/consultation/01_besoin.md`, « Exigences obligatoires » ; entreprise `/entreprise/08_support_maintenance.md`, « Couverture » ; `/entreprise/01_presentation.md`, « Limites explicites » |
| CMP-07 | Livrer le code source et la documentation technique | Obligatoire — livrables | La méthode prévoit la livraison du code source, de la documentation d’installation, des résultats de tests et du compte rendu de recette | **Couvert par des éléments déclaratifs**. La portée exacte de la documentation technique devra être alignée avec le besoin et le contrat | Consultation `/consultation/01_besoin.md`, « Exigences obligatoires » ; entreprise `/entreprise/06_methodes_qualite.md`, « Livrables » |
| CMP-08 | Intégrer les exigences de sécurité : HTTPS, comptes nominatifs, droits par rôle, journalisation des accès/actions d’administration, protection des données personnelles, documentation et signalement des incidents | Obligatoire — sécurité et protection des données | L’entreprise documente les connexions chiffrées, les accès nominatifs, les droits minimaux, la journalisation des accès administratifs, les secrets hors dépôt et la suppression des accès au départ. Elle prévoit une documentation technique et un signalement des incidents n’est pas explicitement décrit dans les documents consultés | **Partiellement couvert ou à confirmer**. Plusieurs contrôles correspondent aux exigences, mais la journalisation des « principales actions d’administration », les modalités de protection des données personnelles et la procédure formelle de notification d’incident ne sont pas entièrement documentées | Consultation `/consultation/annexes/03_exigences_securite.md`, « Exigences obligatoires » ; entreprise `/entreprise/07_hebergement_securite.md`, « Contrôles internes » ; `/entreprise/06_methodes_qualite.md`, « Livrables » |
| CMP-09 | Documenter l’architecture technique, l’authentification et les procédures de déploiement | Obligatoire — documentation/sécurité | Une architecture de référence conteneurisée est décrite, avec PostgreSQL et séparation des environnements. Les contrôles d’authentification et les livraisons sont mentionnés. La méthode prévoit une documentation d’installation | **Partiellement couvert ou à confirmer** : des éléments existent, mais il faut confirmer que la documentation livrée couvrira précisément l’architecture, les mécanismes d’authentification et les procédures de déploiement demandés | Consultation `/consultation/annexes/03_exigences_securite.md`, point 5 ; entreprise `/entreprise/06_methodes_qualite.md`, « Livrables » ; `/entreprise/07_hebergement_securite.md`, « Architecture » et « Contrôles internes » |
| CMP-10 | Héberger les données dans l’Union européenne | Souhaité — hébergement | Une région France est envisagée chez un prestataire à sélectionner. Aucun contrat ni qualification d’hébergeur n’est fourni | **Partiellement couvert ou à confirmer**. L’orientation vers la France est compatible avec le souhait, mais l’hébergeur n’est pas sélectionné et la localisation n’est pas contractualisée | Consultation `/consultation/annexes/03_exigences_securite.md`, « Éléments souhaités » ; entreprise `/entreprise/07_hebergement_securite.md`, « Architecture de référence » ; `/entreprise/09_justificatifs.md`, « Qualification de l’hébergeur » |
| CMP-11 | Prévoir une revue de sécurité avant la mise en service | Souhaité — sécurité | Les contrôles internes et tests techniques sont décrits, mais l’entreprise précise qu’ils ne constituent pas un audit de sécurité indépendant. Aucun rapport de test d’intrusion indépendant n’est fourni | **Preuve ou information non fournie** concernant une revue de sécurité répondant précisément au souhait de l’acheteur. Les contrôles internes ne doivent pas être assimilés à un audit indépendant | Consultation `/consultation/annexes/03_exigences_securite.md`, « Éléments souhaités » ; entreprise `/entreprise/06_methodes_qualite.md`, « Limites » ; `/entreprise/07_hebergement_securite.md`, « Pièces absentes » |
| CMP-12 | Sensibiliser l’équipe projet aux principaux risques applicatifs | Souhaité — sécurité | Aucun dispositif explicite de sensibilisation de l’équipe projet n’est documenté | **Preuve ou information non fournie**. Il ne s’agit pas d’une absence explicitement déclarée de capacité | Consultation `/consultation/annexes/03_exigences_securite.md`, « Éléments souhaités » ; absence d’élément correspondant dans les documents d’entreprise consultés |
| CMP-13 | Organiser ponctuellement des ateliers à Lyon | Souhaité — organisation | L’entreprise est implantée à Lyon et indique réaliser des ateliers ponctuels sur site, avec déplacements en France métropolitaine | **Couvert par des éléments déclaratifs** | Consultation `/consultation/01_besoin.md`, « Éléments souhaités » ; entreprise `/entreprise/01_presentation.md`, « Clients et mode d’intervention » ; `/entreprise/10_preferences.md`, « Cibles » |
| CMP-14 | Respecter le budget maximal de 160 000 EUR HT pour le développement initial | Obligatoire — contrainte financière | La fourchette commerciale déclarée est de 60 000 à 220 000 EUR HT. Les tarifs journaliers sont documentés, mais le périmètre et la charge détaillée de la consultation ne permettent pas de calculer une offre ferme | **Partiellement couvert ou à confirmer**. Le plafond est compatible avec la fourchette basse et intermédiaire de l’entreprise, mais la borne haute dépasse le budget client. Aucun chiffrage spécifique n’est fourni | Consultation `/consultation/01_besoin.md`, « Budget » ; `/consultation/02_conditions.md`, « Conditions financières » ; entreprise `/entreprise/01_presentation.md`, « Positionnement commercial » ; `/entreprise/05_tarifs.md`, « Grille » et « Construction d’une estimation » |
| CMP-15 | Chiffrer séparément l’hébergement et la maintenance | Obligatoire — réponse financière | La maintenance est proposée en complément. L’entreprise indique que les prix d’hébergement ne sont pas fournis et qu’un devis doit être obtenu | **Partiellement couvert ou à confirmer**. La séparation est prévue, mais les montants d’hébergement ne sont pas disponibles dans le corpus et la maintenance n’est pas chiffrée pour ce projet | Consultation `/consultation/01_besoin.md`, « Budget et calendrier » ; `/consultation/02_conditions.md`, « Modalités de réponse » et « Conditions financières » ; entreprise `/entreprise/05_tarifs.md`, « Construction d’une estimation » ; `/entreprise/10_preferences.md`, « Points déclenchant une clarification » |
| CMP-16 | Démarrage souhaité en octobre 2026 et mise en service visée en mars 2027 | Souhait de calendrier / objectif client | Le plan de charge fournit des disponibilités pour octobre, novembre et décembre 2026 uniquement. Aucun capacitaire n’est documenté après décembre. La méthode prévoit un cadrage, des lots, des démonstrations bimensuelles, une recette et une mise en maintenance | **Partiellement couvert ou à confirmer**. La capacité disponible après décembre 2026 n’est pas documentée ; il est donc impossible de confirmer la faisabilité jusqu’à mars 2027 à partir du corpus | Consultation `/consultation/01_besoin.md`, « Budget et calendrier » ; `/consultation/02_conditions.md`, « Calendrier » ; entreprise `/entreprise/04_plan_charge.md`, tableau de capacité et « Décision d’affectation » ; `/entreprise/06_methodes_qualite.md`, « Déroulement » |
| CMP-17 | Transmettre la réponse avant le 30 septembre 2026 à 17 h, heure de Paris | Obligatoire — délai de soumission | Les documents de l’entreprise ne présentent pas d’engagement ni de confirmation de disponibilité pour préparer cette réponse | **Preuve ou information non fournie** sur la capacité de l’entreprise à respecter cette échéance. Il s’agit d’une validation organisationnelle, non d’un écart établi | Consultation `/consultation/02_conditions.md`, « Modalités de réponse » ; aucun élément correspondant explicite dans le corpus entreprise |
| CMP-18 | Réponse en français avec présentation de l’approche, références, équipe/disponibilité, planning, budget et chiffrage séparé de l’hébergement/maintenance | Obligatoire — contenu de la réponse | Les documents fournissent des éléments sur l’approche, les références, l’équipe, les tarifs, le plan de charge et la séparation des postes ; certains éléments restent à produire pour cette consultation | **Partiellement couvert ou à confirmer**. Le corpus permet de préparer la réponse, mais ne constitue pas lui-même une réponse finalisée et ne confirme pas la disponibilité après décembre 2026 | Consultation `/consultation/02_conditions.md`, « Modalités de réponse » ; entreprise `/entreprise/04_plan_charge.md`, `/entreprise/05_tarifs.md`, `/entreprise/06_methodes_qualite.md`, `/entreprise/03_references.md` |
| CMP-19 | Préciser pendant le cadrage les rôles utilisateurs, l’authentification éventuelle SSO/MFA, la conservation des journaux et documents, ainsi que les interlocuteurs incidents | Information à préciser par l’acheteur | L’entreprise documente le MFA pour les consoles d’administration, les journaux et les sauvegardes, mais pas les paramètres propres au projet. Elle indique que les obligations relatives aux données doivent être examinées au cas par cas | **À confirmer avec l’acheteur et l’équipe projet**. Les paramètres fonctionnels et de conservation ne sont pas encore définis dans la consultation | Consultation `/consultation/annexes/03_exigences_securite.md`, « Informations à préciser » ; `/consultation/01_besoin.md`, « Informations à préciser » ; entreprise `/entreprise/07_hebergement_securite.md`, « Contrôles internes » et « Sauvegarde et reprise » |
| CMP-20 | Préciser le nombre d’utilisateurs, les pics de connexion, les contraintes de l’API ERP et le volume de documents | Information à préciser par l’acheteur | A-R01 documente 450 comptes et A-R02 1 200 comptes, mais ces chiffres concernent d’autres projets. Aucun volume cible, pic de connexion ou documentation de l’API actuelle n’est fourni | **Preuve ou information non fournie** pour le projet objet de la consultation. Les références ne permettent pas de transposer automatiquement les volumes | Consultation `/consultation/01_besoin.md`, « Informations à préciser » ; entreprise `/entreprise/03_references.md`, A-R01 et A-R02 |

## Points favorables documentés

- **Adéquation technologique déclarée** : Symfony, Vue.js, PHP, PostgreSQL, API REST et Docker sont cités dans l’activité et les compétences de l’entreprise (`/entreprise/01_presentation.md`, `/entreprise/02_equipe_competences.md`).
- **Référence particulièrement proche** : A-R01 combine un portail de suivi des commandes, des comptes clients et une connexion à un ERP (`/entreprise/03_references.md`, A-R01).
- **Couverture complémentaire des fonctions documentaires et des rôles** : A-R02 mentionne des documents privés et des rôles (`/entreprise/03_references.md`, A-R02).
- **Organisation projet documentée** : chef de projet, développeurs, UX, QA et DevOps sont identifiés, avec une méthode incluant cadrage, lots, tests, recette, documentation et transfert (`/entreprise/02_equipe_competences.md`, `/entreprise/06_methodes_qualite.md`).
- **Support compatible sur les horaires principaux** : couverture déclarée du lundi au vendredi, de 9 h à 18 h, heure de Paris (`/entreprise/08_support_maintenance.md`).
- **Capacités de sécurité correspondant à plusieurs exigences** : HTTPS/connexions chiffrées, accès nominatifs, droits minimaux, MFA pour les consoles d’administration, journalisation des accès administratifs et gestion des secrets sont documentés (`/entreprise/07_hebergement_securite.md`).
- **Ateliers à Lyon** : implantation à Lyon et ateliers ponctuels sur site déclarés (`/entreprise/01_presentation.md`).
- **Positionnement budgétaire potentiellement compatible**, mais non confirmé : le développement initial est annoncé entre 60 000 et 220 000 EUR HT, tandis que le budget client est plafonné à 160 000 EUR HT (`/entreprise/01_presentation.md`, `/consultation/02_conditions.md`).

## Risques, écarts et validations nécessaires

### Écarts explicites

Aucun écart explicite n’est identifié sur une exigence obligatoire de la consultation.

En revanche, l’entreprise indique explicitement :
- ne pas fournir d’audit externe d’accessibilité ;
- ne pas détenir de certification ISO 27001 ;
- ne pas disposer d’une astreinte 24 h/24 (`/entreprise/01_presentation.md`, `/entreprise/02_equipe_competences.md`).

Ces éléments ne correspondent pas à des exigences obligatoires identifiées dans la consultation. La revue de sécurité est seulement souhaitée ; elle n’est donc pas assimilée à un écart éliminatoire.

### Preuves ou informations manquantes

- Preuves indépendantes des références : aucune attestation client ni procès-verbal de recette n’est fourni (`/entreprise/03_references.md`, `/entreprise/09_justificatifs.md`).
- Disponibilité de l’équipe après décembre 2026 : le plan de charge ne couvre pas janvier à mars 2027 (`/entreprise/04_plan_charge.md`).
- Chiffrage de l’hébergement : les prix ne sont pas fournis et un devis reste à obtenir (`/entreprise/05_tarifs.md`).
- Chiffrage détaillé de la maintenance pour ce projet.
- Confirmation d’un budget de développement inférieur ou égal à 160 000 EUR HT.
- Procédure formelle de signalement des incidents de sécurité.
- Périmètre exact de la journalisation des actions d’administration.
- Modalités précises de protection des données personnelles.
- Revue de sécurité avant mise en service et éventuelle intervention d’un tiers.
- Sensibilisation de l’équipe projet aux risques applicatifs.
- Qualification ou contrat de l’hébergeur, notamment pour confirmer la localisation en France ou dans l’Union européenne (`/entreprise/07_hebergement_securite.md`, `/entreprise/09_justificatifs.md`).
- Pièces administratives et assurances : aucun justificatif d’assurance professionnelle, d’immatriculation ou d’attestations sociales et fiscales n’est fourni (`/entreprise/09_justificatifs.md`).

### Validations humaines nécessaires

- Faire valider par la production les personnes mobilisables, leurs dates et leurs compétences précises ; aucune ressource n’est réservée par la présente analyse (`/entreprise/04_plan_charge.md`).
- Construire un planning argumenté jusqu’à mars 2027 après clarification des capacités de janvier à mars.
- Vérifier que la charge et le prix restent dans le plafond de 160 000 EUR HT, hors hébergement et maintenance.
- Définir avec l’acheteur le périmètre de l’API ERP, les utilisateurs, les pics de connexion et le volume de documents.
- Valider les exigences de sécurité et de protection des données applicables au projet.
- Déterminer l’hébergeur, sa localisation, ses garanties et les coûts associés.
- Confirmer la couverture du support les jours fériés et les modalités attendues pour la prise en charge des incidents.
- Préparer les pièces administratives ou contractuelles éventuellement demandées après sélection.

## Questions à poser

### Questions destinées à l’acheteur

Ces questions sont des suggestions issues des informations manquantes identifiées ; elles ne constituent pas de nouvelles exigences client :

1. Quels sont le nombre d’utilisateurs prévisionnel, les profils de rôles et les pics de connexion attendus ?
2. Quelle est la documentation disponible de l’API REST de l’ERP, et quelles sont ses contraintes d’authentification, de débit, de disponibilité et de gestion des erreurs ?
3. Quels volumes de documents doivent être stockés, pendant quelles durées et avec quelles règles de suppression ?
4. Le support doit-il inclure les jours fériés français, ou la couverture annoncée du lundi au vendredi hors jours fériés est-elle acceptable ?
5. Quel niveau de journalisation est attendu pour les connexions et les actions d’administration, et quelle doit être la durée de conservation des journaux ?
6. Un SSO ou une MFA pour les utilisateurs finaux est-il requis, au-delà de la MFA prévue pour les consoles d’administration ?
7. Quelle procédure et quels interlocuteurs doivent être prévus pour le signalement d’un incident de sécurité ?
8. Une revue de sécurité indépendante est-elle attendue, et selon quel périmètre ou référentiel ?
9. L’hébergement dans un pays précis de l’Union européenne est-il requis, ou un hébergement en France est-il seulement préféré ?
10. Quelles sont les modalités de contractualisation, de facturation et de recette qui seront précisées après sélection ?
11. Le budget de 160 000 EUR HT inclut-il des réserves de risques ou uniquement les charges de réalisation prévues ?

### Validations à demander à l’entreprise

1. La production peut-elle confirmer les personnes affectables et leur disponibilité de janvier à mars 2027 ?
2. Quelle charge prévisionnelle par rôle permettrait de rester sous 160 000 EUR HT de développement initial ?
3. L’entreprise peut-elle fournir une estimation séparée de la maintenance et obtenir le coût d’hébergement auprès d’un prestataire identifié ?
4. Quelle procédure documentée de notification des incidents de sécurité peut-elle proposer ?
5. Quels journaux d’actions d’administration sont effectivement produits et conservés ?
6. Comment la protection des données personnelles serait-elle organisée pour ce projet précis ?
7. L’entreprise peut-elle proposer ou organiser une revue de sécurité avant mise en service ?
8. Peut-elle prévoir une sensibilisation de l’équipe projet aux risques applicatifs ?
9. Les références A-R01 et A-R02 peuvent-elles être appuyées par des attestations ou autres justificatifs autorisés ?
10. Les horaires de support hors jours fériés sont-ils compatibles avec l’attente exacte de l’acheteur ?
11. Les pièces d’assurance professionnelle et autres justificatifs administratifs requis peuvent-ils être réunis ?

Cette comparaison ne prend pas de décision sur l’opportunité de répondre à la consultation.