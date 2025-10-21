# Audit UX Assembl'âge - Notes

## Page d'accueil (index.html)

### Observations initiales
- URL testée: https://5001-itb52pwaoahg1upikz61n-f39a189e.manusvm.computer/
- Titre: "Assembl'âge - Entraide entre générations"
- Navigation visible avec logo et menu

### Éléments à analyser
- Structure de navigation
- Hiérarchie visuelle
- Accessibilité
- Responsive design
- Cohérence des couleurs
- Lisibilité pour seniors

---



## Observations détaillées par page

### 1. Page d'accueil (index.html)

**Points positifs:**
- Design moderne avec dégradé vert-bleu cohérent avec la marque
- Sections bien structurées (Services, Comment ça marche)
- Icônes visuelles pour illustrer les services
- Comptes de test visibles pour faciliter les tests

**Problèmes identifiés:**
- Navigation: Bordures colorées différentes sur chaque onglet (jaune, violet, bleu, rose) - manque de cohérence
- Titre principal en jaune (#FFEB3B) - couleur trop vive, contraste insuffisant sur fond blanc
- Boutons "Se connecter" et "Tableau de bord" avec des styles différents
- Pas de footer visible
- Espacement entre sections pourrait être amélioré

### 2. Page de connexion (login.html)

**Points positifs:**
- Formulaire centré et simple
- Comptes de test affichés clairement
- Bouton "Retour à l'accueil" présent

**Problèmes identifiés:**
- Labels des champs en rouge (#FF0000) - couleur agressive et non accessible
- Champs de formulaire avec bordures de couleurs différentes (vert, bleu)
- Bouton "Se connecter" en rouge rosé - couleur inhabituelle pour une action primaire
- Manque de hiérarchie visuelle claire
- Pas d'indication de chargement lors de la connexion

### 3. Tableau de bord (dashboard.html)

**Points positifs:**
- Message de bienvenue personnalisé
- Cartes d'actions rapides avec icônes
- Sections pour demandes récentes et opportunités
- Calendrier intégré

**Problèmes identifiés:**
- Cartes d'actions rapides avec bordures de couleurs différentes (bleu, rouge, vert, violet) - manque de cohérence
- Titre "Bonjour Marie !" trop petit
- Icône de notification (0) peu visible
- Sections vides ("Aucune demande récente", "Aucun événement prévu") - manque de guidance
- Pas de statistiques (conformément aux spécifications, mais pourrait être remplacé par autre chose)
- Menu utilisateur en haut à droite peu visible

### 4. Page de recherche (search.html)

**Points positifs:**
- Filtres de recherche bien organisés
- Options de tri disponibles
- Affichage des résultats avec informations clés
- Badges de services colorés

**Problèmes identifiés:**
- Menu utilisateur déroulant visible en permanence (Mon profil, Déconnexion)
- Filtres avec bordures de couleurs différentes (violet, jaune, rose, violet)
- Boutons de tri avec bordures colorées différentes
- Cartes de résultats sans hiérarchie visuelle claire
- Services affichés mais parfois vides
- Bouton "Proposer mon aide" répété - manque de cohérence

### 5. Page de messagerie (messages.html)

**Points positifs:**
- Interface de messagerie complète avec liste de conversations
- Boutons de modération (Signaler, Bloquer) présents
- Modals de modération fonctionnels (correction récente)
- Icônes pour actions (recherche, appel vidéo, etc.)

**Problèmes identifiés:**
- Bannière en haut avec dégradé vert-bleu prend beaucoup d'espace
- Boutons de filtrage avec bordures colorées différentes
- Icônes de fonctionnalités (fichier, emoji, vocal, position) avec bordures colorées
- Conversations avec bordures de couleurs différentes (vert, orange, bleu)
- Zone de saisie de message peu visible
- Trop d'options pour des seniors (appel vidéo, message vocal, partage de position)

### 6. Page de profil (profile.html)

**Points positifs:**
- Informations personnelles bien organisées
- Présentation de l'utilisateur visible
- Statistiques affichées (contrairement aux spécifications qui demandent de les supprimer)

**Problèmes identifiés:**
- Nom de l'utilisateur en jaune vif (#FFEB3B) - peu lisible
- Statistiques présentes alors que les spécifications demandent de les supprimer pour les seniors
- Bouton "Modifier" en rouge - couleur inhabituelle
- Manque de photo de profil
- Présentation textuelle peu mise en valeur

### 7. Page Mes offres (my-service-offers.html)

**Points positifs:**
- État vide bien géré avec message et icône
- Bouton d'action clair "Créer ma première offre"

**Problèmes identifiés:**
- Bouton "Nouvelle offre" en vert avec dégradé à droite
- Bouton "Créer ma première offre" en rouge - incohérence
- Manque de guidance sur ce qu'est une offre de service

## Problèmes transversaux

### Navigation
- Bordures colorées différentes sur chaque onglet du menu (jaune, violet, bleu, rose, vert)
- Manque de cohérence dans les couleurs utilisées
- Pas d'indication claire de la page active

### Couleurs
- Utilisation excessive de couleurs vives (jaune, rouge, rose, violet, bleu)
- Manque de respect de la charte graphique (vert et gris foncé du logo)
- Contraste insuffisant sur certains éléments (texte jaune sur blanc)
- Couleurs différentes pour des éléments similaires (boutons, bordures)

### Typographie
- Tailles de texte variables sans hiérarchie claire
- Manque de contraste sur certains textes
- Police Montserrat bien utilisée mais tailles incohérentes

### Accessibilité pour seniors
- Trop d'options et de fonctionnalités complexes (messagerie)
- Statistiques présentes alors qu'elles devraient être supprimées
- Manque de guidance et d'aide contextuelle
- Icônes sans labels textuels
- Boutons et zones cliquables parfois petits

### Design system
- Absence de cohérence dans les styles de boutons
- Bordures colorées différentes partout
- Manque de système de design unifié
- Incohérence dans les espacements et les marges

---

