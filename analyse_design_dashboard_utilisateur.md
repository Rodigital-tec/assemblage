# Analyse du design du dashboard utilisateur Assembl'âge

## Éléments clés observés

### Header
- Fond blanc
- Logo à gauche
- Menu de navigation horizontal avec liens encadrés de couleurs différentes :
  - Tableau de bord : violet
  - Mes offres : orange
  - Recherche : violet
  - Messages : turquoise
  - Mon profil : rose
- Badge "Senior" turquoise à droite
- Bouton "Déconnexion" rose à droite
- Icône de notification orange

### Section d'accueil
- Carte avec bordure verte à gauche
- Avatar circulaire avec initiales "MD" sur fond vert
- Message de bienvenue "Bonjour Marie !"
- Sous-titre gris
- Badge "Senior" turquoise à droite
- Fond blanc

### Actions rapides
- Titre "Actions rapides" avec barre verte à gauche
- 4 grandes cartes colorées avec bordures :
  1. **Nouvelle demande** - Fond vert clair, bordure verte
  2. **Recherche géolocalisée** - Fond rose clair, bordure rose
  3. **Mon profil** - Fond bleu clair, bordure bleue
  4. **Messagerie** - Fond rose clair, bordure rose/rouge
- Chaque carte contient :
  - Icône SVG monochrome grande
  - Titre en gras
  - Description en gris
- Espacement généreux entre les cartes

### Sections Demandes récentes et Calendrier
- Titre avec icône SVG à gauche
- Bouton "Voir tout" vert à droite
- État vide avec grande icône grise et texte centré
- Fond blanc

### Couleurs principales
- **Vert** : #9ACD32 (actions, bordures, badges)
- **Turquoise** : #00A0B0 (badges, liens)
- **Rose/Rouge** : #FF6B9D (cartes, boutons)
- **Bleu** : #4A90E2 (cartes)
- **Gris** : #666666 (textes secondaires)
- **Blanc** : Fond principal

### Style général
- Design épuré avec beaucoup d'espace blanc
- Cartes avec bordures colorées (2-3px)
- Ombres légères sur les cartes
- Coins arrondis (border-radius: 8-12px)
- Typographie Montserrat
- Icônes SVG monochromes
- Espacement généreux (padding, margin)

### Structure
- Pas de sidebar
- Navigation uniquement par header
- Contenu centré avec max-width
- Layout en grille pour les cartes d'actions
- Responsive avec cartes empilées sur mobile
