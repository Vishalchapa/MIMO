document.addEventListener('DOMContentLoaded', function() {
    const createTaskBtn = document.getElementById('create-task-btn')
    const createTask = document.getElementById('createTaskForm')
    const editButtons = document.getElementsByClassName("btn-edit");
    const submitButton = document.getElementById("submitButton");

    if (createTaskBtn && createTask) { // Check if elements exist
        createTaskBtn.addEventListener('click', function() {
            createTask.style.display = 'block';
            this.style.display = 'none'; // Hide the button when clicked
        });
    }

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let taskId = e.target.getAttribute("task_id");
            let taskContent = document.getElementById(`task${taskId}`).innerText;
            taskTitle.value = taskContent;
            submitButton.innerText = "Update";
            taskForm.setAttribute("action", `edit_task/${taskId}`);
        });
    };

    const tables = document.querySelectorAll('.tasks-table');

    
    tables.forEach(table => {
        
        const sortableHeaders = table.querySelectorAll('.sortable');

        sortableHeaders.forEach(header => {
        
            header.addEventListener('click', function() {
                
                const tbody = table.querySelector('tbody');
                const rows = Array.from(tbody.querySelectorAll('tr'));
                const sortBy = this.dataset.sort;
                const isAscending = !this.classList.contains('asc');


                rows.sort(function(rowA, rowB) {
                    let valueA, valueB;

                    const cellA = rowA.querySelector(`td:nth-child(${Array.from(header.parentNode.children).indexOf(header) + 1})`);
                    const cellB = rowB.querySelector(`td:nth-child(${Array.from(header.parentNode.children).indexOf(header) + 1})`);

                    if (sortBy === 'priority') {
                        // For priority, use a custom order
                        const priorityOrder = {'High': 3, 'Normal': 2, 'Low': 1};
                        const cellA = rowA.querySelector('td:nth-child(3)');
                        const cellB = rowB.querySelector('td:nth-child(3)');
                        
                        
                        valueA = cellA.querySelector('select') ? 
                            priorityOrder[cellA.querySelector('select').value] : 
                            priorityOrder[cellA.textContent.trim()];
                        valueB = cellB.querySelector('select') ? 
                            priorityOrder[cellB.querySelector('select').value] : 
                            priorityOrder[cellB.textContent.trim()];
                    } else if (sortBy === 'status') {
                        // For status, use the numeric value
                        valueA = parseInt(cellA.querySelector('select') ? cellA.querySelector('select').value : cellA.textContent.trim());
                        valueB = parseInt(cellB.querySelector('select') ? cellB.querySelector('select').value : cellB.textContent.trim());
                    } else if (sortBy === 'due_day') {
                        // For due date, convert to Date objects
                        valueA = new Date(cellA.textContent.trim());
                        valueB = new Date(cellB.textContent.trim());
                    } else {
                        // For other columns, use text content
                        valueA = cellA.textContent.trim().toLowerCase();
                        valueB = cellB.textContent.trim().toLowerCase();
                    }

                    // Compare the values
                    if (valueA < valueB) return isAscending ? -1 : 1;
                    if (valueA > valueB) return isAscending ? 1 : -1;
                    return 0;
                });

                // Rearrange the rows in the table
                rows.forEach(row => tbody.appendChild(row));

                // Update the sorting indicators
                sortableHeaders.forEach(h => h.classList.remove('asc', 'desc'));
                this.classList.toggle('asc', isAscending);
                this.classList.toggle('desc', !isAscending);
            });
        });
    });
});
