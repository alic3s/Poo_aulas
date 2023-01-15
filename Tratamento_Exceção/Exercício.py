'''n = int(input('Número: '))
print(f'Você digitou o número {n}')'''

#NameError
#ValueError

'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigada.')'''


#ZeroDivisionError
#TypeError

'''lst = [3, 6, 4]
print(lst[3])'''

#IndexError

# Toda exceção em python é filha
# de uma classe maior chamada Exception
# é meio que um erro, mas um erro que não
# ocorre sempre, o comando está digitado
# corretamente, não é umm erro sintático,
# mas ele está acontecendo

# usar a estrutura (TRY(operação) - EXCEPT(falhou) - ELSE(deu certo) - FINALLY(certo/falha))


def valido(num):
    while(num == 0):
        break

try:
    while True:
        vetor = []
        num = int(input('Informe o número: '))
        vetor.append(num)

except:
    if vetor > 9:
        print('Tamanho do vetor previsto foi excedido.')
    
    if TypeError:
        print('Tipo inválido.')

    while num == 0:
        vetor.append(num)
        print(vetor)
        break
