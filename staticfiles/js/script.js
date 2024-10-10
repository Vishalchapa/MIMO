document.addEventListener('DOMContentLoaded', function() {
    const createTask = document.getElementById('createTaskForm')
    const createTaskBtn = document.getElementById('create-task-btn')
    createTaskBtn.addEventListener('click', function(){
           createTask.style.display = 'block';
        })
    }
);