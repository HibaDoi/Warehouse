
// Initialize the map
var mymap = L.map('map').setView([34.044414357320676, -6.787781743978746], 48);

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
///////////////
fetch('/warehouse/get_infra/')
.then(response => response.json())
.then(data => {
var jsonObject = JSON.parse(data);
L.geoJson(jsonObject, {
    style: function (feature) {
        return {
            fillColor: feature.properties.color,
            color: 'black',
            weight: 0.8,
            fillOpacity: 0
        };
    }
}).addTo(mymap);
setTimeout(display_merchandise, 1000);

});

/////////////
var merchandiseLayer = null;

function display_merchandise() {
    // Clear existing merchandise layer if it exists
    

    fetch('/warehouse/get_shelf_data/')
        .then(response => response.json())
        .then(data => {
            var jsonObject = JSON.parse(data);
            if (merchandiseLayer !== null) {
                mymap.removeLayer(merchandiseLayer);
            }
            merchandiseLayer = L.geoJson(jsonObject, {
                style: function (feature) {
                    return {
                        fillColor: feature.properties.color,
                        color: 'black',
                        weight: 0.8,
                        fillOpacity: 0.8
                    };
                }
            }).addTo(mymap);
            setTimeout(display_merchandise, 5000);
            
        });
}

// Set the function to run every 2 seconds (2000 milliseconds)
display_merchandise();
//setInterval(display_merchandise, 1000);



