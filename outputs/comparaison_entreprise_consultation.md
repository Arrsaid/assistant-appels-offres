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

> Les données de la consultation et de l’entreprise sont explicitement fictives et utilisées à des fins pédagogiques.

## Matrice de comparaison

| Identifiant | Exigence | Nature | Élément entreprise | Constat | Sources |
|---|---|---|---|---|---|
| CMP-01 | Développer avec Symfony et Vue.js | Obligatoire | Symfony, PHP, Vue.js sont indiqués comme technologies principales et sont documentés dans les références A-R01 et A-R02. | **Couvert par des éléments déclaratifs.** Les technologies sont bien documentées, mais aucune preuve indépendante n’est fournie. | Consultation : `/consultation/01_besoin.md` — « Exigences obligatoires » ; Entreprise : `/entreprise/01_presentation.md` — « Activité », `/entreprise/02_equipe_competences.md` — « Compétences et preuves », `/entreprise/03_references.md` — A-R01 et A-R02 |
| CMP-02 | Présenter au moins une référence comparable de portail clients | Obligatoire | A-R01 porte sur un portail de suivi des commandes avec comptes clients, suivi de commandes et connexion à un ERP ; 450 comptes. A-R02 concerne un extranet avec documents privés et rôles ; 1 200 comptes. | **Couvert par des éléments déclaratifs.** A-R01 est particulièrement comparable au besoin. Les références restent déclaratives, sans attestation client ni procès-verbal de recette. | Consultation : `/consultation/01_besoin.md` — « Exigences obligatoires » ; Entreprise : `/entreprise/03_references.md` — A-R01, A-R02 |
| CMP-03 | Identifier un chef de projet et les compétences mobilisées | Obligatoire | Un chef de projet est identifié dans l’équipe ; ses compétences portent sur les ateliers, le cadrage et la recette. Les compétences de développement, QA et DevOps sont également décrites. | **Couvert par des éléments déclaratifs**, sous réserve de confirmer les personnes effectivement affectées et leur disponibilité. | Consultation : `/consultation/01_besoin.md` ; Entreprise : `/entreprise/02_equipe_competences.md` — « Répartition », « Compétences et preuves », profils CP01, DEV01 et OPS01 |
| CMP-04 | Assurer un support du lundi au vendredi, de 9 h à 18 h, heure de Paris | Obligatoire | Le dispositif prévoit cette couverture, hors jours fériés français. Les niveaux de prise en charge P1 à P3 sont précisés. | **Couvert par des éléments déclaratifs**, avec une réserve sur le périmètre : la qualification et le début d’investigation sont couverts, mais aucun délai de résolution n’est garanti. | Consultation : `/consultation/01_besoin.md` ; Entreprise : `/entreprise/08_support_maintenance.md` — « Couverture » et « Qualification des incidents » |
| CMP-05 | Livrer le code source et la documentation technique | Obligatoire | Les livrables annoncés comprennent le code source, la documentation d’installation, les résultats de tests et le compte rendu de recette. | **Couvert par des éléments déclaratifs.** La documentation d’installation est explicitement prévue ; il faut confirmer qu’elle couvrira tout le périmètre de la documentation technique attendue. | Consultation : `/consultation/01_besoin.md` ; Entreprise : `/entreprise/06_methodes_qualite.md` — « Livrables » |
| CMP-06 | Expérience d’intégration avec un ERP | Souhaité | A-R01 mentionne la connexion à un ERP ; l’entreprise déclare utiliser les API REST. | **Couvert par des éléments déclaratifs.** L’expérience est pertinente, mais les caractéristiques de l’ERP et de son API cible ne sont pas encore connues. | Consultation : `/consultation/01_besoin.md` — « Éléments souhaités » et « Informations à préciser » ; Entreprise : `/entreprise/03_references.md` — A-R01, `/entreprise/01_presentation.md` — « Technologies principales » |
| CMP-07 | Possibilité d’organiser des ateliers ponctuels à Lyon | Souhaité | L’entreprise est implantée à Lyon et prévoit des ateliers ponctuels sur site ainsi que des déplacements en France métropolitaine. | **Couvert par des éléments déclaratifs.** Les modalités pratiques et le nombre d’ateliers restent à confirmer. | Consultation : `/consultation/01_besoin.md` — « Éléments souhaités » ; Entreprise : `/entreprise/01_presentation.md` — « Clients et mode d’intervention » et « Positionnement commercial » |
| CMP-08 | Respecter un budget maximal de 160 000 EUR HT pour le développement initial | Obligatoire / contrainte financière | La fourchette commerciale annoncée est de 60 000 à 220 000 EUR HT. Les tarifs journaliers sont fournis, mais aucune estimation de charge du projet n’est établie. | **Partiellement couvert ou à confirmer.** Le budget cible se situe dans la fourchette commerciale, mais cette fourchette ne démontre pas que le projet sera réalisable sous 160 000 EUR HT. Le chiffrage doit exclure l’hébergement et la maintenance, qui sont séparés. | Consultation : `/consultation/01_besoin.md` — « Budget et calendrier », `/consultation/02_conditions.md` — « Conditions financières » ; Entreprise : `/entreprise/01_presentation.md` — « Positionnement commercial », `/entreprise/05_tarifs.md` |
| CMP-09 | Chiffrer séparément l’hébergement et la maintenance | Obligatoire dans la réponse | La maintenance est proposée en complément. Les prix d’hébergement et d’audit externe ne sont pas fournis et doivent faire l’objet d’un devis. Le support et la maintenance sont décrits opérationnellement. | **Partiellement couvert ou à confirmer.** Le principe de séparation est compatible, mais aucun montant d’hébergement n’est documenté. | Consultation : `/consultation/01_besoin.md`, `/consultation/02_conditions.md` ; Entreprise : `/entreprise/05_tarifs.md` — « Construction d’une estimation », `/entreprise/08_support_maintenance.md` |
| CMP-10 | Démarrage souhaité en octobre 2026 et mise en service visée en mars 2027 | Calendrier souhaité / objectif client | Le plan de charge fournit des disponibilités uniquement pour octobre, novembre et décembre 2026 : chef de projet 8/10/10 jours, développeurs 42/54/60, UX 6/8/8, QA 8/10/10, DevOps 4/6/6. Aucune disponibilité n’est fournie après décembre 2026. | **Partiellement couvert ou à confirmer.** Le démarrage en octobre est envisageable au regard des capacités agrégées, mais aucune disponibilité ni estimation de planning n’est documentée pour janvier à mars 2027. Aucune ressource n’est réservée. | Consultation : `/consultation/01_besoin.md` — « Budget et calendrier », `/consultation/02_conditions.md` — « Calendrier » ; Entreprise : `/entreprise/04_plan_charge.md` |
| CMP-11 | Fournir l’équipe envisagée et sa disponibilité dans la réponse | Obligatoire dans la réponse | Les fonctions et profils sont décrits, mais les capacités sont agrégées par métier. Le document précise que les personnes, dates et compétences doivent être validées par la production. | **Partiellement couvert ou à confirmer.** Une équipe-type est documentée, mais la disponibilité nominative et l’affectation effective ne le sont pas. | Consultation : `/consultation/01_besoin.md`, `/consultation/02_conditions.md` ; Entreprise : `/entreprise/02_equipe_competences.md`, `/entreprise/04_plan_charge.md` |
| CMP-12 | Transmettre la réponse en français avant le 30 septembre 2026 à 17 h, heure de Paris | Obligatoire, échéance de remise | Les documents de l’entreprise sont rédigés en français, mais ils ne documentent ni préparation ni validation d’une réponse à cette échéance. | **Preuve ou information non fournie** concernant l’organisation interne de remise. L’échéance client est toutefois clairement fixée. | Consultation : `/consultation/02_conditions.md` — « Modalités de réponse » ; Entreprise : aucun élément spécifique dans les documents consultés |
| CMP-13 | Utiliser HTTPS pour tous les échanges | Obligatoire sécurité | Les contrôles internes mentionnent les connexions chiffrées. | **Couvert par des éléments déclaratifs**, sans configuration détaillée ni preuve technique indépendante. | Consultation : `/consultation/annexes/03_exigences_securite.md` — exigence 1 ; Entreprise : `/entreprise/07_hebergement_securite.md` — « Contrôles internes de scénario » |
| CMP-14 | Gérer des comptes nominatifs et des droits différenciés selon les rôles | Obligatoire sécurité | L’entreprise documente des accès nominatifs et des droits minimaux. A-R02 mentionne des rôles dans un extranet. | **Couvert par des éléments déclaratifs.** Le détail des rôles attendus par l’acheteur reste à définir pendant le cadrage. | Consultation : `/consultation/annexes/03_exigences_securite.md` — exigence 2 et « Informations à préciser » ; Entreprise : `/entreprise/07_hebergement_securite.md`, `/entreprise/03_references.md` — A-R02 |
| CMP-15 | Journaliser les connexions et les principales actions d’administration | Obligatoire sécurité | La journalisation des accès administratifs est prévue. | **Partiellement couvert ou à confirmer.** La source mentionne les accès administratifs, mais ne confirme pas expressément la journalisation de toutes les connexions ni le périmètre exact des actions d’administration. | Consultation : `/consultation/annexes/03_exigences_securite.md` — exigence 3 ; Entreprise : `/entreprise/07_hebergement_securite.md` — « Contrôles internes de scénario » |
| CMP-16 | Protéger les données personnelles conformément aux obligations applicables | Obligatoire sécurité / protection des données | L’entreprise indique que les obligations relatives aux données et aux sous-traitants doivent être examinées pour chaque dossier. Aucun constat général de conformité n’est fourni. | **Preuve ou information non fournie.** Il ne faut pas conclure à une conformité générale à partir du dossier. | Consultation : `/consultation/annexes/03_exigences_securite.md` — exigence 4 ; Entreprise : `/entreprise/07_hebergement_securite.md` — « Sauvegarde et reprise » |
| CMP-17 | Documenter l’architecture, l’authentification et les procédures de déploiement | Obligatoire sécurité | Une architecture de référence est décrite : application conteneurisée, PostgreSQL et environnements séparés. Les accès nominatifs et la MFA pour les consoles d’administration sont mentionnés. Les méthodes annoncent une documentation d’installation et un passage en maintenance. | **Partiellement couvert ou à confirmer.** Les éléments existent au niveau de principes et d’une architecture de référence, mais la documentation complète à livrer n’est pas encore produite et la MFA ne concerne explicitement que les consoles d’administration. | Consultation : `/consultation/annexes/03_exigences_securite.md` — exigence 5 ; Entreprise : `/entreprise/07_hebergement_securite.md`, `/entreprise/06_methodes_qualite.md` |
| CMP-18 | Signaler à l’acheteur tout incident de sécurité identifié pendant la prestation | Obligatoire sécurité | Le processus de support prévoit qualification, affectation et communication au client, mais ne décrit pas spécifiquement la notification d’incidents de sécurité ni ses délais. | **Preuve ou information non fournie.** Un processus dédié d’incident de sécurité doit être confirmé. | Consultation : `/consultation/annexes/03_exigences_securite.md` — exigence 6 ; Entreprise : `/entreprise/08_support_maintenance.md` — « Organisation » |
| CMP-19 | Héberger de préférence les données dans l’Union européenne | Souhaité | Une région France est envisagée chez un prestataire à sélectionner. Aucun contrat ni qualification d’hébergeur n’est fourni. | **Partiellement couvert ou à confirmer.** La France se situe dans l’Union européenne, mais l’hébergement n’est qu’une hypothèse et n’est pas engagé. | Consultation : `/consultation/annexes/03_exigences_securite.md` — « Éléments souhaités » ; Entreprise : `/entreprise/07_hebergement_securite.md` — « Architecture de référence proposée », `/entreprise/09_justificatifs.md` |
| CMP-20 | Réaliser une revue de sécurité avant mise en service | Souhaité | Les contrôles internes sont décrits, mais aucun audit ou rapport de sécurité indépendant n’est fourni. Les tarifs indiquent que le prix d’un audit externe est à obtenir. | **Partiellement couvert ou à confirmer.** Une revue peut être envisagée, mais son contenu, son indépendance et son coût ne sont pas documentés. | Consultation : `/consultation/annexes/03_exigences_securite.md` — « Éléments souhaités » ; Entreprise : `/entreprise/06_methodes_qualite.md` — « Limites », `/entreprise/05_tarifs.md`, `/entreprise/07_hebergement_securite.md` |
| CMP-21 | Sensibiliser l’équipe projet aux principaux risques applicatifs | Souhaité | Les documents décrivent des revues de code et des tests, mais ne mentionnent pas de dispositif de sensibilisation de l’équipe aux risques applicatifs. | **Preuve ou information non fournie.** Les pratiques qualité ne suffisent pas à démontrer une sensibilisation formalisée. | Consultation : `/consultation/annexes/03_exigences_securite.md` — « Éléments souhaités » ; Entreprise : `/entreprise/06_methodes_qualite.md`, `/entreprise/07_hebergement_securite.md` |
| CMP-22 | Fournir une estimation argumentée du planning et du budget | Obligatoire dans la réponse | Une méthode de chiffrage par rôle est fournie, avec tarifs journaliers, mais aucune charge cible ni planning projet détaillé n’est établi. | **Partiellement couvert ou à confirmer.** La base de calcul existe ; il manque l’estimation du périmètre de cette consultation et la démonstration de sa compatibilité avec mars 2027. | Consultation : `/consultation/01_besoin.md` — « Réponse attendue », `/consultation/02_conditions.md` ; Entreprise : `/entreprise/05_tarifs.md`, `/entreprise/04_plan_charge.md` |
| CMP-23 | Répondre en français | Obligatoire de forme | Les documents fournis par l’entreprise sont en français. | **Couvert par des éléments documentaires**, sans preuve d’une réponse finale effectivement préparée. | Consultation : `/consultation/02_conditions.md` — « Modalités de réponse » ; documents de l’entreprise consultés |
| CMP-24 | Tenir compte des informations encore à préciser : utilisateurs, pics, API ERP, volumes documentaires, rôles, SSO/MFA, conservation et interlocuteurs incident | Données de cadrage à obtenir | L’entreprise identifie elle-même comme déclencheurs de clarification le volume d’utilisateurs ou de données, le prix d’hébergement manquant et les contraintes du dossier. | **Partiellement couvert ou à confirmer.** Les documents reconnaissent plusieurs dépendances, mais ne fournissent pas les données client manquantes et ne permettent pas de chiffrer précisément le projet. | Consultation : `/consultation/01_besoin.md`, `/consultation/annexes/03_exigences_securite.md` ; Entreprise : `/entreprise/10_preferences.md` — « Points déclenchant une clarification », `/entreprise/07_hebergement_securite.md` |

