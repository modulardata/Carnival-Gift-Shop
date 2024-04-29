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
        console.log('\r');
    },
    chose: function () {
        console.log('What do you want to do?');
        let question = input(
            '1-Buy a gift 2-Add tickets 3-Check tickets 4-Show gifts\n'
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
                giftShop.showGifts();
                break;
            default:
                console.log('Unknown command!');
        } // switch
    },
    buy: function () {
        let question = input('Enter the number of the gift you want to get:');
        for (let i = 0; i < data['gifts_list'].length; i++) {

            if (parseInt(question) === parseInt(data['gifts_list'][i].id)) {
                let total = data['tickets'] - data['gifts_list'][i].price;
                console.log(
                    `Here you go, one ${data['gifts_list'][i].name}!`
                );
                console.log(`Total tickets: ${total + '\n'}Have a nice day!`);
                break;
            }
        }
    },
    addTickets: function () {
        let question = input('Enter the ticket amount: ');
        data['tickets'] += parseInt(question);
        console.log(`Total tickets: ${data['tickets'] + '\n'}Have a nice day!`);
    },
    checkTickets: function (amount) {
        console.log(`Total tickets: ${amount + '\n'}Have a nice day!`);
    },
    showGifts: function () {
        console.log('Here\'s the list of gifts:' + '\n');
        giftShop.showGiftsList();
        console.log('Have a nice day!');
    },
};

const __main__ = () => {
    giftShop.welcomeMessage();
    giftShop.showGiftsList();
    giftShop.chose();
};

__main__();
