print("Sistema de salário mensal")

nomefuncionario = str(input("Digite o nome do funcionário: "))
horastrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valorhora = float(input("Digite o valor recebido por hora trabalhada: "))
horasextras = float(input("Digite a quantidade de horas extras trabalhadas: "))
valetransporte = str(input("O funcionário recebe vale transporte? (sim ou não): "))

salariobase = horastrabalhadas * valorhora
valorhoraextra = valorhora * 1.5
totalhorasextras = horasextras * valorhoraextra
salariobruto = salariobase + totalhorasextras

if salariobruto <= 1500:
    desconto = salariobruto * 0.05
elif salariobruto > 1500 and salariobruto <= 3000:
    desconto = salariobruto * 0.08
else:
    desconto = salariobruto * 0.11

if valetransporte.lower() == "sim":
    desconto = desconto + (salariobase * 0.06)

print("Demonstativo de salário do funcionário:", nomefuncionario)
print(f"Salário base: R${salariobase:.2f}")
print(f"Total de horas extras: R${totalhorasextras:.2f}")
print(f"Salário bruto: R${salariobruto:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Salário líquido: R${salariobruto - desconto:.2f}")
