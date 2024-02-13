// Initialize the map
var mymap = L.map('map').setView([34.044414357320676, -6.787781743978746], 48);
  
// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
///////////////
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
 setTimeout(display_merchandise, 100);
 
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
         setTimeout(display_merchandise, 1000);
         
     });
}
display_merchandise();
///////////
function routing() {
var previousMarker = null; // Keep track of the previous marker
var polylines = []; // Keep track of polylines

fetch('/warehouse/routing/') // Use the correct path to your Django view
.then(response => response.json())
.then(closest_shortest_path => {
    // Define custom icon options using a predefined icon
    var customIcon = L.icon({
        iconUrl: 'C:/IOT/v.png', // URL to the predefined icon image
        iconSize: [10, 10], // Size of the icon
    });

    // Iterate over each point in the shortest path
    closest_shortest_path.forEach((point, index) => {
        setTimeout(() => {
            // Remove the previous marker if it exists
            if (previousMarker !== null) {
                mymap.removeLayer(previousMarker);
            }

            // Create a marker for each point using the custom icon
            var marker = L.marker([point[0], point[1]], {icon: customIcon}).addTo(mymap);

            previousMarker = marker; // Update the previous marker
        }, index * 1000);
    });

    // Iterate over each segment in the shortest path
    for (var i = 0; i < closest_shortest_path.length - 1; i++) {
        var startPoint = closest_shortest_path[i];
        var endPoint = closest_shortest_path[i + 1];

        // Create a polyline to represent the segment
        var polyline = L.polyline([
            [startPoint[0], startPoint[1]],
            [endPoint[0], endPoint[1]]
        ]).addTo(mymap);
        polylines.push(polyline); // Add polyline to the array
    }

    // Remove the last polyline and marker after routing is completed
    setTimeout(() => {
        if (previousMarker !== null) {
            mymap.removeLayer(previousMarker);
        }
        polylines.forEach(polyline => {
            mymap.removeLayer(polyline);
        });
    }, closest_shortest_path.length * 1000);
});
}

// Change this value to your preferred interval
setInterval(routing, 10000);
routing();    
