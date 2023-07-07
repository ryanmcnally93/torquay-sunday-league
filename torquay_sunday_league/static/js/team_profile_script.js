document.addEventListener('DOMContentLoaded', function() {
    if (parseInt(document.getElementById('no_of_players').innerText) < 16) {
        document.getElementById('no_of_players').style.color = "red";
        document.getElementById('no_of_players').title = "You must have 16 players to be accepted";
    }
});