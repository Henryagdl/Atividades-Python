print("Sistema de resultado esolar")

nomeestudante = str(input("Digite o nome do estudante: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
percentualfrequencia = float(input("Digite o percentual de frequência do estudante: "))

media = (nota1 + nota2 + nota3) / 3

if nota1 < 0 or nota1 > 10:
    print("Nota inválida. As notas devem estar entre 0 e 10.")
    exit()

if nota2 < 0 or nota2 > 10:
    print("Nota inválida. As notas devem estar entre 0 e 10.")
    exit()

if nota3 < 0 or nota3 > 10:
    print("Nota inválida. As notas devem estar entre 0 e 10.")
    exit()

if percentualfrequencia < 75:
    situacao = "Reprovado"
    motivo = "Frequência insuficiente"

if percentualfrequencia >= 75 and media >= 7:
    situacao = "Aprovado"
    motivo = "Média suficiente e frequência adequada"
elif media >= 5 and media <7:
    situacao = "Recuperação"
    motivo = "Média insuficiente, mas frequência adequada"
else:
    situacao = "Reprovado"
    motivo = "Média e frequência insuficientes"

print("Nome do estudante:", nomeestudante)
print(f"Média final: {media:.2f}")
print(f"Percentual de frequência: {percentualfrequencia:.2f}%")
print(f"Situação: {situacao}")
