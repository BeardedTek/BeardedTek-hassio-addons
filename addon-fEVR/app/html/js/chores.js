function toggleDisplay(querySelect,display){
    let myElements = document.querySelectorAll(querySelect);
    for (let i = 0; i < myElements.length; i++){
        myElements[i].style.display = display;
    }
}

function toggleDisabled(action){
    
    showButton = "<button onClick='toggleDisabled(\"show\")'>Show Disabled Chores</button>"
    hideButton = "<button onClick='toggleDisabled(\"hide\")'>Hide Disabled Chores</button>"
    if (action == "show"){
        toggleDisplay(".disabled","flex")
        document.querySelector("#toggleDisabled").innerHTML = hideButton;
    }
    else{
        toggleDisplay(".disabled","none")
        document.querySelector("#toggleDisabled").innerHTML = showButton;
    }
}

function toggleChoreList(action){
    showButton = "<button onClick='toggleChoreList(\"show\")'>Show Chore List</button>"
    hideButton = "<button onClick='toggleChoreList(\"hide\")'>Hide Chore List</button>"
    if (action == "show"){
        toggleDisplay("#chores","block")
        document.querySelector("#toggleChoreList").innerHTML = hideButton;
    }
    else{
        toggleDisplay("#chores","none")
        document.querySelector("#toggleChoreList").innerHTML = showButton;
    }
}

function toggleWho(){
    who = document.getElementById('who')
    if (who.clientHeight < 100){
        who.style = "height: 240px;"
    }
    else{
        who.style = "height: 40px;"
    }
}

function toggleChores(){
    chores = document.getElementById('chores')
    toggle = document.getElementById('toggleChores')
    if (chores.clientHeight > 100){
        chores.style = ""
        toggle.style = ""
    }
    else{
        chores.style= "height: auto; width: 800px; padding: 10px;";
        toggle.style = "text-align: right; left:629px;";
    }
}