const chartEl = document.getElementById("messageChart");
const labelsEl = document.getElementById("chart-labels");
const dataEl = document.getElementById("chart-data");

if (chartEl && labelsEl && dataEl) {
  const labels = JSON.parse(labelsEl.textContent || "[]");
  const data = JSON.parse(dataEl.textContent || "[]");
  const ctx = chartEl.getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "Messages",
          data,
          borderColor: "#5b8bff",
          backgroundColor: "rgba(91, 139, 255, 0.2)",
          tension: 0.35,
          fill: true,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: { ticks: { color: "#a6b0c3" }, grid: { display: false } },
        y: {
          ticks: { color: "#a6b0c3" },
          grid: { color: "rgba(255,255,255,0.06)" },
        },
      },
      plugins: {
        legend: { labels: { color: "#f5f7ff" } },
      },
    },
  });
}
