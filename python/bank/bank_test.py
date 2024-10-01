from models.client import Client
from models.account import Account

felicity: Client = Client('Felicity Jones', 'felicity@gmail.com', '123.456.789-01', '02/09/1987')
angelina: Client = Client('Angelina Jolie', 'angelinay@gmail.com', '234.567.890-02', '08/07/1978')

account_f: Account = Account(felicity)
account_a: Account = Account(angelina)

print(account_f)
print(account_a)
