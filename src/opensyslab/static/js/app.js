function updateDateTime() {
    const now = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: false };
    document.getElementById('datetime').textContent = now.toLocaleDateString('fr-FR', options);
}

// Mettre à jour la date et l'heure toutes les secondes
setInterval(updateDateTime, 1000);