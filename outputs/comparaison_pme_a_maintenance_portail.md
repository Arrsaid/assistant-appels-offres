## Documents consultés

- Consultation : `/consultation/01_consultation_maintenance.pdf.md`  
  - Source originale indiquée : `/consultation/01_consultation_maintenance.pdf`
- Entreprise :
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

Les données décrivent une entreprise et une consultation fictives, à usage pédagogique. Les références de l’entreprise sont déclaratives et aucun justificatif indépendant n’est fourni.

## Matrice de comparaison

| Identifiant | Exigence | Nature | Élément entreprise | Constat | Sources |
|---|---|---|---|---|---|
| CMP-01 | Assurer la maintenance corrective et évolutive d’un portail clients existant | Besoin général | L’entreprise développe des portails clients et applications métier. Elle documente une mission de maintenance d’un portail métier comprenant corrections et petites évolutions. | **Couvert par des éléments déclaratifs**, sous réserve de vérifier la stack, la documentation et la volumétrie du portail à reprendre. | Consultation, p. 1, « Besoin » ; `/entreprise/01_presentation.md`, « Activité » ; `/entreprise/03_references.md`, « A-R03 — Maintenance portail métier » ; `/entreprise/08_support_maintenance.md`, « Reprise d’application » |
| CMP-02 | Support du lundi au vendredi, de 8 h à 20 h, heure de Paris | Exigence obligatoire | L’entreprise prévoit une couverture du lundi au vendredi, de 9 h à 18 h, hors jours fériés français. | **Écart explicite** : la plage documentée est plus restreinte, avec une différence d’une heure le matin et de deux heures le soir. | Consultation, p. 1, « Exigences obligatoires » ; `/entreprise/08_support_maintenance.md`, « Couverture » |
| CMP-03 | Prise en charge des incidents critiques P1 en moins de 2 heures ouvrées | Exigence obligatoire | Pour un incident P1, l’objectif documenté de prise en charge est de 4 heures de service. Il s’agit de la qualification et du début d’investigation, et non d’une garantie de résolution. | **Écart explicite** sur le délai documenté : 4 heures de service contre moins de 2 heures ouvrées demandées. La portée exacte de « heures ouvrées » doit néanmoins être confirmée. | Consultation, p. 1, « Exigences obligatoires » ; `/entreprise/08_support_maintenance.md`, « Qualification des incidents » |
| CMP-04 | Fournir un rapport mensuel des incidents | Exigence obligatoire | L’entreprise prévoit un point mensuel portant sur les incidents, la consommation et les évolutions. | **Couvert par des éléments déclaratifs**. Le format, le contenu minimal et le niveau de détail du rapport restent à préciser. | Consultation, p. 1, « Exigences obligatoires » ; `/entreprise/08_support_maintenance.md`, « Organisation » |
| CMP-05 | Présenter au moins une référence de maintenance de portail | Exigence obligatoire | La référence A-R03 concerne la maintenance d’un portail métier, avec corrections et petites évolutions, 38 tickets clos et un support en heures de service. | **Couvert par des éléments déclaratifs**. La référence est pertinente, mais aucune attestation client indépendante ni procès-verbal de recette n’est fourni. | Consultation, p. 1, « Exigences obligatoires » ; `/entreprise/03_references.md`, « A-R03 — Maintenance portail métier » ; `/entreprise/09_justificatifs.md`, « Références de projets » |
| CMP-06 | Respecter un budget maximal de 80 000 EUR HT par an | Contraintes budgétaires | L’entreprise fonctionne sous enveloppe de jours pour la maintenance. Les tarifs documentés sont de 750 €/jour pour le chef de projet, 650 €/jour pour un développeur, 550 €/jour pour le QA et 750 €/jour pour le DevOps. Les coûts d’hébergement, licences, déplacements et sous-traitance sont à ajouter séparément. | **À confirmer** : aucune charge annuelle ni chiffrage complet ne permet de vérifier le respect du plafond. Le tarif journalier ne constitue pas à lui seul un prix annuel. | Consultation, p. 1, « Budget » ; `/entreprise/05_tarifs.md`, « Grille de simulation » et « Construction d’une estimation » ; `/entreprise/08_support_maintenance.md`, « Reprise d’application » |
| CMP-07 | Date limite de réponse : 30 novembre 2026 à 12 h, heure de Paris | Échéance imposée au candidat | Les documents de l’entreprise ne mentionnent pas de validation de cette échéance ni de processus de préparation de réponse associé. | **Information non fournie** dans le corpus de l’entreprise. La date est à respecter si l’entreprise décide de répondre ; aucune conclusion de disponibilité ne peut être tirée. | Consultation, p. 2, « Calendrier » ; `/entreprise/10_preferences.md`, « Validation avant réponse » |
| CMP-08 | Démarrage attendu le 15 janvier 2027 | Date de démarrage attendue | Le plan de charge ne fournit des disponibilités que pour octobre, novembre et décembre 2026. Aucune disponibilité n’est fournie après décembre 2026. | **À confirmer** : la capacité au 15 janvier 2027 n’est pas documentée. Aucun écart explicite ne peut être établi sur cette seule base. | Consultation, p. 2, « Calendrier » ; `/entreprise/04_plan_charge.md`, « Plan de charge et capacité disponible » |
| CMP-09 | Durée initiale de 24 mois | Durée contractuelle attendue | Les documents indiquent que la maintenance est réalisée sous enveloppe de jours, mais ne documentent ni engagement sur 24 mois ni capacité de production sur cette durée. | **Information non fournie / à confirmer**. Les capacités disponibles sont limitées aux mois d’octobre à décembre 2026 et ne valent pas réservation de ressources. | Consultation, p. 2, « Calendrier » ; `/entreprise/04_plan_charge.md`, « Décision d’affectation » ; `/entreprise/05_tarifs.md`, « Modalités commerciales de scénario » |
| CMP-10 | Préciser l’équipe mobilisée | Information à fournir par le candidat | L’entreprise dispose d’un chef de projet, de développeurs, d’un QA et d’un DevOps. Des profils fictifs sont associés à des missions antérieures, mais les disponibilités et l’affectation doivent être validées. | **Partiellement couvert ou à confirmer** : la composition possible est documentée, mais l’équipe effectivement mobilisable pour cette consultation ne l’est pas. | Consultation, p. 2, « Informations à préciser » ; `/entreprise/02_equipe_competences.md`, « Répartition des 12 salariés » et « Profils individuels fictifs » ; `/entreprise/04_plan_charge.md`, « Décision d’affectation » |
| CMP-11 | Préciser les délais de résolution proposés | Information à fournir par le candidat | Les délais documentés sont des objectifs de prise en charge : P1 en 4 heures de service, P2 en 1 jour ouvré et P3 en 3 jours ouvrés. Le rétablissement est évalué après diagnostic. | **Partiellement couvert ou à confirmer** : les objectifs de prise en charge sont documentés, mais les délais de résolution proposés ne le sont pas. Le délai P1 est en outre incompatible avec l’exigence obligatoire de moins de 2 heures. | Consultation, p. 2, « Informations à préciser » ; `/entreprise/08_support_maintenance.md`, « Qualification des incidents » |
| CMP-12 | Préciser la procédure d’escalade | Information à fournir par le candidat | Une organisation de traitement est décrite : ticket centralisé, qualification, affectation, communication au client, correction testée et clôture confirmée. | **Partiellement couvert ou à confirmer** : le processus général est décrit, mais aucune procédure d’escalade formalisée, avec niveaux, responsables et délais, n’est fournie. | Consultation, p. 2, « Informations à préciser » ; `/entreprise/08_support_maintenance.md`, « Organisation » |
| CMP-13 | Préciser les outils de suivi des tickets | Information à fournir par le candidat | L’entreprise mentionne un ticket centralisé, mais aucun outil ou nom de solution n’est précisé. | **Preuve ou information non fournie** concernant l’outil de ticketing. | Consultation, p. 2, « Informations à préciser » ; `/entreprise/08_support_maintenance.md`, « Organisation » |
| CMP-14 | Volumétrie des incidents à préciser par l’acheteur pendant le cadrage | Information attendue de l’acheteur | La référence A-R03 mentionne 38 tickets clos, mais cela ne permet pas d’inférer la volumétrie du présent portail. | **Information à obtenir auprès de l’acheteur** ; la capacité de l’entreprise ne peut pas être évaluée précisément sans cette donnée. | Consultation, p. 2, « L’acheteur précisera pendant le cadrage » ; `/entreprise/03_references.md`, « A-R03 — Maintenance portail métier » |
| CMP-15 | Documentation disponible à préciser par l’acheteur pendant le cadrage | Information attendue de l’acheteur | La méthode de reprise de l’entreprise prévoit un audit de l’existant et nécessite les accès et la documentation nécessaires. | **À confirmer auprès de l’acheteur** : le niveau de documentation du portail est inconnu et peut influencer la charge de reprise. | Consultation, p. 2, « L’acheteur précisera pendant le cadrage » ; `/entreprise/06_methodes_qualite.md`, « Déroulement » ; `/entreprise/08_support_maintenance.md`, « Reprise d’application » |
| CMP-16 | Stack technique actuelle à préciser par l’acheteur pendant le cadrage | Information attendue de l’acheteur | L’entreprise documente Symfony, PHP, Vue.js, PostgreSQL, API REST et Docker. Elle indique également qu’aucune référence de migration Java n’est disponible. | **À confirmer auprès de l’acheteur** : la compatibilité technique ne peut pas être établie avant connaissance de la stack. Si une migration Java était nécessaire, aucune référence correspondante n’est documentée. | Consultation, p. 2, « L’acheteur précisera pendant le cadrage » ; `/entreprise/01_presentation.md`, « Activité » et « Limites explicites » ; `/entreprise/02_equipe_competences.md`, « Compétences non démontrées » |

