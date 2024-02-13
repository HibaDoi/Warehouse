function EMPTY() {
fetch('/warehouse/empty_shelf/')
    .then(response => response.json())
    .then(data => {

        var tdata = [
            {
                domain: { x: [0, 1], y: [0, 1] },
                value: data.r1,
                title: { text: "Room 1" },
                type: "indicator",
                mode: "gauge+number",
             gauge: {
              axis: { range: [null, 12] },bar: { color:'rgba(255, 255, 255, 1)' } },
            }
        ];
        var ttdata = [
            {
                domain: { x: [0, 1], y: [0, 1] },
                value: data.r2,
                title: { text: "Room 2" },
                type: "indicator",
                mode: "gauge+number",
             gauge: {
              axis: { range: [null, 12] }},
            }
        ];
        var tttdata = [
            {
                domain: { x: [0, 1], y: [0, 1] },
                value: data.r3,
                title: { text: "Room 3" },
                type: "indicator",
                mode: "gauge+number",
             gauge: {
              axis: { range: [null, 12] }},
            }
        ];
        
        var layout = { width: 250, height: 150, margin: { t: 0, b: 0 },
        paper_bgcolor : 'rgba(0,0,0,0)', 
        plot_bgcolor : 'rgba(21, 39, 27, 1)' };
        Plotly.newPlot('rooom1Graphss', tdata, layout);
        Plotly.newPlot('rooom2Graphss', ttdata, layout);
        Plotly.newPlot('rooom3Graphss', tttdata, layout);
        
    })
    .catch(error => console.error('Error:', error));
}
EMPTY()
setInterval(EMPTY, 2000);

