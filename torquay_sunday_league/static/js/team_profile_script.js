document.addEventListener('DOMContentLoaded', function () {
    if (parseInt(document.getElementById('no_of_players').innerText) < 16) {
        // This code displays the message for a team with less than 16 players
        document.getElementById('no_of_players').style.color = "red";
        document.getElementById('no_of_players').title = "You must have 16 players to be accepted";
    }
});