## Points favorables documentés

- **Adéquation technologique** : Symfony, Vue.js, PHP, PostgreSQL et API REST sont documentés comme technologies utilisées par l’entreprise (`/entreprise/01_presentation.md`, `/entreprise/02_equipe_competences.md`).
- **Référence très proche du besoin** : A-R01 couvre un portail de suivi des commandes, des comptes clients et une connexion à un ERP (`/entreprise/03_references.md`).
- **Références complémentaires pertinentes** : A-R02 documente des documents privés et des rôles, éléments proches de la gestion des documents et des accès collaborateurs.
- **Présence d’un chef de projet et de fonctions QA/DevOps** : les rôles, activités et compétences sont décrits (`/entreprise/02_equipe_competences.md`).
- **Support aligné sur les horaires demandés** : couverture du lundi au vendredi, 9 h–18 h, heure de Paris, hors jours fériés (`/entreprise/08_support_maintenance.md`).
- **Livraison du code et d’éléments documentaires prévue** : code source, documentation d’installation, résultats de tests et compte rendu de recette (`/entreprise/06_methodes_qualite.md`).
- **Capacité à organiser des ateliers à Lyon** : l’entreprise est implantée à Lyon et prévoit des interventions ponctuelles sur site (`/entreprise/01_presentation.md`).
- **Pratiques de sécurité documentées au niveau déclaratif** : connexions chiffrées, accès nominatifs, droits minimaux, MFA pour les consoles d’administration, secrets hors dépôt et journalisation des accès administratifs (`/entreprise/07_hebergement_securite.md`).
- **Méthode de réalisation structurée** : cadrage, découpage en lots, démonstrations, revue de code, tests, recette et transfert en maintenance (`/entreprise/06_methodes_qualite.md`).

