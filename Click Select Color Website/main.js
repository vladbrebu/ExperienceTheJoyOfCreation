let target = document.getElementById("target");

let btn = document.getElementById("test-button");

// btn.addEventListener("click",changeColor);

// function changeColor(){
//     let selection = prompt("Select a color");
//     target.style.backgroundColor = selection;
// }

btn.addEventListener("click", () => {
    response = prompt("Type a color")
    target.style.backgroundColor = response;
})