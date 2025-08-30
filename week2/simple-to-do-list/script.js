let tasks = [];
let task = '';

function getNewTask(){
    task = document.getElementById("new-task").value;
    return task;
}

function addTask(task) {
    tasks.push(task);
}

function displayTasks() {
    const taskList = document.getElementById("task-list");
    taskList.innerHTML = "";
    tasks.forEach((task, index) => {
        const li = document.createElement("li");
        li.textContent = task;
        taskList.appendChild(li);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    displayTasks();
});

document.getElementById("add-task").addEventListener("click", function() {
    const newTask = getNewTask();
    if (newTask) {
        addTask(newTask);
        displayTasks();
        document.getElementById("new-task").value = '';
    }
});