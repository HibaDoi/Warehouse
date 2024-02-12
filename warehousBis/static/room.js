// Add event listeners to each radio button
document.querySelectorAll('input[name="roomSelect"]').forEach(function(radio) {
    radio.addEventListener('change', function() {
        // Hide all graph containers initially
        document.getElementById('rooom1Graphs').style.display = 'none';
        document.getElementById('rooom2Graphs').style.display = 'none';
        document.getElementById('rooom3Graphs').style.display = 'none';

        // Show the selected room's graphs
        var selectedRoom = this.value; // Gets the selected radio button's value
        if(selectedRoom === 'room1') {
            document.getElementById('rooom1Graphs').style.display = 'block';
        } else if(selectedRoom === 'room2') {
            document.getElementById('rooom2Graphs').style.display = 'block';
        } else if(selectedRoom === 'room3') {
            document.getElementById('rooom3Graphs').style.display = 'block';
        }
    });
});

// Trigger change event on page load to display the first room's graphs
window.onload = function() {
    // Find the first radio button and set it to checked
    var firstRadio = document.querySelector('input[name="roomSelect"]:first-of-type');
    firstRadio.checked = true;
    firstRadio.dispatchEvent(new Event('change'));
};
