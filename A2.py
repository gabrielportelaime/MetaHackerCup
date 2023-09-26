respostas = open("A2_answer.txt", "w")

for i in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    valores = []
    duplo = c//b
    simples = (c - duplo*b)//a
    tem_pao = 2*(simples+duplo)
    tem_recheio = simples + 2*duplo
    if(tem_pao < 2 or tem_recheio < 1):
        resposta = 0
    else:
        resposta = min(tem_recheio, tem_pao-1)
    valores.append(resposta)
    simples = c//a
    duplo = (c - simples*a)//b
    tem_pao = 2*(simples+duplo)
    tem_recheio = simples + 2*duplo
    if(tem_pao < 2 or tem_recheio < 1):
        resposta = 0
    else:
        resposta = min(tem_recheio, tem_pao-1)
    valores.append(resposta)
    print(f'Case #{i+1}: {max(valores)}')
    respostas.write(f'Case #{i+1}: {max(valores)}' + '\n')