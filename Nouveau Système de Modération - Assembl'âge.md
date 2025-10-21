# Nouveau Système de Modération - Assembl'âge
## Spécifications Complètes

**Date** : 8 octobre 2025  
**Objectif** : Reconstruire le système de modération dans le bon sens

---

## 1. Fonctionnalités Utilisateur (Frontend)

### 1.1 Signaler un Message

**Emplacement** : Page de messagerie (messages.html)

**Interface** :
- Bouton "⚠️ Signaler" à côté de chaque message reçu
- Au clic, ouvre un modal avec :
  - Titre : "Signaler ce message"
  - Raisons prédéfinies :
    - Contenu inapproprié
    - Harcèlement
    - Spam
    - Arnaque / Fraude
    - Autre (champ texte libre)
  - Boutons : "Annuler" / "Signaler"

**API Call** :
```javascript
POST /api/messages/{message_id}/report
Body: {
  reason: "Contenu inapproprié",
  details: "Description optionnelle"
}
```

### 1.2 Bloquer un Utilisateur

**Emplacement** : 
- En-tête de conversation dans messages.html
- Page de profil d'un autre utilisateur

**Interface** :
- Bouton "🚫 Bloquer" dans l'en-tête de conversation
- Au clic, ouvre un modal de confirmation :
  - Titre : "Bloquer cet utilisateur ?"
  - Message : "Vous ne recevrez plus de messages de cet utilisateur et il ne pourra plus voir votre profil."
  - Boutons : "Annuler" / "Bloquer"

**API Call** :
```javascript
POST /api/users/{user_id}/block
```

**Effet** :
- L'utilisateur bloqué ne peut plus envoyer de messages
- L'utilisateur bloqué ne peut plus voir le profil du bloqueur
- Les conversations existantes restent visibles mais grisées

### 1.3 Débloquer un Utilisateur

**Emplacement** : Page de paramètres / profil

**Interface** :
- Section "Utilisateurs bloqués"
- Liste des utilisateurs bloqués avec bouton "Débloquer"

**API Call** :
```javascript
DELETE /api/users/{user_id}/block
```

### 1.4 Signaler un Utilisateur

**Emplacement** : Page de profil d'un autre utilisateur

**Interface** :
- Bouton "⚠️ Signaler cet utilisateur"
- Modal similaire au signalement de message
- Raisons :
  - Comportement inapproprié
  - Faux profil
  - Arnaque
  - Autre

**API Call** :
```javascript
POST /api/users/{user_id}/report
Body: {
  reason: "Comportement inapproprié",
  details: "Description"
}
```

---

## 2. Interface Admin (Backend)

### 2.1 Page de Modération Globale

**Fichier** : admin-moderation.html

**Sections** :

#### A. Statistiques de Modération
- Nombre de messages signalés (non traités)
- Nombre d'utilisateurs signalés (non traités)
- Nombre d'utilisateurs bannis
- Nombre de messages supprimés (ce mois)

#### B. Messages Signalés
**Tableau** :
| ID | Expéditeur | Destinataire | Contenu (aperçu) | Raison | Signalé par | Date | Actions |
|----|------------|--------------|------------------|--------|-------------|------|---------|
| 123 | Jean M. | Marie D. | "Contenu..." | Harcèlement | Sophie L. | 08/10/2025 | Voir / Supprimer / Ignorer |

**Filtres** :
- Tous / Non traités / Traités
- Par raison
- Par date

**Actions** :
- **Voir** : Ouvre un modal avec le message complet et l'historique de conversation
- **Supprimer** : Supprime le message et envoie un avertissement à l'expéditeur
- **Ignorer** : Marque le signalement comme traité sans action
- **Bannir l'expéditeur** : Bannit l'utilisateur qui a envoyé le message

