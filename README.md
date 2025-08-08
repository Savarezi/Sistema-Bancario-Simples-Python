# 🏦 Sistema Bancário Simples - Python

Um sistema bancário simples desenvolvido em Python, que permite realizar operações básicas como **depósito**, **saque** e **consulta de extrato**

   <img width="321" height="180" alt="image" src="https://github.com/user-attachments/assets/e8bff432-68eb-4a8a-836b-6bdb178103b5" />


---

## 🚀 Funcionalidades

- 💰 **Depósito:** aceita somente valores positivos e registra cada depósito.  
- 🏧 **Saque:** permite até 3 saques por dia, com limite de R$ 500,00 por saque e saldo suficiente.  
- 📄 **Extrato:** exibe todas as movimentações feitas e o saldo atual formatado em reais (R$).

---

## 🛠 Como usar

1. Clone ou baixe este repositório.  
2. Execute o arquivo `banco.py` com Python 3:

   ```bash
   python banco.py
# No menu do terminal, escolha a opção desejada:

- d para depositar

- s para sacar

- e para visualizar o extrato

- q para sair do programa

Siga as instruções na tela para inserir os valores.
--
# ⚙️ Requisitos
Python 3.x instalado.
--

📋 Detalhes técnicos
Entrada aceita vírgula ou ponto como separador decimal.

Limite diário de saques controlado por execução do programa.
--

Formatação de valores no padrão brasileiro (R$ 1.234,56).
--

💡 Exemplo de uso

# === Banco Python - Menu ===

- [d] Depositar

- [s] Sacar

- [e] Extrato

- [q] Sair

Escolha uma opção: d

Valor do depósito: 1500,75

Depósito realizado com sucesso. Saldo atual: R$ 1.500,75

Escolha uma opção: s

Valor do saque: 300

Saque realizado com sucesso. Saldo atual: R$ 1.200,75

Saques realizados hoje: 1/3

Escolha uma opção: e

# ==== Extrato ====
Depósito: +R$ 1.500,75

Saque: -R$ 300,00

Saldo atual: R$ 1.200,75
=================

Escolha uma opção: q

Encerrando. Obrigada por usar o Banco Python. Até logo!
--


📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
