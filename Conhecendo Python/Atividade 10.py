print("Cálculo do valor da conta de água")

nomecliente = str(input("Digite o nome do cliente: "))
consumoagua = float(input("Digite o consumo de água em m³: "))
tipoimovel = str(input("Digite o tipo de imóvel (residencial ou comercial): "))

# - Declarar variáveis para armazenar o valor da taxa fixa, multa e valor final da conta de água
taxafixa = 12.00
multa = 0.00

# - Calcular o valor da conta de água com base no tipo de imóvel e no consumo de água, aplicando a taxa fixa e a multa, se houver
if tipoimovel == "residencial": 
    if consumoagua <= 0:
        print("Consumo inválido")
        exit()
    elif consumoagua <= 10:
        valoragua = consumoagua * 2.00
        clasificaçao = "baixo consumo"
    elif consumoagua >=11 and consumoagua <= 20:
        valoragua = consumoagua * 3.00
        clasificaçao = "consumo moderado"
    elif consumoagua > 20 and consumoagua <= 30:
        valoragua = consumoagua * 4.50
        clasificaçao = "consumo elevado"
    else:
        multa = 0.9
        valoragua = consumoagua * 7.00 * (1 + multa)

elif tipoimovel == "comercial":
    if consumoagua <= 0:
        print("Consumo inválido")
        exit()
    elif consumoagua <= 10:
        valoragua = consumoagua * 3.50
        clasificaçao = "baixo consumo"
    elif consumoagua >=11 and consumoagua <= 20:
        valoragua = consumoagua * 5.00
        clasificaçao = "consumo moderado"
    elif consumoagua > 20 and consumoagua <= 30:
        valoragua = consumoagua * 7.00
        clasificaçao = "consumo elevado"
    else:
        multa = 0.9
        valoragua = consumoagua * 7.00 * (1 + multa)

# - Calcular o valor final da conta de água, incluindo a taxa fixa e a multa, se houver
valorfinal = valoragua + taxafixa

# - Exibir o resultado final, incluindo o nome do cliente, o consumo de água, a classificação do consumo, a taxa fixa, a multa e o valor final da conta de água
print(f"Nome do cliente: {nomecliente}")
print(f"Consumo de água: {consumoagua} m³")
print(f"consumo de água: {clasificaçao}")
print(f"Taxa fixa: R$ {taxafixa:.2f}")
print(f"multa: R$ {multa:.2f}")
print(f"Valor final: R$ {valorfinal:.2f}")