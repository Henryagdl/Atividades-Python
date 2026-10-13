print("Simulador de empréstimos")

nomecliente = str(input("Digite o nome do cliente: "))
rendamensal = float(input("Digite a renda mensal do cliente: "))
valorsolicitado = float(input("Digite o valor do empréstimo solicitado: "))
quantidadeparcelas = int(input("Digite a quantidade de parcelas do empréstimo: "))
dividasematraso = str(input("O cliente possui dívidas em atraso? (sim ou não): "))

valorparcelas = valorsolicitado / quantidadeparcelas

if dividasematraso.lower() == "sim":
    situacaoemprestimo = "Reprovado"
    motivo = "Cliente possui dívidas em atraso"

elif valorparcelas > (rendamensal * 0.3):
    situacaoemprestimo = "Reprovado"
    motivo = "Valor das parcelas excede 30% da renda mensal"

elif valorsolicitado > (rendamensal * 10):
        situacaoemprestimo = "Reprovado"
        motivo = "Valor do empréstimo excede 10x a renda mensal"

elif quantidadeparcelas < 1 or quantidadeparcelas > 48:
    situacaoemprestimo = "Reprovado"
    motivo = "Quantidade de parcelas inválida"

else:
    situacaoemprestimo = "Aprovado"
    motivo = "Empréstimo aprovado"

if situacaoemprestimo == "Reprovado":
    print(f"Empréstimo para {nomecliente}. O empréstimo foi reprovado.")
    print(f"Motivo: {motivo}")

else:
    print(f"Empréstimo para {nomecliente}. O empréstimo foi aprovado.")
    print(f"Valor solicitado: R${valorsolicitado:.2f}")
    print("Quantidade de parcelas:", quantidadeparcelas)
    print(f"Valor das parcelas: R${valorparcelas:.2f}")