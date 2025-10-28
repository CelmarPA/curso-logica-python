# CONDICIONAIS

# São estruturas que permitem ao nosso programa tomar decisões com base
# em determinadas condições. Em outras palavras, o programa pode executar
# ações diferentes dependendo de uma situação específica.add()

# Exemplo:

# Você está em uma cafeteria e está  com pouca grana.
# O cappuccino custa 10 reais, café com leite 7 e o café simples 4.

# Se você tiver 10 reais ou mais na carteira, pode pedir o cappuccino.add()
# Se você tiver 7 reais ou mais, pode pedir o café com leite.
# Se não, pede o café simples.

# Sintaxe básica no Python!

# if - "se"
# else - "se não"
# elif - "se + se não"


# if condição:
    # Código a ser executado se a condição for verdadeira
# elif outra_condição:
    # Código executado se a primeira condição for falsa, mais essa for verdadeira
# else:
    # Código executado se nenhuma das condições anteriores for verdadeira


# EXEMPLOS

# Verificando a idade para entrada em um evento (18 ANOS)

idade = int(input("Digite sua idade: "))    # Usuário digita a idade

if idade >= 18:
    print("Você pode entrar no evento!")
else:
    print("Desculpe, você ainda não tem idade suficiente para entrar.")


# Verificando a nota de um aluno

nota = float(input("Digite sua nota: "))    # Usuário insere a nota

if nota >=7:
    print("Parabéns! Você passou de ano!")
elif nota >=5:
    print("Você está de recuperação. Estude mais e tente novamente.")
else:
    print("Infelizmente, você foi reprovado. Tente novamente no próximo ano.")

    