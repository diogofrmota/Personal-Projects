from typing import List
from time import sleep

from models.client import Client
from models.account import Account


accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=====================================================')
    print('=================== ATM SYSTEM ======================')
    print('================= Diogo’s Bank ======================')
    print('=====================================================')

    print('Select an option from the menu: ')
    print('1 - Create account')
    print('2 - Make withdrawal')
    print('3 - Make deposit')
    print('4 - Make transfer')
    print('5 - List accounts')
    print('6 - Exit system')

    option: int = int(input())

    if option == 1:
        create_account()
    elif option == 2:
        make_withdrawal()
    elif option == 3:
        make_deposit()
    elif option == 4:
        make_transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('Thank you for visiting.')
        sleep(2)
        exit(0)
    else:
        print('Invalid option')
        sleep(2)
        menu()


def create_account() -> None:
    print('Please enter the client details: ')

    name: str = input('Client name: ')
    email: str = input('Client email: ')
    cpf: str = input('Client CPF: ')
    date_of_birth: str = input('Client date of birth: ')

    client: Client = Client(name, email, cpf, date_of_birth)

    account: Account = Account(client)

    accounts.append(account)

    print('Account created successfully.')
    print('Account details: ')
    print('=====================================================')
    print(account)
    sleep(2)
    menu()


def make_withdrawal() -> None:
    if len(accounts) > 0:
        number: int = int(input('Enter your account number: '))

        account: Account = find_account_by_number(number)

        if account:
            value: float = float(input('Enter the withdrawal amount: '))

            account.withdraw(value)
        else:
            print(f'No account found with number {number}')
    else:
        print('No accounts registered.')
    sleep(2)
    menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        number: int = int(input('Enter your account number: '))

        account: Account = find_account_by_number(number)

        if account:
            value: float = float(input('Enter the deposit amount: '))

            account.deposit(value)
        else:
            print(f'No account found with number {number}')
    else:
        print('No accounts registered.')
    sleep(2)
    menu()


def make_transfer() -> None:
    if len(accounts) > 0:
        number_origin: int = int(input('Enter your account number: '))

        account_origin: Account = find_account_by_number(number_origin)

        if account_origin:
            number_destiny: int = int(input('Enter the destination account number: '))
            
            account_destiny: Account = find_account_by_number(number_destiny)

            if account_destiny:
                value: float = float(input('Enter the transfer amount: '))

                account_origin.transfer(account_destiny, value)
            else:
                print(f'Destination account {number_destiny} not found.')
        else:
            print(f'Your account with number {number_origin} not found.')
    else:
        print('No accounts registered.')
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print('Listing of accounts')
        
        for acc in accounts:
            print(acc)
            print('=====================================================')
            sleep(1)
    else:
        print('No accounts registered.')
    sleep(2)
    menu()


def find_account_by_number(number: int) -> Account:
    for acc in accounts:
        if acc.number == number:
            return acc
    return None


if __name__ == '__main__':
    main()
