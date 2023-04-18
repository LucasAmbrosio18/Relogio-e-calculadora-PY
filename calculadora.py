# Funções matemáticas básicas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

# Imprime as opções disponíveis na calculadora
print("Opções disponíveis:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Pede ao usuário para escolher a operação desejada
opcao = int(input("Digite o número da operação desejada: "))

# Pede ao usuário para inserir os números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Chama a função apropriada com base na opção escolhida
if opcao == 1:
    resultado = adicao(num1, num2)
elif opcao == 2:
    resultado = subtracao(num1, num2)
elif opcao == 3:
    resultado = multiplicacao(num1, num2)
elif opcao == 4:
    resultado = divisao(num1, num2)
else:
    print("Opção inválida.")

# Imprime o resultado
print("O resultado da operação escolhida é:", resultado)