## Points favorables documentés

- L’entreprise intervient sur les portails clients et applications métier, avec des compétences déclarées en Symfony, PHP, Vue.js, PostgreSQL, API REST et Docker (`/entreprise/01_presentation.md`, « Activité »).
- Une référence déclarative de maintenance d’un portail métier est fournie : corrections, petites évolutions et 38 tickets clos (`/entreprise/03_references.md`, « A-R03 »).
- L’organisation de support comprend la centralisation des tickets, la qualification, l’affectation, la communication au client, la correction testée et la clôture confirmée (`/entreprise/08_support_maintenance.md`, « Organisation »).
- Un point mensuel sur les incidents, la consommation et les évolutions est prévu (`/entreprise/08_support_maintenance.md`, « Organisation »).
- Les méthodes qualité documentent la revue de code, les tests, la recette sur environnement dédié, le suivi des anomalies et la documentation (`/entreprise/06_methodes_qualite.md`, « Déroulement » et « Livrables »).
- Une équipe-type comprenant chef de projet, développeurs, QA et DevOps est documentée, sans que son affectation à cette consultation soit acquise (`/entreprise/02_equipe_competences.md`, « Répartition des 12 salariés » ; `/entreprise/04_plan_charge.md`).

## Risques, écarts et validations nécessaires

