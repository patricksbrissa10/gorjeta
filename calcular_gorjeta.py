
def calcular_gorjeta():
    """
    Calcula a gorjeta e o valor total da conta de um restaurante.

    O programa solicita ao usuário o valor da conta e a porcentagem de gorjeta,
    garantindo que os dados sejam válidos (numéricos e não negativos).
    Exibe o valor da gorjeta e o total a pagar, e permite repetir o cálculo.
    """
    while True:
        try:
            conta = float(input('Digite o valor da conta: '))
            if conta < 0:
                print('❌ O valor da conta não pode ser negativo. Tente novamente.\n')
                continue
            break
        except ValueError:
            print('⚠️ Por favor, digite um número válido para o valor da conta.\n')

    while True:
        try:
            porcentagem = float(input('Digite a porcentagem da gorjeta: '))
            if porcentagem < 0:
                print('❌ O valor da gorjeta não pode ser negativo. Tente novamente.\n')
                continue
            break
        except ValueError:
            print('⚠️ Por favor, digite um número válido para a porcentagem da gorjeta.\n')

    gorjeta = conta * (porcentagem / 100)
    total = gorjeta + conta

    print('\n--- Resultado ---')
    print(f'💰 Valor da gorjeta: R$ {gorjeta:.2f}')
    print(f'🧾 Valor total da conta: R$ {total:.2f}')


def main():
    """
    Função principal que controla o fluxo do programa.
    Permite que o usuário faça novos cálculos até decidir sair.
    """
    while True:
        calcular_gorjeta()
        repetir = input('\nDeseja calcular outra gorjeta? (s/n): ').strip().lower()
        if repetir != 's':
            print('\n👋 Obrigado por usar o calculador de gorjeta!')
            break


if __name__ == "__main__":
    main()




