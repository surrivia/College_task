// The programme will Ask user for favorite car name and a number, then print the car name that many times
let carName = prompt("Enter your favorite car name: ");
let numberOfTimes = parseInt(prompt("How many times do you want to print the car name? "));

for (let i = 0; i < numberOfTimes; i++) {
    console.log(carName);
}