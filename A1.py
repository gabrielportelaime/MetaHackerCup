respostas = open("A1_answer.txt", "w")

for i in range(int(input())):
    simples, duplos, k = [int(x) for x in input().split()]
    tem_pao = 2*(simples+duplos)
    tem_recheio = simples + 2*duplos
    if(tem_pao >= k+1 and tem_recheio >= k):
        print(f'Case #{i+1}: YES')
        respostas.write(f'Case #{i+1}: YES' + '\n')
    else:
        respostas.write(f'Case #{i+1}: NO' + '\n')
        print(f'Case #{i+1}: NO')