## Risques, écarts et validations nécessaires

### Écarts explicites

Aucun écart explicite ne ressort concernant une exigence obligatoire fonctionnelle ou technologique de la consultation.

En revanche, le dossier entreprise comporte des limites explicites à ne pas ignorer :

- aucune certification ISO 27001 détenue ;
- aucun audit externe d’accessibilité fourni ;
- aucun rapport indépendant de test d’intrusion ;
- aucun contrat d’hébergement signé ni qualification d’hébergeur ;
- aucune astreinte 24 h/24, alors que la consultation ne l’exige pas ;
- aucune disponibilité documentée après décembre 2026 ;
- aucune référence documentée de migration Java, sans lien apparent avec le besoin actuel.

### Preuves ou informations manquantes

- Estimation réelle de charge et de durée pour respecter le budget maximal de **160 000 EUR HT**.
- Planning détaillé jusqu’à la mise en service visée en mars 2027.
- Disponibilité nominative et engagement des personnes proposées.
- Prix d’hébergement et conditions du prestataire.
- Détails de l’API ERP, du nombre d’utilisateurs, des pics de connexion et du volume de documents.
- Définition précise des rôles, des besoins éventuels de SSO/MFA, des durées de conservation et des procédures de suppression.
- Procédure spécifique de notification des incidents de sécurité.
- Démonstration de conformité aux obligations applicables en matière de données personnelles.
- Preuves indépendantes des références A-R01 et A-R02.
- Éventuelle revue ou audit de sécurité avant mise en production, avec périmètre et coût.
- Pièces administratives et assurance professionnelle : aucun justificatif n’est fourni dans le corpus (`/entreprise/09_justificatifs.md`).

