📚 Sistema Bancário Simples - Python 🏦

Um sistema bancário simples feito em Python que permite operações básicas: depósito, saque e extrato.

✨ Funcionalidades:

💰 Depósito: só aceita valores positivos e registra cada depósito.

🏧 Saque: máximo 3 saques por dia, limite de R$ 500 por saque e saldo suficiente.

📄 Extrato: mostra todas as movimentações e o saldo atual formatado em reais.

🛠️ Como usar:

Baixe ou clone o projeto.

Execute o arquivo banco.py com Python 3:
python banco.py

No menu, escolha a opção:

d para depositar

s para sacar

e para extrato

q para sair

Digite os valores conforme as instruções.

⚙️ Requisitos:

Python 3 instalado.

📋 Detalhes técnicos:

Entrada de valores aceita vírgula ou ponto como separador decimal.

Controla limite diário de saques.

Formatação de valores no padrão brasileiro: R$ 1.234,56.

💡 Exemplo de uso:

ruby
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

Escolha uma opção: s  
Valor do saque: 300  
Saque realizado com sucesso. Saldo atual: R$ 1.200,75  
Saques realizados hoje: 1/3

Escolha uma opção: e  
==== Extrato ====  
Depósito: +R$ 1.500,75  
Saque: -R$ 300,00  

Saldo atual: R$ 1.200,75  
=================  

Escolha uma opção: q  
Encerrando. Obrigada por usar o Banco Python. Até logo!
👩‍💻 Autor:
Patrícia Oliveira

📄 Licença:
Projeto sob licença MIT.

