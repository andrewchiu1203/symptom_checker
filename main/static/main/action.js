function process(){
    let form = document.getElementById("form");
    let btn = document.getElementById("btn");
    let output = document.getElementById("output");

    btn.style.color = "rgba(0, 0, 0, 0)";
    btn.disabled = true;

    HTMLFormElement.prototype.submit.call(form);

    output.innerHTML = "Processing..."
}