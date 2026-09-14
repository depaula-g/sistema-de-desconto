# Solicita o nome do cliente
nome = input("Digite seu nome para começarmos: ")

# Exibe uma mensagem de boas-vindas
print(f"Olá {nome}! Bem-vindo(a) à nossa loja online, vamos calcular o seu desconto.")

# Solicita o valor total da compra
valor = float(input("Digite o valor total da compra: "))

# Verifica a faixa de desconto e calcula o valor do desconto
if valor < 200:
    desconto = valor * 5 / 100

elif valor >= 200 and valor < 300:
    desconto = valor * 10 / 100

elif valor >= 300:
    desconto = valor * 15 / 100

# Calcula o valor final da compra
total = valor - desconto

# Exibe o desconto e o valor final a pagar
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total:.2f}")