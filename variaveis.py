# Variáveis e tipo de dados "básicos"

# Uma variável é um espaço na memória onde armazenamos um valor.

# <nome da var> = <valor>

nome = "Celmar"     # Variável do tipo string (texto), sempre entre aspas ("" ou '')
idade = 35          # var do tipo inteiro (núm sem casas decimais)
altura = 1.84       # var do tipo float (núm com casas decimais)
dev = True          # var do tipo boolean, valores lógicos (True/False)

# print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")

nome = input("Digite seu nome: ")               # Entrada de texto
idade = int(input("Digite sua idade: "))        # Entrada de texto convertida para int
altura = float(input("Digite sua altura: "))    # Entrada de texto convertida para float

print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")
