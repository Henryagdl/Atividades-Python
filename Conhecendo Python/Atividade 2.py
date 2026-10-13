print ("Sistemas de Estacionamento")

placa = int(input("Qual a placa do veiculo"))
horas = int(input("Horas estacionadas: "))
cadastro = str(input("Tem cadastro?"))



if horas < 0:
    print("Horas invalidas")
    exit()   
elif horas <=1:
    valor = 8
elif horas >1 and horas <=3:
    valor = 15
elif horas >3 and horas <=6:
    valor = 25
else:
    valor = 40

if cadastro == "S":
    desconto = valor*0.9
elif cadastro == "N":
    desconto = valor*0
else:
    print("Opção invalida")
    exit()

final = desconto

print("Placa do veiculo: ",placa)
print("Tempo de permanencia: ",horas)
print("Valor original: ",valor)
print("Valor com desconto: ",desconto)
print("Valor final: ",final)


