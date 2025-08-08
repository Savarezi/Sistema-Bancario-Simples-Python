"""
Sistema bancário simples - V1
Operações: depósito, saque e extrato
Regras:
- Depósito: somente valores positivos. Cada depósito é registrado.
- Saque: máximo 3 saques por execução (dia), limite de R$ 500,00 por saque, não permite saque sem saldo suficiente.
- Extrato: lista todas as operações e mostra o saldo atual no formato R$ xxx,xx
"""

def format_brl(valor: float) -> str:
    """Formata número para R$ xxx.xxx,xx (padrão brasileiro)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def menu():
    print("\n=== Banco Python - Menu ===")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")
    return input("Escolha uma opcao: ").strip().lower()

def main():
    saldo = 0.0
    extrato = []  # lista de strings descrevendo cada operação
    limite_saque = 500.00
    saques_realizados = 0
    limite_saques_diarios = 3

    while True:
        opc = menu()

        if opc == 'd':
            try:
                valor = float(input("Valor do depósito: ").replace(",", "."))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            if valor <= 0:
                print("Operação falhou: somente valores positivos são aceitos para depósito.")
            else:
                saldo += valor
                extrato.append(f"Depósito: +{format_brl(valor)}")
                print(f"Depósito realizado com sucesso. Saldo atual: {format_brl(saldo)}")

        elif opc == 's':
            if saques_realizados >= limite_saques_diarios:
                print(f"Operação falhou: número máximo de saques diários ({limite_saques_diarios}) atingido.")
                continue

            try:
                valor = float(input("Valor do saque: ").replace(",", "."))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            if valor <= 0:
                print("Operação falhou: valor de saque inválido.")
                continue
            if valor > limite_saque:
                print(f"Operação falhou: valor excede o limite por saque de {format_brl(limite_saque)}.")
                continue
            if valor > saldo:
                print("Operação falhou: saldo insuficiente.")
                continue

            saldo -= valor
            saques_realizados += 1
            extrato.append(f"Saque: -{format_brl(valor)}")
            print(f"Saque realizado com sucesso. Saldo atual: {format_brl(saldo)}")
            print(f"Saques realizados hoje: {saques_realizados}/{limite_saques_diarios}")

        elif opc == 'e':
            print("\n==== Extrato ====")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for item in extrato:
                    print(item)
            print(f"\nSaldo atual: {format_brl(saldo)}")
            print("=================\n")

        elif opc == 'q':
            print("Encerrando. Obrigada por usar o Banco Python. Até logo!")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
