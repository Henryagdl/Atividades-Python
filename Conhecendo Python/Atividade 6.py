print("Sistema de ingresso para evento")

nomeparticipante = str(input("Digite o nome do participante: "))
idade = int(input("Digite a idade do participante: "))
categoria = str(input("Digite a categoria do participante (Estudante, Professor, Publico geral): "))
quantidadeingressos = int(input("Digite a quantidade de ingressos desejada: "))

ingresso = 0.00
desconto = 0.00

if quantidadeingressos < 1:
    print("Quantidade de ingressos inválida. O participante deve solicitar pelo menos 1 ingresso.")
    exit()
elif idade < 0:
    print("Idade inválida. A idade do participante não pode ser negativa.")
    exit()

if categoria.lower() == "estudante":
    ingresso = 20.00
elif categoria.lower() == "professor":
    ingresso = 25.00
elif categoria.lower() == "publico geral":
    ingresso = 40.00

if idade < 10:
    ingresso = 0.00
elif idade >=60:
    desconto = ingresso * 0.50
    ingresso = ingresso - desconto
elif quantidadeingressos >= 5:
    desconto = ingresso * 0.10
    ingresso = ingresso - desconto

total = ingresso * quantidadeingressos

print(f"Demonstrativo de ingresso para o participante: {nomeparticipante}")
print(f"Categoria: {categoria}")
print(f"Idade: {idade}")
print(f"Quantidade de ingressos: {quantidadeingressos}")
print(f"Valor do ingresso: R${ingresso:.2f}")
print(f"Desconto aplicado: R${desconto:.2f}")
print(f"Total a pagar: R${total:.2f}")


