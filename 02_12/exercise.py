import random


class CommandPrompt:
    def __init__(self, buy_commands, sell_commands, wait_commands):
        self.buy_commands = buy_commands
        self.sell_commands = sell_commands
        self.wait_commands = wait_commands

    def ask(self):
        while True:
            decision = input('Decision: ')
            if decision in self.buy_commands:
                return 'buy'
            elif decision in self.sell_commands:
                return 'sell'
            elif decision in self.wait_commands:
                return 'wait'
            else:
                print('Invalid choice!')


prompt = CommandPrompt(['b', 'buy'], ['s', 'sell'], ['w', 'wait', ''])


class Wallet:
    def __init__(self, pln, usd):
        self.pln = pln
        self.usd = usd

    def convert_usd_to_pln(self, usdpln_rate):
        self.pln += self.usd * usdpln_rate
        self.usd = 0.0

    def convert_pln_to_usd(self, usdpln_rate):
        self.usd += self.pln / usdpln_rate
        self.pln = 0.0


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


def main(usdpln_rates):
    wallet = Wallet(100.0, 0.0)

    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(wallet.pln, 2)} PLN, ${round(wallet.usd, 2)}, rate {usdpln_rate}')
        choice = prompt.ask()
        if choice == 'buy':
            wallet.convert_pln_to_usd(usdpln_rate)
        elif choice == 'sell':
            wallet.convert_usd_to_pln(usdpln_rate)

    wallet.convert_usd_to_pln(usdpln_rate)
    print(f'Your result: {wallet.pln} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)