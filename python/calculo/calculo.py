from models.conta import Conta

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            
def get_difficulty_level() -> int:
    return get_integer_input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: ')

def get_continue_option() -> int:
    return get_integer_input('Deseja continuar no jogo? [1 - sim, 0 não]: ')

def play_game(pontos: int) -> None:
    difficulty = get_difficulty_level()
    calc: Conta = Conta(difficulty)

    print('Informe o resultado para a seguinte operação: ')
    calc._mostrar_operacao()

    result: int = get_integer_input()
    
    if calc.checar_resultado(result):
        pontos += 1
        print(f'Tem {pontos} ponto(s).')

    if get_continue_option() == 1:
        play_game(pontos)
    else:
        print(f'Finalizou com {pontos} ponto(s).')
        print('Até à próxima!')

def main() -> None:
    pontos: int = 0
    play_game(pontos)

if __name__ == '__main__':
    main()
