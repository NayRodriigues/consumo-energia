aparelho = input("Qual aparelho deseja calcular o consumo? ")
potencia = int(input("Qual a potência do aparelho em watts (W)? "))
uso_diario = int(input("Digite o uso diário em horas: "))

consumo_mensal = (potencia*uso_diario*30) / 1000
custo_estimado = (consumo_mensal*0.78)

print (f"Aparelho: {aparelho}")
print (f"Consumo estimado {int(consumo_mensal)} kWh/mês")
print (f"O custo estimado de energia do aparelho: {aparelho} será de aproximadamente R${custo_estimado:.2f}")