### Validations humaines nécessaires

- Le responsable de production doit confirmer l’affectation des ressources et leur disponibilité réelle.
- Le responsable technique doit valider la faisabilité du périmètre avec l’API ERP.
- Le responsable commercial et la direction doivent valider le chiffrage sous plafond et la séparation des coûts d’hébergement et de maintenance.
- Il faut déterminer si la couverture de support proposée répond exactement à la définition contractuelle attendue par l’acheteur.
- Il faut valider les engagements de sécurité, de notification d’incidents et de protection des données avant toute promesse contractuelle.
- Il faut confirmer la possibilité de mobiliser l’équipe entre octobre 2026 et mars 2027, période non couverte intégralement par le plan de charge.

## Questions à poser

### Questions destinées à l’acheteur

Ces questions sont des suggestions d’analyse et ne constituent pas des exigences supplémentaires :

1. Quels sont le nombre d’utilisateurs prévisionnel, le nombre d’utilisateurs simultanés et les pics de connexion attendus ?
2. Quelle est la documentation de l’API REST de l’ERP : authentification, formats, limites de débit, environnements de test et exigences de disponibilité ?
3. Quels rôles utilisateurs et quelles règles d’accès doivent être implémentés ?
4. Le SSO ou la MFA sont-ils requis pour les utilisateurs finaux, ou seulement pour les comptes d’administration ?
5. Quelle durée de conservation est attendue pour les journaux et les documents ?
6. Quelles sont les modalités et délais attendus pour la notification d’un incident de sécurité ?
7. Quel est le volume initial et la croissance prévue des documents à stocker ?
8. Une revue de sécurité doit-elle être réalisée par un tiers indépendant, ou une revue interne est-elle acceptable ?
9. Quelles sont les modalités de contractualisation, de facturation et de recette, annoncées comme devant être précisées après sélection ?

### Validations à demander à l’entreprise

1. Produire une estimation de charge par rôle et un planning détaillé jusqu’à mars 2027.
2. Confirmer les personnes proposées, leur disponibilité nominative et leur taux d’affectation.
3. Vérifier que l’estimation du développement initial reste inférieure ou égale à 160 000 EUR HT, hors hébergement et maintenance.
4. Obtenir un chiffrage séparé de l’hébergement, des licences éventuelles, des déplacements, de la maintenance et d’une éventuelle revue de sécurité.
5. Décrire précisément la gestion des comptes, des rôles, de la journalisation et des incidents de sécurité.
6. Confirmer les engagements applicables aux données personnelles et aux sous-traitants.
7. Préciser la région d’hébergement réellement proposée et fournir, si disponible, la qualification ou les éléments contractuels du prestataire.
8. Vérifier si une revue de sécurité avant mise en service peut être organisée et dans quelles conditions.
9. Rassembler les justificatifs administratifs, l’assurance professionnelle et, si possible, des attestations clients pour les références.
10. Confirmer que la documentation livrée couvrira l’architecture, l’authentification, le déploiement et l’exploitation.

Cette comparaison met en évidence plusieurs correspondances documentées, mais elle ne constitue pas une décision de répondre à la consultation.