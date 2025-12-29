let chart;

const weight = document.getElementById("weight");
const origin = document.getElementById("origin");
const destination = document.getElementById("destination");
const transport = document.getElementById("transport");
const packaging = document.getElementById("packaging");
const result = document.getElementById("result");

async function calculate() {
  console.log("weight:", weight.value);
  console.log("origin:", origin.value);
  console.log("destination:", destination.value);
  console.log("transport:", transport.value);
  console.log("packaging:", packaging.value);

  const response = await fetch("http://127.0.0.1:8000/api/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      weight: Number(weight.value),
      quantity: 1,
      origin_zip: origin.value,
      destination_zip: destination.value,
      transport_mode: transport.value,
      packaging: packaging.value
    })
  });

  const data = await response.json();

  console.log("response data:", data);

  result.innerHTML = `
    🌍 CO₂ Emission: <b>${data.carbon_kg} kg</b><br>
    📏 Distance: ${data.distance_km} km<br>
    🟢 Eco Score: ${data.eco_score}
  `;

  drawChart(data.carbon_kg);
}

function drawChart(co2) {
  const ctx = document.getElementById("co2Chart");

  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["This Shipment"],
      datasets: [{
        label: "CO₂ Emission (kg)",
        data: [co2],
        backgroundColor: 'rgba(75, 192, 192, 0.6)'
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}
