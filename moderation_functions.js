// Fonctions de Modération Utilisateur
let currentMessageIdToReport = null;
let currentUserIdToBlock = null;

// Afficher le modal de signalement de message
function showReportMessageModal(messageId) {
    currentMessageIdToReport = messageId;
    document.getElementById('reportMessageModal').style.display = 'flex';
    document.getElementById('reportReason').value = '';
    document.getElementById('reportDetails').value = '';
}

// Cacher le modal de signalement
function hideReportMessageModal() {
    document.getElementById('reportMessageModal').style.display = 'none';
    currentMessageIdToReport = null;
}

// Soumettre le signalement de message
function submitReportMessage() {
    const reason = document.getElementById('reportReason').value;
    const details = document.getElementById('reportDetails').value;
    
    if (!reason) {
        alert('Veuillez sélectionner une raison');
        return;
    }
    
    const API_URL = window.API_BASE_URL || '';
    
    fetch(`${API_URL}/api/messages/${currentMessageIdToReport}/report`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include',
        body: JSON.stringify({
            reason: reason,
            details: details
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Message signalé avec succès. Notre équipe va l\'examiner.');
            hideReportMessageModal();
        } else {
            alert('Erreur lors du signalement: ' + (data.message || 'Erreur inconnue'));
        }
    })
    .catch(error => {
        console.error('Erreur:', error);
        alert('Erreur lors du signalement du message');
    });
}

// Afficher le modal de blocage d'utilisateur
function showBlockUserModal(userId, userName) {
    currentUserIdToBlock = userId;
    document.getElementById('blockUserName').textContent = userName;
    document.getElementById('blockUserModal').style.display = 'flex';
}

// Cacher le modal de blocage
function hideBlockUserModal() {
    document.getElementById('blockUserModal').style.display = 'none';
    currentUserIdToBlock = null;
}

// Soumettre le blocage d'utilisateur
function submitBlockUser() {
    const API_URL = window.API_BASE_URL || '';
    
    fetch(`${API_URL}/api/users/${currentUserIdToBlock}/block`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Utilisateur bloqué avec succès');
            hideBlockUserModal();
            // Recharger la page ou mettre à jour l'interface
            location.reload();
        } else {
            alert('Erreur lors du blocage: ' + (data.message || 'Erreur inconnue'));
        }
    })
    .catch(error => {
        console.error('Erreur:', error);
        alert('Erreur lors du blocage de l\'utilisateur');
    });
}
