const input = require('sync-input');
const data = require('./gift_shop_data.json');

const giftShop = {
    welcomeMessage: function () {
        for (let i = 0; i < data['welcome_message'].length; i++) {
            console.log(data['welcome_message'][i]);
        }
        console.log('\r');
    },
    showGiftsList: function () {
        for (let i = 0; i < data['gifts_list'].length; i++) {
            console.log(
                `${data['gifts_list'][i].id}- ${data['gifts_list'][i].name}, Cost: ${data['gifts_list'][i].price} tickets`
            );
        }
        console.log();
    },
    chose: function () {
        console.log('What do you want to do?');
        let question = input(
            '1-Buy a gift 2-Add tickets 3-Check tickets 4-Show gifts 5-Exit the shop\n'
        );
        switch (question) {
            case '1':
                giftShop.buy();
                break;
            case '2':
                giftShop.addTickets();
                break;
            case '3':
                giftShop.checkTickets(data['tickets']);
                break;
            case '4':
                giftShop.showGiftsList();
                break;
            case '5':
                giftShop.out();
                break;
            default:
                console.log('Please enter a valid number!\n');
                giftShop.chose();
        } // switch
    },
    buy: function () {
        if (data['gifts_list'].length === 0) {
            console.log("Wow! There are no gifts to buy.");
            console.log();
            giftShop.chose();
            return;
        }

        const question = input('Enter the number of the gift you want to get: ');
        if (isNaN(question) || question.trim() === '') {
            console.log('Please enter a valid number!');
            console.log();
            giftShop.chose();
            return;
        }

        const giftNumber = parseInt(question);
        const gift = data['gifts_list'].find(g => g.id === giftNumber);

        if (!gift) {
            console.log('There is no gift with that number!');
            console.log();
            giftShop.chose();
            return;
        }

        if (data['tickets'] >= gift.price) {
            let total = data['tickets'] - gift.price;
            console.log(`Here you go, one ${gift.name}!`);
            console.log(`Total tickets: ${total}`);
            data['tickets'] = total;
            data['gifts_list'] = data['gifts_list'].filter(g => g.id !== gift.id);
        } else {
            console.log("You don't have enough tickets to buy this gift.");
        }

        console.log(`Total tickets: ${data['tickets']}`);
        console.log();
        giftShop.chose();
    },
    addTickets: function () {
        let question = input('Enter the ticket amount: ');
        if (isNaN(question) || question.trim() === '' || parseInt(question) < 0 || parseInt(question) > 1000) {
            console.log('Please enter a valid number between 0 and 1000.');
            console.log();
            giftShop.chose();
            return;
        }

        let amount = parseInt(question);
        data['tickets'] += amount;
        console.log(`Total tickets: ${data['tickets']}`);
        console.log();
        giftShop.chose();
    },
    checkTickets: function (amount) {
        console.log(`Total tickets: ${amount}`);
        console.log();
        giftShop.chose();
    },
    out: function () {
        console.log('Have a nice day!');
        process.exit(0);
    }
};

const __main__ = () => {
    do {
        giftShop.welcomeMessage();
        giftShop.showGiftsList();
        giftShop.chose();
    } while (true);
};

__main__();