# Analyse de la consultation

La consultation est explicitement présentée comme **fictive**, à usage pédagogique uniquement. L’analyse porte exclusivement sur le document `/consultation/01_consultation_maintenance.pdf.md`, correspondant au PDF original `/consultation/01_consultation_maintenance.pdf`.

## Besoin

L’acheteur recherche une prestation de **maintenance corrective et évolutive d’un portail clients existant**.

Les prestations attendues comprennent notamment :

- la correction des incidents affectant le portail ;
- la réalisation d’évolutions sur le portail ;
- un dispositif de support couvrant les plages horaires demandées ;
- la prise en charge prioritaire des incidents critiques ;
- le suivi et le reporting mensuel des incidents ;
- la présentation d’au moins une référence comparable.

La volumétrie des incidents, la documentation disponible et la stack technique actuelle ne sont pas encore définies dans les documents consultés. Elles doivent être précisées par l’acheteur pendant le cadrage.

**Source :** `/consultation/01_consultation_maintenance.pdf`, page 1, section « Besoin » et section « Exigences obligatoires » ; page 2, section « Informations à préciser ».

## Exigences

| Identifiant | Exigence | Nature | Source |
|---|---|---|---|
| EX-01 | Assurer la maintenance corrective du portail clients existant. | obligatoire | `/consultation/01_consultation_maintenance.pdf`, page 1, section « Besoin » |
| EX-02 | Assurer la maintenance évolutive du portail clients existant. | obligatoire | `/consultation/01_consultation_maintenance.pdf`, page 1, section « Besoin » |
| EX-03 | Assurer un support du lundi au vendredi, de 8 h à 20 h, heure de Paris. | obligatoire | `/consultation/01_consultation_maintenance.pdf`, page 1, section « Exigences obligatoires » |
| EX-04 | Prendre en charge les incidents critiques de priorité P1 en moins de 2 heures ouvrées. | obligatoire | `/consultation/01_consultation_maintenance.pdf`, page 1, section « Exigences obligatoires » |
| EX-05 | Fournir un rapport mensuel des incidents. | obligatoire | `/consultation/01_consultation_maintenance.pdf`, page 1, section « Exigences obligatoires » |
| EX-06 | Présenter au moins une référence de maintenance de portail. | obligatoire | `/consultation/01_consultation_maintenance.pdf`, page 1, section « Exigences obligatoires » |
| EX-07 | Préciser l’équipe mobilisée. | obligatoire — information à fournir dans la réponse | `/consultation/01_consultation_maintenance.pdf`, page 2, section « Informations à préciser » |
| EX-08 | Préciser les délais de résolution proposés. | obligatoire — information à fournir dans la réponse | `/consultation/01_consultation_maintenance.pdf`, page 2, section « Informations à préciser » |
| EX-09 | Préciser la procédure d’escalade. | obligatoire — information à fournir dans la réponse | `/consultation/01_consultation_maintenance.pdf`, page 2, section « Informations à préciser » |
| EX-10 | Préciser les outils de suivi des tickets. | obligatoire — information à fournir dans la réponse | `/consultation/01_consultation_maintenance.pdf`, page 2, section « Informations à préciser » |
| EX-11 | La volumétrie des incidents sera précisée pendant le cadrage. | non précisée — donnée nécessaire à confirmer | `/consultation/01_consultation_maintenance.pdf`, page 2, section « L’acheteur précisera pendant le cadrage » |
| EX-12 | La documentation disponible sera précisée pendant le cadrage. | non précisée — donnée nécessaire à confirmer | `/consultation/01_consultation_maintenance.pdf`, page 2, section « L’acheteur précisera pendant le cadrage » |
| EX-13 | La stack technique actuelle sera précisée pendant le cadrage. | non précisée — donnée nécessaire à confirmer | `/consultation/01_consultation_maintenance.pdf`, page 2, section « L’acheteur précisera pendant le cadrage » |

Aucun élément n’est explicitement identifié comme **souhaité** dans les documents consultés. Les éléments EX-11 à EX-13 ne constituent pas des prestations à fournir, mais des informations techniques et opérationnelles restant à préciser par l’acheteur.

## Budget

