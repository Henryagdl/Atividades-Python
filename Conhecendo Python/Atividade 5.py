print("Sistema de consumo de energia")

nomeconsumidor = str(input("Digite o nome do consumidor: "))
consumomensal = float(input("Digite o consumo mensal do consumidor (em kWh): "))
tipointalacao = str(input("Digite o tipo de instalação (Residencial, Comercial, Industrial): "))

taxa = 15.00
imposto = 0.12

if tipointalacao.lower() == "residencial":
    if consumomensal <= 100:
        valorconsumo = consumomensal * 0.60
    elif consumomensal > 100:
        valorconsumo = consumomensal * 0.75

elif tipointalacao.lower() == "comercial":
    if consumomensal <= 100:
        valorconsumo = consumomensal * 0.70
    elif consumomensal > 100:
        valorconsumo = consumomensal * 0.85

elif tipointalacao.lower() == "industrial":
    if consumomensal <= 100:
        valorconsumo = consumomensal * 0.80
    elif consumomensal > 100:
        valorconsumo = consumomensal * 0.95

if consumomensal > 100:
    clasificacao = "Baixo"

elif consumomensal > 100 and consumomensal <= 250:
    clasificacao = "Moderado"

else:
    clasificacao = "Elevado"

total = valorconsumo + taxa + (valorconsumo * imposto)

print(f"Demonstrativo de consumo de energia para o consumidor: {nomeconsumidor}")
print("valor do consumo: R$", valorconsumo)
print("Imposto: R$",imposto)
print("Taxa: R$", taxa)
print("Classificação do consumo:", clasificacao)
print("Total a pagar: R$", total)
