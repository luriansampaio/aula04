# # Verifica maioridade 
# idade = int(input('Informe sua idade:'))

# if idade >= 18:
#     print('Você é maior de idade.')
# else:
#     # print('Você é menor de idade.')


# Testando mais condições
# Teste de pontos

# pontos = int(input('Quantos pontos?'))

# if pontos >= 100:
#     print('Nível máximo!')
# elif pontos >= 50:
#     print("Nível bom!")
# elif pontos >= 25:
#     print('Pontuação ruim')    
# # else:

# # Verificação de login 
# usuario = input('Informe o usuario:').upper()
# senha = input('Digite a senha:')

# print(usuario)

# if usuario == 'admin' and senha == '1234':
#     print('O pai tá on')
# else:
#     print('Ops! Usuário ou senha incorretos!')

# # Condição para brinde
# compra = float(input('Digite o valor da compra:'))
# cliente_frequente = input('Cliente frequente? [S/N]').lower()

# if compra >= 1000 or cliente_frequente == 's':
#     print('Tem direito a brinde!')
# else:
#     print('Sem brinde!')

nota = float(input('Informe a nota:'))
frequencia = float(input('Informe a frequencia:'))

if nota >= 7: 
    if frequencia >= 75:
        print('APROVADO!')
    else:
        print('Boa nota, mas reprovado por falta!')
else:
    print('Reprovado por nota!')
    