### Écarts explicites

1. **Plage de support insuffisante au regard de l’exigence obligatoire**  
   La couverture documentée est de 9 h à 18 h, alors que la consultation exige 8 h à 20 h (`/entreprise/08_support_maintenance.md`, « Couverture » ; consultation, p. 1).

2. **Délai P1 documenté supérieur à l’exigence**  
   L’objectif de prise en charge P1 est de 4 heures de service, contre moins de 2 heures ouvrées demandées (`/entreprise/08_support_maintenance.md`, « Qualification des incidents » ; consultation, p. 1).

### Preuves ou informations manquantes

- Aucun chiffrage ne permet de vérifier le plafond de 80 000 € HT par an.
- Aucun prix d’hébergement, de licence, d’audit externe ou de sous-traitance n’est fourni.
- Les références sont déclaratives et ne sont accompagnées d’aucune attestation client indépendante.
- L’équipe effectivement mobilisable, ses quotités et ses disponibilités à partir de janvier 2027 ne sont pas établies.
- La capacité sur la durée initiale de 24 mois n’est pas documentée.
- Aucun outil de ticketing précis n’est identifié.
- La procédure d’escalade n’est pas formalisée.
- Les délais de résolution ne sont pas définis ; seuls des objectifs de prise en charge sont indiqués.
- La volumétrie, la documentation et la stack du portail cible sont inconnues.

