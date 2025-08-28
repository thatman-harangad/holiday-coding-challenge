let count = 0;

increment = document.getElementById("increment");
decrement = document.getElementById("decrement");
reset = document.getElementById("reset");
countDisplay = document.getElementById("count");

function updateCountDisplay() {
    countDisplay.textContent = count;
    document.title = `Counter: ${count}`;
    localStorage.setItem("count", count);
};

increment.addEventListener("click", function() {
    count++;
    updateCountDisplay();
});

decrement.addEventListener("click", function() {
    count--;
    updateCountDisplay();
});

reset.addEventListener("click", function() {
    count = 0;
    updateCountDisplay();
});