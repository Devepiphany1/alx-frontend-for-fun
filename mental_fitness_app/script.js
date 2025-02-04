document.getElementById('moodForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const mood = document.getElementById('mood').value;
    alert('Mood recorded: ' + mood);
    // Here you can add functionality to save the mood to a database or local storage
});