### Validations humaines nécessaires

- Faire valider par le responsable technique et la production la possibilité réelle d’étendre la couverture à 8 h–20 h.
- Faire valider la possibilité de respecter une prise en charge P1 en moins de 2 heures ouvrées ; le corpus actuel documente l’objectif inverse.
- Construire un chiffrage annuel intégrant toutes les charges et coûts annexes.
- Vérifier les ressources disponibles à compter du 15 janvier 2027 et sur 24 mois.
- Identifier l’équipe nominative ou fonctionnelle, les rôles de relais et les niveaux d’escalade.
- Confirmer la compatibilité avec la stack technique et les conditions de reprise du portail.
- Vérifier les pièces administratives, l’assurance professionnelle et les éventuelles exigences de sécurité applicables, qui ne sont pas fournies dans le corpus (`/entreprise/09_justificatifs.md`).

## Questions à poser

### Questions destinées à l’acheteur

Ces questions sont des suggestions d’analyse et ne constituent pas de nouvelles exigences client :

1. Les horaires 8 h–20 h s’appliquent-ils uniquement à la réception et au traitement des tickets, ou impliquent-ils une présence continue et une capacité d’intervention pendant toute la plage ?
2. La notion de « moins de 2 heures ouvrées » pour les incidents P1 désigne-t-elle la prise en charge, le début d’investigation, le rétablissement ou la résolution ?
3. Comment sont définies les heures ouvrées : incluent-elles les jours fériés français ?
4. Le rapport mensuel doit-il comporter des indicateurs imposés, tels que volumes, délais, causes, récurrences et actions correctives ?
5. Quelle volumétrie historique des incidents est prévue, notamment pour les P1, P2 et P3 ?
6. Quelle documentation technique, fonctionnelle et d’exploitation sera remise au titulaire ?
7. Quelle est la stack technique actuelle du portail, ainsi que ses dépendances et contraintes d’hébergement ?
8. Le budget annuel de 80 000 € HT inclut-il l’hébergement, les licences, les évolutions et les éventuels déplacements ?
9. Les 24 mois correspondent-ils à une durée ferme, avec ou sans reconduction ou période de réversibilité ?

### Validations à demander à l’entreprise

1. L’entreprise peut-elle étendre effectivement sa couverture de 9 h–18 h à 8 h–20 h, du lundi au vendredi ?
2. Peut-elle proposer et contractualiser une prise en charge P1 en moins de 2 heures ouvrées ?
3. Quel est le délai de résolution ou de rétablissement proposé par niveau de criticité, distinct du délai de prise en charge ?
4. Quelle procédure d’escalade, avec quels rôles et délais, serait mise en place ?
5. Quel outil de ticketing serait utilisé et quels accès ou rapports seraient fournis à l’acheteur ?
6. Quelle équipe serait mobilisée à partir du 15 janvier 2027, et quelle capacité pourrait-elle garantir pendant 24 mois ?
7. Quel chiffrage annuel complet serait compatible avec le plafond de 80 000 € HT, en distinguant maintenance, évolutions et coûts annexes ?
8. La stack technique cible est-elle compatible avec les compétences documentées, notamment si elle comporte des composants non listés ou une migration Java ?
9. Quelles pièces administratives, assurance et justificatifs pourraient être fournis si la consultation les exigeait ?

Cette comparaison met en évidence les éléments documentés et les points à confirmer, sans se substituer à la décision humaine de répondre ou non à la consultation.