- **Budget maximal :** 80 000 EUR HT par année.
- **Nature du montant :** plafond budgétaire maximal, et non estimation.
- **Périmètre couvert :** la consultation indique que ce budget concerne la prestation de maintenance du portail clients, sans fournir de ventilation entre maintenance corrective, maintenance évolutive, support ou reporting.
- **Durée initiale :** 24 mois. Le document ne précise pas si le budget maximal de 80 000 EUR HT s’applique à chaque année contractuelle ou à l’ensemble des 24 mois ; la formulation « par année » suggère un plafond annuel, mais ce point mérite confirmation.
- **Exclusions :** aucune exclusion budgétaire explicite n’est indiquée.

**Source :** `/consultation/01_consultation_maintenance.pdf`, page 1, section « Budget » ; page 2, section « Calendrier ».

## Calendrier

### Échéance imposée

- **Date limite de réponse :** 30 novembre 2026 à 12 h, heure de Paris.

### Date de démarrage attendue

- **Démarrage attendu :** 15 janvier 2027.

Le document qualifie cette date de démarrage « attendu », sans préciser s’il s’agit d’une échéance contractuellement impérative ou d’un objectif.

### Durée

- **Durée initiale :** 24 mois.

**Source :** `/consultation/01_consultation_maintenance.pdf`, page 2, section « Calendrier ».

## Points à clarifier

### Informations explicitement demandées dans la consultation

Le candidat doit préciser :

1. l’équipe mobilisée ;
2. les délais de résolution proposés ;
3. la procédure d’escalade ;
4. les outils de suivi des tickets.

**Source :** `/consultation/01_consultation_maintenance.pdf`, page 2, section « Informations à préciser ».

L’acheteur indique également que les éléments suivants seront précisés pendant le cadrage :

- la volumétrie des incidents ;
- la documentation disponible ;
- la stack technique actuelle.

**Source :** `/consultation/01_consultation_maintenance.pdf`, page 2, section « L’acheteur précisera pendant le cadrage ».

### Ambiguïtés ou contradictions relevées

- **Budget sur 24 mois :** le budget est exprimé à 80 000 EUR HT « par année », tandis que la durée initiale est de 24 mois. Le document ne précise pas explicitement si le plafond total attendu est de 160 000 EUR HT sur deux ans, ni les modalités de révision éventuelle.
- **Portée de la maintenance évolutive :** le document mentionne la maintenance évolutive, mais ne précise ni le volume d’évolutions attendu, ni la méthode de chiffrage, ni les limites de cette prestation.
- **Délais de résolution :** seul le délai de prise en charge des incidents P1 est défini — moins de 2 heures ouvrées. Les délais applicables aux autres niveaux de priorité ne sont pas précisés.
- **Définition de P1 :** la consultation ne définit pas les critères permettant de qualifier un incident de priorité P1.
- **Plage de support :** le support est prévu du lundi au vendredi, de 8 h à 20 h, heure de Paris, mais la consultation ne précise pas si les jours fériés sont inclus.
- **Date de démarrage :** le 15 janvier 2027 est présenté comme un démarrage attendu, sans indication sur son caractère impératif.
- **Référence demandée :** une référence de maintenance de portail est exigée, mais les critères d’acceptabilité de cette référence — ancienneté, durée, périmètre ou coordonnées vérifiables — ne sont pas précisés.
- **Livrables et indicateurs :** le rapport mensuel des incidents est exigé, mais son contenu minimal, ses indicateurs et son format ne sont pas définis.

### Suggestions de l’agent, non formulées dans la consultation

- Demander la définition précise des niveaux de priorité, notamment les critères de qualification d’un incident P1.
- Demander les délais de prise en charge et de résolution attendus pour les incidents non-P1.
- Clarifier le mode de calcul du délai de deux heures ouvrées et les modalités applicables en dehors des horaires de support.
- Confirmer le traitement des week-ends et jours fériés.
- Demander si le budget annuel de 80 000 EUR HT est ferme pour chacune des deux années et s’il inclut l’ensemble des évolutions.
- Préciser le périmètre de la maintenance évolutive : nombre de jours, volume de demandes, processus de priorisation et modalités de validation.
- Demander le contenu attendu du rapport mensuel et les indicateurs de performance à produire.
- Clarifier les modalités d’accès au portail, aux environnements techniques, aux journaux et aux outils de supervision.
- Demander les conditions de réversibilité et de transfert de connaissances en fin de prestation.
- Préciser les modalités de sécurité, de confidentialité et de protection des données traitées par le portail.