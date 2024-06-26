from hstest import StageTest, CheckResult, dynamic_test, TestedProgram


class Gift:
    def __init__(self, name, price, _id):
        self.name = name
        self.price = price
        self.id = _id


class Feedback:
    missing_input = 'Your program is missing the input message '
    waiting_input = 'Your program is not waiting for input '
    check_eg = ' Check the example!'
    missing_ending = 'Your program is missing the correct ending message.' + check_eg
    test1 = "Your output should be like in the example!"
    test2 = {
        "missing_input": missing_input + 'which the user decides what to do.' + check_eg,
        "waiting_input": waiting_input + 'which the user decides what to do.',
    }
    test3 = {
        "missing_input": missing_input + 'which the user enters the gift number.' + check_eg,
        "waiting_input": waiting_input + 'which the user enters the gift number.',
        "buy_gift": "Your program couldn't process all of the gift numbers correctly!"
                    " Make sure you have all of the gifts defined in the gift list!",
    }
    test4 = {
        "missing_input": missing_input + 'which the user enters the ticket amount.' + check_eg,
        "waiting_input": waiting_input + 'which the user enters the ticket amount.',
        "add_tickets": "Your program couldn't process all of the ticket amounts correctly!"
    }
    test5 = "Your program couldn't output the total tickets correctly!" \
            "The starting total tickets should be 100 in this stage!"
    test6 = "Your program couldn't output the gift list again correctly!" \
            "The gift list should be the same as in the example!"
    test7 = "Your program should end after the user decides to quit!"
    test8 = "Your program should ask for what to do again, after processing an operation!"
    test9 = "Your program couldn't output the total tickets correctly!" \
            "The starting total tickets should be 0 in this stage!"
    test10 = "Your program should remove the gift from the list after the user buys it!"

