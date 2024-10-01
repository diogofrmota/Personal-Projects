from models.client import Client
from utils.helper import format_float_to_currency

class Account:

    code_counter: int = 1001

    def __init__(self, client: Client) -> None:
        self.__number: int = Account.code_counter
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self.calculate_total_balance()
        Account.code_counter += 1

    @property
    def number(self) -> int:
        return self.__number

    @property
    def client(self) -> Client:
        return self.__client

    @property
    def balance(self) -> float:
        return self.__balance

    def calculate_total_balance(self) -> float:
        return self.__balance + self.__limit

    @property
    def total_balance(self) -> float:
        return self.calculate_total_balance()

    @balance.setter
    def balance(self, amount: float) -> None:
        self.__balance = amount

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print('Deposit made successfully!')
        else:
            print('Error making the deposit. Please try again.')

    def withdraw(self, amount: float) -> None:
        if amount > 0 and self.total_balance >= amount:
            if self.__balance >= amount:
                self.balance -= amount
            else:
                rest: float = self.__balance - amount
                self.balance = 0
                self.__limit += rest
            print('Withdrawal made successfully!')
        else:
            print('Not enough balance. Please try again.')

    def transfer(self, destination, amount: float) -> None:
        if amount > 0 and self.total_balance >= amount:
            self.withdraw(amount)
            destination.deposit(amount)
            print('Transfer made successfully!')
        else:
            print('Not enough balance to make the transfer. Please try again.')

    def __str__(self) -> str:
        return (f'Account Number: {self.number} \n'
                f'Client: {self.client.name} \n'
                f'Total Balance: {format_float_to_currency(self.total_balance)}')
