idades = [39, 30, 27, 18]
len(idades)
idades[2]
idades.append(15)
idades
10 in idades

if 18 in idades:
    idades.remove(18)
    
idades.insert(2,31)
idades.extend([33,52])
idades
for idade in idades:
    print(idade + 1)

idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade+1)

idades_ano_que_vem

idades_ano_que_vem = [(idade+1) for idade in idades_ano_que_vem]

idades_ano_que_vem
