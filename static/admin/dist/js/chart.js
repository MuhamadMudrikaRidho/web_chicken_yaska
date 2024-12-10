$(document).ready(function () {
  // Fetch data for the bar chart (previously for donut)
  $.ajax({
    url: '/admin/sales-chart-data',
    method: 'GET',
    success: function (chartData) {
      var barChartCanvas = $('#barChart').get(0).getContext('2d');
      var barChartData = {
        labels: chartData.labels,
        datasets: [
          {
            label: 'Sales by Menu',
            backgroundColor: [
              '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5',
              '#F5FF33', '#A133FF', '#FF8C33', '#33FF8C', '#8C33FF',
              '#FFD633', '#33FFD6', '#FF3333', '#33A1FF', '#FF33D6',
              '#D633FF', '#33FF33', '#33FFB5', '#FFB533', '#B533FF'
            ],
            data: chartData.data
          }
        ]
      };
      var barChartOptions = {
        legend: {
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      };

      // Render Bar Chart
      new Chart(barChartCanvas, {
        type: 'bar',
        data: barChartData,
        options: barChartOptions
      });
    },
    error: function (xhr, status, error) {
      console.error('Failed to fetch chart data:', error);
    }
  });

  // Fetch data for the donut chart (previously for bar)
  $.ajax({
    url: '/admin/bar-chart-data',
    method: 'GET',
    success: function (chartData) {
      var donutChartCanvas = $('#donutChart').get(0).getContext('2d');
      var donutData = {
        labels: chartData.labels,
        datasets: [
          {
            data: chartData.data,
            backgroundColor: [
              '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5',
              '#F5FF33', '#A133FF', '#FF8C33', '#33FF8C', '#8C33FF',
              '#FFD633', '#33FFD6', '#FF3333', '#33A1FF', '#FF33D6',
              '#D633FF', '#33FF33', '#33FFB5', '#FFB533', '#B533FF'
            ]
          }
        ]
      };
      var donutOptions = {
        legend: {
          display: true
        },
        maintainAspectRatio: false,
        responsive: true
      };

      // Render Donut Chart
      new Chart(donutChartCanvas, {
        type: 'doughnut',
        data: donutData,
        options: donutOptions
      });
    },
    error: function (xhr, status, error) {
      console.error('Failed to fetch chart data:', error);
    }
  });
});
