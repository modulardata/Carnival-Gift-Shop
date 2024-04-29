const welcomeText = [
    "WELCOME TO THE CARNIVAL GIFT SHOP!",
    "Hello friend! Thank you for visiting the carnival!",
    "Here's the list of gifts:"
];

const gifts = [
    { name: "Teddy Bear", price: 10, id: 1 },
    { name: "Big Red Ball", price: 5, id: 2 },
    { name: "Huge Bear", price: 50, id: 3 },
    { name: "Candy", price: 8, id: 4 },
    { name: "Stuffed Tiger", price: 15, id: 5 },
    { name: "Stuffed Dragon", price: 30, id: 6 },
    { name: "Skateboard", price: 100, id: 7 },
    { name: "Toy Car", price: 25, id: 8 },
    { name: "Basketball", price: 20, id: 9 },
    { name: "Scary Mask", price: 75, id: 10 }
];

function logWelcomeText() {
    welcomeText.forEach((sentence, index) => {
        console.log(`${sentence}`);
    });
}

function logGifts() {
    gifts.forEach((gift, index) => {
        console.log(`${index + 1}- ${gift.name}, Cost: ${gift.price} tickets`);
    });
}

logWelcomeText();
console.log('\r');
logGifts();