#### C. Utilisateurs Signalés
**Tableau** :
| ID | Nom | Email | Type | Raison | Signalé par | Nb signalements | Date | Actions |
|----|-----|-------|------|--------|-------------|-----------------|------|---------|
| 45 | Jean Martin | jean@... | Aidant | Arnaque | 3 utilisateurs | 3 | 08/10/2025 | Voir profil / Avertir / Bannir |

**Actions** :
- **Voir profil** : Ouvre le profil complet de l'utilisateur
- **Avertir** : Envoie un email d'avertissement
- **Bannir temporairement** : 7 jours / 30 jours
- **Bannir définitivement** : Suppression du compte

#### D. Tous les Messages de la Plateforme
**Tableau** :
| ID | Expéditeur | Destinataire | Aperçu | Date | Statut | Actions |
|----|------------|--------------|--------|------|--------|---------|
| 456 | Marie D. | Sophie L. | "Bonjour..." | 08/10/2025 10:30 | Normal | Voir / Supprimer |

**Filtres** :
- Par utilisateur (recherche)
- Par date
- Par statut (normal / signalé / supprimé)

**Pagination** : 50 messages par page

**Actions** :
- **Voir** : Affiche le message complet avec contexte de conversation
- **Supprimer** : Supprime le message (avec confirmation)

#### E. Utilisateurs Bannis
**Tableau** :
| ID | Nom | Email | Raison du ban | Banni par | Date | Type | Actions |
|----|-----|-------|---------------|-----------|------|------|---------|
| 78 | User X | x@... | Harcèlement | Admin | 05/10/2025 | Définitif | Voir / Débannir |

**Actions** :
- **Voir** : Historique complet des infractions
- **Débannir** : Réactiver le compte

---

## 3. Endpoints API Backend

### 3.1 Signalements de Messages

#### POST /api/messages/:id/report
**Description** : Signaler un message inapproprié  
**Auth** : Utilisateur connecté  
**Body** :
```json
{
  "reason": "Contenu inapproprié",
  "details": "Description optionnelle"
}
```
**Response** :
```json
{
  "success": true,
  "message": "Message signalé avec succès"
}
```

#### GET /api/admin/messages/reported
**Description** : Liste des messages signalés  
**Auth** : Admin uniquement  
**Query params** :
- status: all / pending / resolved
- reason: filter by reason
- page: pagination

**Response** :
```json
{
  "reports": [
    {
      "id": 123,
      "message_id": 456,
      "message_content": "Contenu du message...",
      "sender": {
        "id": 10,
        "name": "Jean Martin",
        "email": "jean@email.com"
      },
      "receiver": {
        "id": 11,
        "name": "Marie Dupont"
      },
      "reporter": {
        "id": 12,
        "name": "Sophie Leroy"
      },
      "reason": "Harcèlement",
      "details": "Description",
      "status": "pending",
      "created_at": "2025-10-08T10:30:00Z"
    }
  ],
  "total": 15,
  "page": 1,
  "per_page": 50
}
```

#### POST /api/admin/messages/:id/moderate
**Description** : Prendre une action de modération sur un message  
**Auth** : Admin uniquement  
**Body** :
```json
{
  "action": "delete" | "ignore",
  "notify_sender": true,
  "ban_sender": false
}
```

### 3.2 Blocage d'Utilisateurs

#### POST /api/users/:id/block
**Description** : Bloquer un utilisateur  
**Auth** : Utilisateur connecté  
**Response** :
```json
{
  "success": true,
  "message": "Utilisateur bloqué"
}
```

#### DELETE /api/users/:id/block
**Description** : Débloquer un utilisateur  
**Auth** : Utilisateur connecté

#### GET /api/users/blocked
**Description** : Liste des utilisateurs bloqués par l'utilisateur connecté  
**Auth** : Utilisateur connecté  
**Response** :
```json
{
  "blocked_users": [
    {
      "id": 45,
      "name": "Jean Martin",
      "blocked_at": "2025-10-08T10:00:00Z"
    }
  ]
}
```

### 3.3 Signalements d'Utilisateurs

