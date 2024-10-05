from typing import List
from time import sleep
import re

from models.client import Client
from models.account import Account

accounts: List[Account] = []

def main() -> None:
    while True:
        menu()

def validate_email(email: str) -> bool:
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False

def validate_birth_date(date_of_birth: str) -> bool:
    try:
        day, month, year = map(int, date_of_birth.split('-'))
        if day <= 31 and month <= 12 and len(str(year))==4:
            return True
    except:
        return False
    return False

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

def create_account() -> None:
    print('Please enter the client details: ')

    name: str = input('Client name: ')
    email: str = input('Client email: ')
    while not validate_email(email):
        print("Invalid email. Try again.")
        email = input('Client email: ')
  
    cpf: str = input('Client CPF: ')
  
    date_of_birth: str = input('Client date of birth: ')
    while not validate_birth_date(date_of_birth):
        print("Invalid Date of Birth. Try again.")
        date_of_birth = input('Client date of birth: ')

    client: Client = Client(name, email, cpf, date_of_birth)

    account: Account = Account(client)

    accounts.append(account)

    print('Account created successfully.')
    print('Account details: ')
    print('=====================================================')
    print(account)
    sleep(2)

def make_withdrawal() -> None:
    if len(accounts) > 0:
        number: str = input('Enter your account number: ')
        while not number.isdigit():
            print("Invalid account number. Try again.")
            number = input('Enter your account number: ')

        account: Account = find_account_by_number(int(number))

        if account:
            value: float = float(input('Enter the withdrawal amount: '))

            account.withdraw(value)
        else:
            print(f'No account found with number {number}')
    else:
        print('No accounts registered.')
    sleep(2)

def make_deposit() -> None:
    if len(accounts) > 0:
        number: str = input('Enter your account number: ')
        while not number.isdigit():
            print("Invalid account number. Try again.")
            number = input('Enter your account number: ')

        account: Account = find_account_by_number(int(number))

        if account:
            value: float = float(input('Enter the deposit amount: '))

            account.deposit(value)
        else:
            print(f'No account found with number {number}')
    else:
        print('No accounts registered.')
    sleep(2)

def make_transfer() -> None:
    if len(accounts) > 0:
        number_origin: str = input('Enter your account number: ')
        while not number_origin.isdigit():
            print("Invalid account number. Try again.")
            number_origin = input('Enter your account number: ')

        account_origin: Account = find_account_by_number(int(number_origin))

        if account_origin:
            number_destiny: str = input('Enter the destination account number: ')
            while not number_destiny.isdigit():
                print("Invalid destination account number. Try again.")
                number_destiny = input('Enter the destination account number: ')
                
            account_destiny: Account = find_account_by_number(int(number_destiny))

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

def find_account_by_number(number: int) -> Account:
    for acc in accounts:
        if acc.number == number:
            return acc
    return None

if __name__ == '__main__':
    main()
