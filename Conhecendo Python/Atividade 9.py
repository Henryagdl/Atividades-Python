print("Sistema de abstecimento e viagem")

distancia = float(input("Qual a distancia da viagem em km?"))
consumo = float(input("Qual o consumo do veiculo em km/l?"))
quantidadecombustivel = float(input("Qual a quantidade de combustivel no tanque em litros?"))
preco = float(input("Qual o preço do combustivel?"))
pedagio = str(input("Havera pedágio? (sim ou não)"))

# - Calcular a quantidade de litros necessários para a viagem e o custo do combustível
litrosnecessarios = distancia / consumo
custo = litrosnecessarios * preco

# - Declarar variáveis para armazenar o valor do pedágio e o valor total do pedágio
quantdadepedagio = 0
valordopedagio = 0
valorpedagiototal = 0

# - Se houver pedágio, solicitar a quantidade de pedágios e o valor de cada pedágio, e calcular o valor total do pedágio
if pedagio == "sim":
    quantdadepedagio = int(input("Qual a quantidades de pedágios?"))
    valordopedagio = float(input("Qual o valor do pedágio?"))
    valorpedagiototal = int(quantdadepedagio) * float(valordopedagio)

# - Calcular a diferença entre a quantidade de combustível no tanque e a quantidade de litros necessários para a viagem
diferenca = quantidadecombustivel - litrosnecessarios
if diferenca < 0:
    print(f"Combustível insuficiente. Faltarão {-diferenca:.2f} litros")
else:
    print(f"Combustível suficiente. Sobrarão {diferenca:.2f} litros")

# - Calcular o valor total gasto na viagem, incluindo o custo do combustível e o valor total do pedágio
total = valorpedagiototal + custo

# - Exibir o resultado final, incluindo a quantidade de litros necessários, o custo do combustível, o valor total do pedágio e o valor total gasto na viagem
print(f"Quantidade de litros necessários: {litrosnecessarios:.2f} litros")
print(f"Valor gasto necessário: R$ {custo:.2f}")
print(f"Valor gasto com pedágios: R$ {valorpedagiototal:.2f}")
print(f"Valor total gasto na viagem: R$ {total:.2f}")

