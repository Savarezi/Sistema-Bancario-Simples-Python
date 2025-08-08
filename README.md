# Sistema Bancário Simples - Python

Um sistema bancário simples desenvolvido em Python que permite realizar operações básicas como depósito, saque e consulta de extrato.

---

## Funcionalidades

- **Depósito:** aceita somente valores positivos e registra cada depósito.  
- **Saque:** permite até 3 saques por execução (dia), com limite de R$ 500,00 por saque e saldo suficiente.  
- **Extrato:** exibe todas as movimentações feitas e o saldo atual formatado em reais (R$).

---

## Como usar

1. Clone ou baixe o repositório.  
2. Execute o arquivo `banco.py` com Python 3:

   ```bash
   python banco.py
No menu que aparecerá no terminal, escolha a opção desejada:

d para depositar

s para sacar

e para visualizar o extrato

q para sair do programa

Siga as instruções na tela para inserir valores.

Requisitos
Python 3.x instalado na máquina.

Detalhes técnicos
O valor do depósito e saque aceita entradas com vírgula ou ponto como separador decimal.

O sistema controla a quantidade máxima de saques por execução para simular limite diário.

Extrato exibe as operações no formato brasileiro de moeda (R$ xxx.xxx,xx).

Exemplo de uso
csharp
Copiar
Editar
=== Banco Python - Menu ===
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Escolha uma opção: d
Valor do depósito: 1500,75
Depósito realizado com sucesso. Saldo atual: R$ 1.500,75

=== Banco Python - Menu ===
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Escolha uma opção: s
Valor do saque: 300
Saque realizado com sucesso. Saldo atual: R$ 1.200,75
Saques realizados hoje: 1/3

=== Banco Python - Menu ===
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Escolha uma opção: e

==== Extrato ====
Depósito: +R$ 1.500,75
Saque: -R$ 300,00

Saldo atual: R$ 1.200,75
=================

=== Banco Python - Menu ===
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Escolha uma opção: q
Encerrando. Obrigada por usar o Banco Python. Até logo!
Autor
Patrícia Oliveira

Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.