#### POST /api/users/:id/report
**Description** : Signaler un utilisateur  
**Auth** : Utilisateur connecté  
**Body** :
```json
{
  "reason": "Comportement inapproprié",
  "details": "Description"
}
```

#### GET /api/admin/users/reported
**Description** : Liste des utilisateurs signalés  
**Auth** : Admin uniquement  
**Response** :
```json
{
  "reports": [
    {
      "user_id": 45,
      "user_name": "Jean Martin",
      "user_email": "jean@email.com",
      "user_type": "aidant",
      "reports_count": 3,
      "reports": [
        {
          "reporter_id": 12,
          "reporter_name": "Sophie Leroy",
          "reason": "Arnaque",
          "details": "...",
          "created_at": "2025-10-08T10:00:00Z"
        }
      ]
    }
  ]
}
```

### 3.4 Modération Admin

#### GET /api/admin/messages/all
**Description** : Tous les messages de la plateforme  
**Auth** : Admin uniquement  
**Query params** :
- user_id: filter by user
- start_date, end_date: date range
- status: normal / reported / deleted
- page: pagination

**Response** :
```json
{
  "messages": [
    {
      "id": 456,
      "sender": {...},
      "receiver": {...},
      "content": "Message content",
      "created_at": "2025-10-08T10:30:00Z",
      "status": "normal",
      "is_reported": false
    }
  ],
  "total": 1250,
  "page": 1,
  "per_page": 50
}
```

#### POST /api/admin/users/:id/ban
**Description** : Bannir un utilisateur  
**Auth** : Admin uniquement  
**Body** :
```json
{
  "reason": "Harcèlement répété",
  "duration": "permanent" | "7_days" | "30_days",
  "notify_user": true
}
```

#### POST /api/admin/users/:id/unban
**Description** : Débannir un utilisateur  
**Auth** : Admin uniquement

#### POST /api/admin/users/:id/warn
**Description** : Envoyer un avertissement à un utilisateur  
**Auth** : Admin uniquement  
**Body** :
```json
{
  "message": "Votre comportement ne respecte pas nos règles..."
}
```

---

## 4. Base de Données

### 4.1 Nouvelles Tables

#### Table: message_reports
```sql
CREATE TABLE message_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    reporter_id INTEGER NOT NULL,
    reason VARCHAR(100) NOT NULL,
    details TEXT,
    status VARCHAR(20) DEFAULT 'pending', -- pending, resolved, ignored
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP,
    resolved_by INTEGER, -- admin_id
    FOREIGN KEY (message_id) REFERENCES messages(id),
    FOREIGN KEY (reporter_id) REFERENCES users(id),
    FOREIGN KEY (resolved_by) REFERENCES users(id)
);
```

#### Table: blocked_users
```sql
CREATE TABLE blocked_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    blocker_id INTEGER NOT NULL,
    blocked_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (blocker_id) REFERENCES users(id),
    FOREIGN KEY (blocked_id) REFERENCES users(id),
    UNIQUE(blocker_id, blocked_id)
);
```

#### Table: user_reports
```sql
CREATE TABLE user_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reported_user_id INTEGER NOT NULL,
    reporter_id INTEGER NOT NULL,
    reason VARCHAR(100) NOT NULL,
    details TEXT,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP,
    resolved_by INTEGER,
    FOREIGN KEY (reported_user_id) REFERENCES users(id),
    FOREIGN KEY (reporter_id) REFERENCES users(id),
    FOREIGN KEY (resolved_by) REFERENCES users(id)
);
```

#### Table: user_bans
```sql
CREATE TABLE user_bans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    banned_by INTEGER NOT NULL, -- admin_id
    reason TEXT NOT NULL,
    duration VARCHAR(20) NOT NULL, -- permanent, 7_days, 30_days
    banned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (banned_by) REFERENCES users(id)
);
```

