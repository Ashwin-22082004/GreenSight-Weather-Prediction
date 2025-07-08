document.getElementById("predictionForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    const form = e.target;
    const data = {
      temperature: parseFloat(form.temperature.value),
      humidity: parseFloat(form.humidity.value),
      co2: parseFloat(form.co2.value)
    };
  
    const res = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
  
    const result = await res.json();
    document.getElementById("result").textContent = "Prediction: " + result.prediction;
  });
  