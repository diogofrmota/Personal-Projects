from datetime import date
from utils.helper import date_to_str, str_to_date

class Client:
    counter: int = 101

    def __init__(self, name: str, email: str, cpf: str, date_of_birth: str) -> None:
        self.__code: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__date_of_birth: date = str_to_date(date_of_birth)
        self.__registration_date: date = date.today()
        Client.counter += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def date_of_birth(self) -> str:
        return date_to_str(self.__date_of_birth)

    @property
    def registration_date(self) -> str:
        return date_to_str(self.__registration_date)

    def __str__(self) -> str:
        return (f'Code: {self.code} \n'
                f'Name: {self.name} \n'
                f'Email: {self.email} \n'
                f'CPF: {self.cpf} \n'
                f'Date of Birth: {self.date_of_birth} \n'
                f'Registration Date: {self.registration_date}')
