from datetime import date
from utils.helper import date_para_str, str_para_date

class Cliente:
    # Contador que mantém o controle de quantos clientes foram criados, começando em 101
    contador: int = 101

    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        """
        Método construtor da classe Cliente. Inicializa um objeto Cliente com nome, email, cpf e data de nascimento.
        O código do cliente é gerado automaticamente e a data de cadastro é definida como a data atual.
        """
        self.__codigo: int = Cliente.contador  # Atribui o valor atual do contador ao código do cliente
        self.__nome: str = nome                # Define o nome do cliente
        self.__email: str = email              # Define o email do cliente
        self.__cpf: str = cpf                  # Define o CPF do cliente
        self.__data_nascimento: date = str_para_date(data_nascimento)  # Converte a data de nascimento (str) para date
        self.__data_cadastro: date = date.today()  # Define a data de cadastro como a data atual
        Cliente.contador += 1  # Incrementa o contador para o próximo cliente

    @property
    def codigo(self) -> int:
        """
        Retorna o código do cliente.
        """
        return self.__codigo

    @property
    def nome(self) -> str:
        """
        Retorna o nome do cliente.
        """
        return self.__nome

    @property
    def email(self) -> str:
        """
        Retorna o email do cliente.
        """
        return self.__email

    @property
    def cpf(self) -> str:
        """
        Retorna o CPF do cliente.
        """
        return self.__cpf

    @property
    def data_nascimento(self) -> str:
        """
        Retorna a data de nascimento do cliente, formatada como string.
        """
        return date_para_str(self.__data_nascimento)  # Converte a data para string usando a função auxiliar

    @property
    def data_cadastro(self) -> str:
        """
        Retorna a data de cadastro do cliente, formatada como string.
        """
        return date_para_str(self.__data_cadastro)  # Converte a data de cadastro para string

    def __str__(self) -> str:
        """
        Retorna uma representação textual do cliente, incluindo código, nome, email, CPF,
        data de nascimento e data de cadastro.
        """
        return (f'Código: {self.codigo} \nNome: {self.nome} \nEmail: {self.email} \nCPF: {self.cpf} '
                f'\nData de Nascimento: {self.data_nascimento} \nCadastro: {self.data_cadastro}')