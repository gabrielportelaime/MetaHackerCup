respostas = open("A2_answer.txt", "w")

for i in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    simples = [0, 1, 2, c//a]
    valores = []
    for alternativa in simples:
        duplo = (c - alternativa*a)//b
        tem_pao = 2*(alternativa+duplo)
        tem_recheio = 2*duplo + alternativa
        if(tem_pao < 2 or tem_recheio < 1):
            valores.append(0)
        else:
            valores.append(min(tem_pao-1, tem_recheio))
    print(f'Case #{i+1}: {max(valores)}')
    respostas.write(f'Case #{i+1}: {max(valores)}' + '\n')