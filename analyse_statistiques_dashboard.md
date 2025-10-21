# Analyse des éléments de statistiques à supprimer

## Éléments identifiés dans dashboard.html

### 1. Section "Statistiques" (stats-grid)
**Lignes 495-523**

Cette section contient 4 cartes de statistiques :

1. **Demandes actives**
   - Icône : icon-request
   - Nombre : 5
   - Label : DEMANDES ACTIVES
   - Détail : 5 demandes en cours

2. **Messages reçus**
   - Icône : icon-message
   - Nombre : 4
   - Label : MESSAGES REÇUS
   - Détail : 4 nouvelles conversations

3. **Aides reçues**
   - Icône : icon-help
   - Nombre : 0
   - Label : AIDES REÇUES
   - Détail : Trouvez de l'aide

4. **Statut**
   - Icône : icon-star
   - Nombre : N/A
   - Label : STATUT
   - Détail : Nouveau membre

## Raison de la suppression

Ces statistiques peuvent être **intimidantes ou confuses pour les personnes âgées** :
- Trop d'informations chiffrées
- Pas directement actionnables
- Peuvent créer de l'anxiété (ex: "5 demandes en cours")
- Complexifient l'interface

## Recommandation

**Supprimer complètement la section stats-grid** pour :
- Simplifier l'interface
- Réduire la charge cognitive
- Mettre l'accent sur les actions concrètes (Actions rapides)
- Améliorer la lisibilité globale

Les informations importantes (messages, demandes) seront toujours accessibles via :
- Les sections "Demandes récentes" et "Nouvelles opportunités"
- Le menu de navigation (Messages, Mes offres)
