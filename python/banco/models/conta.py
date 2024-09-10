from models.cliente import Cliente
from utils.helper import formata_float_str_moeda

class Conta:

    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self.__calcula_saldo_total
        Conta.codigo += 1


    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} \nSaldo Total: {formata_float_str_moeda(self.saldo_total)}'
    

    @property
    def numero(self: object) -> int:
        return self.__numero
    

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente
    
    @property
    def saldo(self: object) -> float:
        return self.__saldo
    
    @property
    def limite(self: object) -> float:
        return self.__limite
    

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total