class CarnivalGiftShopTest(StageTest):
    welcome_msg = "WELCOME TO THE CARNIVAL GIFT SHOP!"
    greet_msg = "Hello friend! Thank you for visiting the carnival!"
    gift_list = """Here's the list of gifts:\n
1- Teddy Bear, Cost: 10 tickets
2- Big Red Ball, Cost: 5 tickets
3- Huge Bear, Cost: 50 tickets
4- Candy, Cost: 8 tickets
5- Stuffed Tiger, Cost: 15 tickets
6- Stuffed Dragon, Cost: 30 tickets
7- Skateboard, Cost: 100 tickets
8- Toy Car, Cost: 25 tickets
9- Basketball, Cost: 20 tickets
10- Scary Mask, Cost: 75 tickets"""
    do_what_input_msg = "\nWhat do you want to do?\n1-Buy a gift 2-Add tickets " \
                        "3-Check tickets 4-Show gifts 5-Exit the shop\n"
    gift_id_input_msg = "Enter the number of the gift you want to get: "
    ticket_amount_input_msg = "Enter the ticket amount: "
    end_msg = "Have a nice day!"
    tickets = 0
    gift_ids = list(range(1, 11))
    gifts = [
        Gift("Teddy Bear", 10, 1),
        Gift("Big Red Ball", 5, 2),
        Gift("Huge Bear", 50, 3),
        Gift("Candy", 8, 4),
        Gift("Stuffed Tiger", 15, 5),
        Gift("Stuffed Dragon", 30, 6),
        Gift("Skateboard", 100, 7),
        Gift("Toy Car", 25, 8),
        Gift("Basketball", 20, 9),
        Gift("Scary Mask", 75, 10)
    ]
    ticket_amounts = [100, 50, 1000, 500, 5, 1]
    options = [1, 2, 3, 4]

    @classmethod
    def show_tickets(cls, tickets):
        return f"Total tickets: {tickets}"

    @classmethod
    def buy_gift(cls, gift_id, add_tickets=0):
        tickets = cls.tickets + add_tickets
        gift = list(filter(lambda item: item.id == gift_id, cls.gifts))[0]
        gift_msg = "Here you go, one " + gift.name + "!"
        cls.gifts.remove(gift)
        tickets -= gift.price
        tickets_msg = cls.show_tickets(tickets)
        return gift_msg + "\n" + tickets_msg

    @classmethod
    def add_tickets(cls, ticket_amount):
        tickets = cls.tickets
        tickets += ticket_amount
        tickets_msg = cls.show_tickets(tickets)
        return tickets_msg

    @classmethod
    def show_gifts(cls):
        gifts_msg = "Here's the list of gifts:\n\n"
        for gift in cls.gifts:
            gifts_msg += f"{gift.id}- {gift.name}, Cost: {gift.price} tickets\n"
        print(gifts_msg)
        return gifts_msg

    @classmethod
    def reinit_gifts(cls):
        cls.gifts = [
            Gift("Teddy Bear", 10, 1),
            Gift("Big Red Ball", 5, 2),
            Gift("Huge Bear", 50, 3),
            Gift("Candy", 8, 4),
            Gift("Stuffed Tiger", 15, 5),
            Gift("Stuffed Dragon", 30, 6),
            Gift("Skateboard", 100, 7),
            Gift("Toy Car", 25, 8),
            Gift("Basketball", 20, 9),
            Gift("Scary Mask", 75, 10)
        ]

    # test if the output is correct
    @dynamic_test
    def test1(self):
        main = TestedProgram(self.source_name)
        output = main.start()
        message = f"{self.welcome_msg}\n{self.greet_msg}\n{self.gift_list}"
        if message.strip() not in output.strip():
            return CheckResult.wrong(Feedback.test1)
        return CheckResult.correct()

    # test if the do what input is correct
    @dynamic_test
    def test2(self):
        main = TestedProgram(self.source_name)
        output = main.start()
        message = self.do_what_input_msg
        if main.is_waiting_input():
            if message.strip() not in output.strip():
                return CheckResult.wrong(Feedback.test2["missing_input"])
            return CheckResult.correct()
        return CheckResult.wrong(Feedback.test2["waiting_input"])

    # test if option 1 is working
    @dynamic_test(data=gift_ids)
    def test3(self, gift_id):
        main = TestedProgram(self.source_name)
        main.start()
        self.reinit_gifts()
        message = self.gift_id_input_msg
        output = main.execute("1")
        if message.strip() not in output.strip():
            return CheckResult.wrong(Feedback.test3["missing_input"])
        if main.is_waiting_input():
            output = main.execute(str(gift_id))
            if self.buy_gift(gift_id).strip() not in output.strip():
                return CheckResult.wrong(Feedback.test3["buy_gift"])
            return CheckResult.correct()
        return CheckResult.wrong(Feedback.test3["waiting_input"])

    # test if option 2 is working
    @dynamic_test(data=ticket_amounts)
    def test4(self, ticket_amount):
        main = TestedProgram(self.source_name)
        main.start()
        message = self.ticket_amount_input_msg
        output = main.execute("2")
        if message.strip() not in output.strip():
            return CheckResult.wrong(Feedback.test4["missing_input"])
        if main.is_waiting_input():
            output = main.execute(str(ticket_amount))
            if self.add_tickets(ticket_amount).strip() not in output.strip():
                return CheckResult.wrong(Feedback.test4["add_tickets"])
            return CheckResult.correct()
        return CheckResult.wrong(Feedback.test4["waiting_input"])

    # test if option 3 is working
    @dynamic_test
    def test5(self):
        main = TestedProgram(self.source_name)
        main.start()
        output = main.execute("3")
        if self.show_tickets(self.tickets).strip() not in output.strip():
            return CheckResult.wrong(Feedback.test5)
        return CheckResult.correct()

    # test if option 4 is working
    @dynamic_test
    def test6(self):
        main = TestedProgram(self.source_name)
        main.start()
        output = main.execute("4")
        if self.gift_list.strip() not in output.strip():
            return CheckResult.wrong(Feedback.test6)
        return CheckResult.correct()

    # test if option 5 is working
    @dynamic_test
    def test7(self):
        main = TestedProgram(self.source_name)
        main.start()
        output = main.execute("5")
        if self.end_msg.strip() not in output.strip():
            return CheckResult.wrong(Feedback.missing_ending)
        elif not main.is_finished():
            return CheckResult.wrong(Feedback.test7)
        return CheckResult.correct()

    # test if the program runs continuously
    @dynamic_test
    def test8(self):
        main = TestedProgram(self.source_name)
        main.start()
        main.execute("2")
        output = main.execute("100")
        message = self.do_what_input_msg
        if message.strip() not in output.strip() or not main.is_waiting_input():
            return CheckResult.wrong(Feedback.test8)
        main.execute("1")
        output = main.execute("6")
        if message.strip() not in output.strip() or not main.is_waiting_input():
            return CheckResult.wrong(Feedback.test8)
        output = main.execute("4")
        if message.strip() not in output.strip() or not main.is_waiting_input():
            return CheckResult.wrong(Feedback.test8)
        output = main.execute("3")
        if message.strip() not in output.strip() or not main.is_waiting_input():
            return CheckResult.wrong(Feedback.test8)
        main.execute("5")
        return CheckResult.correct()

    # test if starting tickets are zero
    @dynamic_test
    def test9(self):
        main = TestedProgram(self.source_name)
        main.start()
        output = main.execute("3")
        if self.show_tickets(self.tickets).strip() not in output.strip():
            return CheckResult.wrong(Feedback.test9)
        return CheckResult.correct()

    # test if the program removes the bought gift
    @dynamic_test(data=gift_ids)
    def test10(self, gift_id):
        main = TestedProgram(self.source_name)
        main.start()
        self.reinit_gifts()
        main.execute("2")
        main.execute("100")
        main.execute("1")
        main.execute(str(gift_id))
        self.buy_gift(gift_id, 100)
        output = main.execute("4")
        if self.show_gifts() not in output.strip():
            return CheckResult.wrong(Feedback.test10)
        return CheckResult.correct()


if __name__ == '__main__':
    CarnivalGiftShopTest('main').run_tests()
