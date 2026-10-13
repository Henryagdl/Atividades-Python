print("Sistema de cálculo de frete")

nomecliente = str(input("Qual o seu nome? "))
valorcompra = float(input("Qual o valor da compra? "))
peso = float(input("Qual o peso do pedido (quilograma)? "))
regiao = str(input("Qual a região da entrega? "))
tipoentrega = str(input("Qual o tipo de entrega? "))

if regiao.lower() == "metropolitana":
    valorinicial = 12.00

elif regiao.lower() == "interior":
    valorinicial = 20.00

elif regiao.lower() == "outro estado":
    valorinicial = 35.00

else:
    print("Região inválida")
    exit()

if peso > 5:
    excesso = peso - 5
    valorpeso = excesso * 3.00

else:
    valorpeso = 0.00

totalfrete = valorinicial + valorpeso

total = valorcompra + totalfrete

print("Demonstrativo de frete")
print(f"Cliente: {nomecliente}")
print(f"Valor da compra: R$ {valorcompra:.2f}")
print(f"Peso do pedido: {peso:.2f} kg")
print(f"Região: {regiao}")
print(f"Tipo de entrega: {tipoentrega}")
print(f"Valor inicial do frete: R$ {valorinicial:.2f}")
print(f"Valor adicional pelo peso: R$ {valorpeso:.2f}")
print(f"Valor do frete: R$ {totalfrete:.2f}")
print(f"Total da compra com frete: R$ {total:.2f}")