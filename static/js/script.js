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
    }
});