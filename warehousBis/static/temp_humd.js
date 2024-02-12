
let temperatureChart; // Declare this outside to make it accessible globally
let temperatureChart2; 
let temperatureChart3; 
let humidityChart;
let humidityChart2;
let humidityChart3
function fetchDataAndUpdateChart() {
    fetch('/warehouse/get_temperature_data/') // Use the correct path to your Django view
    .then(response => response.json())
    .then(data => {
        if (temperatureChart) {
        // Update the chart if it already exists
        temperatureChart.data.labels = data.labels;
        temperatureChart.data.datasets[0].data = data.datasets[0].data;
        temperatureChart.update();
        } else {
        // Create the chart if it does not exist
        var ctxTemperature = document.getElementById('temperatureGraph').getContext('2d');
        temperatureChart = new Chart(ctxTemperature, {
            type: 'line',
            data: data,
            options: {
               
            }
        });
        }
        if (temperatureChart2) {
        // Update the chart if it already exists
        temperatureChart2.data.labels = data.labels2;
        temperatureChart2.data.datasets[0].data = data.datasets2[0].data2;
        temperatureChart2.update();
        } else {
        // Create the chart if it does not exist
        var ctxTemperature2 = document.getElementById('temperatureGraph2').getContext('2d');
        temperatureChart2 = new Chart(ctxTemperature2, {
            type: 'line',
            data: data,
            options: {}
        });
        }
        if (temperatureChart3) {
        // Update the chart if it already exists
        temperatureChart3.data.labels = data.labels3;
        temperatureChart3.data.datasets[0].data = data.datasets3[0].data3;
        temperatureChart3.update();
        } else {
        // Create the chart if it does not exist
        var ctxTemperature3 = document.getElementById('temperatureGraph3').getContext('2d');
        temperatureChart3 = new Chart(ctxTemperature3, {
            type: 'line',
            data: data,
            options: {}
        });
        }
        function showChart(chart) {
        if (chart) {
            chart.canvas.parentNode.style.display = 'block'; // Affiche le conteneur du graphique
        }
    }

    }
    )
    .catch(error => console.error('Error fetching temperature data:', error));

    /////////////////////////////////////////////////////
    fetch('/warehouse/get_humidity_data/') // Use the correct path to your Django view
    .then(response => response.json())
    .then(data => {
        if (humidityChart) {
        // Update the chart if it already exists
        humidityChart.data.labels = data.labels;
        humidityChart.data.datasets[0].data = data.datasets[0].data;
        humidityChart.update();
        } else {
        // Create the chart if it does not exist
        var ctxTemperature = document.getElementById('humidityGraph').getContext('2d');
        humidityChart = new Chart(ctxTemperature, {
            type: 'line',
            data: data,
            options: {}
        });
        }
        if (humidityChart2) {
        // Update the chart if it already exists
        humidityChart2.data.labels = data.labels3;
        humidityChart2.data.datasets[0].data = data.datasets3[0].data3;
        humidityChart2.update();
        } else {
        // Create the chart if it does not exist
        var ctxTemperature2 = document.getElementById('humidityGraph2').getContext('2d');
        humidityChart2 = new Chart(ctxTemperature2, {
            type: 'line',
            data: data,
            options: {}
        });
        }
        if (humidityChart3) {
        // Update the chart if it already exists
        humidityChart3.data.labels = data.labels3;
        humidityChart3.data.datasets[0].data = data.datasets3[0].data3;
        humidityChart3.update();
        } else {
        // Create the chart if it does not exist
        var ctxTemperature3 = document.getElementById('humidityGraph3').getContext('2d');
        humidityChart3 = new Chart(ctxTemperature3, {
            type: 'line',
            data: data,
            options: {}
        });
        }
    
    function showChart(chart) {
        if (chart) {
            chart.canvas.parentNode.style.display = 'block'; // Affiche le conteneur du graphique
        }
    }




    })
    .catch(error => console.error('Error fetching temperature data:', error));
}
///////////////////////////////////////////////////////////


// Set the function to run every 2 seconds (2000 milliseconds)
const INTERVAL = 2000; // Change this value to your preferred interval
setInterval(fetchDataAndUpdateChart, INTERVAL);

// Fetch data and create the chart when the page loads for the first time
window.onload = fetchDataAndUpdateChart;
