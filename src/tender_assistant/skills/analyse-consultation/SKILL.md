---
name: analyse-consultation
description: Analyser les documents d’une consultation pour identifier le besoin, les exigences, le budget, les échéances et les informations à clarifier.
---

# Analyser une consultation

## Étapes

1. Découvrir les documents disponibles dans /consultation/ avec ls.
2. Lire les documents pertinents avec read_file.
3. Extraire les éléments demandés ci-dessous.
4. Citer le fichier source de chaque élément.
5. Signaler les contradictions ou informations manquantes.

## Résultat attendu

### Besoin

Présenter l’objet de la consultation et les prestations attendues.

### Exigences

Produire un tableau avec les colonnes :
- Identifiant attribué pour l’analyse : EX-01, EX-02, etc.
- Exigence.
- Nature : obligatoire, souhaitée ou non précisée.
- Source : chemin du fichier et section.

Conserver les nuances du document.
Ne pas transformer un souhait en obligation.
Les identifiants sont des repères internes, pas des identifiants du client.

### Budget

Indiquer les montants, leur périmètre et les exclusions explicites.
Ne pas inventer de ventilation budgétaire.

### Calendrier

Relever les dates et distinguer les échéances imposées
des objectifs ou dates souhaitées.

### Points à clarifier

Lister les informations explicitement manquantes ou ambiguës.
Distinguer les questions proposées par l’agent des demandes du client.

## Limites de cette analyse

Ne pas encore comparer la consultation avec une entreprise.
Ne pas conclure à une décision de répondre.
Si la consultation est fictive, le préciser.