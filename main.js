var listItems = document.getElementById("toDoList");
listItems.addEventListener("click", deleteItem);

function deleteItem(item) {
    item.target.style.display = "none";
}

function newTask() {
    var text = document.getElementById("enter");
    if (text.value == "")
        alert("Give an entry");
    else {
        var entry = document.createElement("li");
        var listItems = document.getElementById("toDoList");
        listItems.appendChild(entry);
        entry.innerHTML = text.value;
        document.getElementById("enter").value = "";
    }
}

function instructions() {
    alert("Enter task and press Add a Task to enter a new task.\nClick on the task itself to delete it.");
}
