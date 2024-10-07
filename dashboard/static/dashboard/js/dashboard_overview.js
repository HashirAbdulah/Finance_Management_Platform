document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('expenseChart').getContext('2d');

    // Ensure projectsData is defined
    if (typeof projectsData !== 'undefined' && projectsData.labels && projectsData.expenses) {
        var expenseChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: projectsData.labels,
                datasets: [{
                    label: 'Expenses',
                    data: projectsData.expenses,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } else {
        console.error('projectsData is undefined or missing properties.');
    }
});
