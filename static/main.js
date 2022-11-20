// Select increment and decrement buttons
const incrementCount = document.getElementById("increment-count");
const decrementCount = document.getElementById("decrement-count");

// Select total count
const totalCount = document.getElementById("total-count");

// Variable to track count
var count = 0;

// Display initial count value
if(totalCount){
totalCount.innerHTML = count;
}
// Function to increment count
const handleIncrement = () => {
  count++;
  totalCount.innerHTML = count;


  var newr = count;
  localStorage.setItem("newr", newr);
};

// Function to decrement count
const handleDecrement = () => {
  count--;
  totalCount.innerHTML = count;

  var newr = count;
  localStorage.setItem("newr", newr);
};

// Add click event to buttons
if(incrementCount ||decrementCount){
  incrementCount.addEventListener("click", handleIncrement);
  decrementCount.addEventListener("click", handleDecrement);
}

