# Atividade 01

compras = float(input('Informe o valor das compras:'))
porcentagem_de_desconto = 0.16

if compras >= 250:
    desconto = (compras) * (porcentagem_de_desconto)
    valor_final = (compras) - (desconto)
    print(f"O valor final de desconto é: R$ {valor_final}")
else: 
    print('Não há desconto!')     