#### Table: moderation_actions
```sql
CREATE TABLE moderation_actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_id INTEGER NOT NULL,
    action_type VARCHAR(50) NOT NULL, -- delete_message, ban_user, warn_user, etc.
    target_type VARCHAR(20) NOT NULL, -- message, user
    target_id INTEGER NOT NULL,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES users(id)
);
```

### 4.2 Modifications de Tables Existantes

#### Table: messages
Ajouter colonnes :
```sql
ALTER TABLE messages ADD COLUMN is_reported BOOLEAN DEFAULT 0;
ALTER TABLE messages ADD COLUMN is_deleted BOOLEAN DEFAULT 0;
ALTER TABLE messages ADD COLUMN deleted_at TIMESTAMP;
ALTER TABLE messages ADD COLUMN deleted_by INTEGER;
```

---

## 5. Ordre d'Implémentation

### Phase 1 : Frontend Utilisateur (2-3 heures)
1. Ajouter bouton "Signaler" dans messages.html
2. Créer modal de signalement de message
3. Ajouter bouton "Bloquer" dans l'en-tête de conversation
4. Créer modal de blocage d'utilisateur
5. Ajouter section "Utilisateurs bloqués" dans profile.html
6. Ajouter bouton "Signaler" dans les profils utilisateurs
7. Implémenter les appels API frontend

### Phase 2 : Interface Admin (3-4 heures)
1. Créer admin-moderation.html
2. Section statistiques
3. Tableau des messages signalés
4. Tableau des utilisateurs signalés
5. Tableau de tous les messages
6. Tableau des utilisateurs bannis
7. Modals de détails et d'actions

### Phase 3 : Backend API (4-5 heures)
1. Créer les nouvelles tables de base de données
2. Implémenter POST /api/messages/:id/report
3. Implémenter POST /api/users/:id/block et DELETE
4. Implémenter POST /api/users/:id/report
5. Implémenter GET /api/admin/messages/reported
6. Implémenter GET /api/admin/users/reported
7. Implémenter GET /api/admin/messages/all
8. Implémenter POST /api/admin/users/:id/ban
9. Implémenter POST /api/admin/users/:id/warn
10. Middleware de vérification de blocage
11. Middleware de vérification de ban

### Phase 4 : Tests et Déploiement (2 heures)
1. Tests utilisateur : signaler message, bloquer utilisateur
2. Tests admin : voir signalements, bannir utilisateur
3. Tests de permissions et sécurité
4. Déploiement

**Temps total estimé** : 11-14 heures

---

## 6. Sécurité et Permissions

### Vérifications Obligatoires

#### Côté Utilisateur :
- Un utilisateur ne peut pas signaler ses propres messages
- Un utilisateur ne peut pas se bloquer lui-même
- Un utilisateur bloqué ne peut pas envoyer de messages au bloqueur
- Un utilisateur banni ne peut pas se connecter

#### Côté Admin :
- Seuls les utilisateurs avec `user_type = 'admin'` peuvent accéder aux routes /api/admin/*
- Toutes les actions de modération sont loggées dans moderation_actions
- Les admins ne peuvent pas se bannir eux-mêmes

---

## 7. Notifications

### Notifications Email

#### Utilisateur signalé :
- Sujet : "Votre compte a été signalé"
- Contenu : Information sur le signalement et les règles de la communauté

#### Utilisateur banni :
- Sujet : "Votre compte a été suspendu"
- Contenu : Raison du ban, durée, procédure d'appel

#### Utilisateur dont le message a été supprimé :
- Sujet : "Un de vos messages a été supprimé"
- Contenu : Raison de la suppression, avertissement

### Notifications In-App

- Badge de notification pour les admins quand nouveau signalement
- Notification pour l'utilisateur quand son message est supprimé
- Notification pour l'utilisateur quand il reçoit un avertissement

---

**Document créé par** : Assistant Manus  
**Date** : 8 octobre 2025  
**Statut** : Spécifications complètes - Prêt pour implémentation
