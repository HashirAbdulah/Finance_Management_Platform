document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('projectExpenseChart').getContext('2d');

    // Use the projectData object passed from the HTML template
    const projectExpenseChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: projectData.labels,  // Labels from Django context
            datasets: [{
                label: 'Expenses',
                data: projectData.expenses,  // Expense data from Django context
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
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
});
