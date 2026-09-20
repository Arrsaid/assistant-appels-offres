# Hébergement, sécurité et sauvegardes

> DONNÉES SYNTHÉTIQUES — ENTREPRISE FICTIVE — usage de test uniquement.
> Dossier : PME A — Atelier Portail (nom de scénario). Version 1.0, situation au 18 septembre 2026.

## Architecture de référence proposée

Application conteneurisée, base PostgreSQL, environnements de test et de production séparés. Hébergement chez un prestataire à sélectionner, région France envisagée ; aucun contrat ni qualification d’hébergeur n’est fourni.

## Contrôles internes de scénario

Accès nominatifs et droits minimaux ; authentification multifacteur pour les consoles d’administration ; secrets hors du dépôt de code ; connexions chiffrées ; journalisation des accès administratifs ; suppression des accès lors d’un départ.

## Sauvegarde et reprise

Sauvegarde quotidienne, rétention de 30 jours ; restauration testée trimestriellement sur un environnement de test. Cible de perte de données maximale : 24 heures ; cible de remise en service : 2 jours ouvrés. Ce sont des objectifs internes à contractualiser.

Une sauvegarde n’est pas une preuve de haute disponibilité. Aucun engagement de disponibilité en pourcentage n’est fixé dans le corpus. Les obligations relatives aux données et aux sous-traitants doivent être examinées pour chaque dossier, sans conclure à une conformité générale à partir de cette fiche.

## Pièces absentes

Rapport de test d’intrusion indépendant, contrat d’hébergement signé, rapport de restauration et attestation de certification. Leur absence dans le corpus ne doit pas être transformée en preuve positive.

