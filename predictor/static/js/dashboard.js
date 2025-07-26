const map = L.map('map').setView([9.082, 8.6753], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

map.on('click', async function(e) {
    const { lat, lng } = e.latlng;
    const response = await fetch(`/get-fire-data/?lat=${lat}&lon=${lng}`);
    const data = await response.json();
    document.getElementById('fire-info').innerHTML = `
        <h3>🔥 Risk: ${data.risk}</h3>
        <p>Temp: ${data.temperature}°C | Humidity: ${data.humidity}% | Wind: ${data.wind} m/s | Rain: ${data.rain} mm</p>
    `;
});

// Load Chart
fetch('/get-weather-chart-data/')
  .then(res => res.json())
  .then(data => {
    new Chart(document.getElementById('chart'), {
      type: 'line',
      data: {
        labels: data.labels,
        datasets: [
          {
            label: 'Temperature (°C)',
            data: data.temperature,
            borderColor: 'orange',
            fill: false,
          },
          {
            label: 'Humidity (%)',
            data: data.humidity,
            borderColor: 'blue',
            fill: false,
          }
        ]
      }
    });
  });

// Load Forecast
fetch('/get-weather-forecast/')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('forecast');
    container.innerHTML = data.forecast.map(day => `
      <div>
        <b>${day.day}</b> - 🌡 ${day.temp}°C | 💧 ${day.humidity}% | 🌬 ${day.wind} m/s | ☔ ${day.rain} mm
      </div>
    `).join('');
  });
