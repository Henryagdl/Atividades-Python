print("Simulador de compra com desconto")

cliente = str(input("Qual o seu nome?"))
produto = str(input("Qual o produto?"))
preco = float(input("Qual o preço unitario?"))
quantidade = int(input("Qual a quantidade do produto?"))
pagamento = str(input("Qual a forma de pagamento?"))

precoinicial = preco*quantidade
juros = 0

if pagamento == "pix":
    desconto = 0.9
elif pagamento == "dinheiro":
    desconto = 0.08
elif pagamento == "cartao de debito":
    desconto = 0.05
elif pagamento == "cartao de credito":
    desconto = 0
    parcelas = int(input("Qual a quantidades de parcelas?"))
    if parcelas <= 3:
        juros = 0
    else:
        juros = 0.06
else:
    print("Pagamento invalido")

valorfinal = precoinicial * (1 - desconto) * (1 + juros)

print("O preço total do produto é: ",precoinicial)
print("O desconto foi de:",desconto)
print("O acrecimo foi de: ",juros)
print(f"Valor final para pagamento {valorfinal: .2f}")