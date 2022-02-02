usuarios_data_science = [7, 15, 96,10]
usuarios_machine_learning = [7, 27, 35, 10, 13]
assistiram = []
assistiram.extend(usuarios_data_science)
print(assistiram)

print('\n--------------\n')

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

#Conjuntos - os elementos não se repetem
set(assistiram)

set([1,2,3,1])

{4,5,6,7,4}

#Já criando sendo tipo set
usuarios_data_science = {7, 15, 96, 10}
usuarios_machine_learning = {7, 27, 35, 10, 13}

for usuario in set(assistiram):
    print(usuario)
    
usuarios_data_science = {7, 15, 96, 10}
usuarios_machine_learning = {7, 27, 35, 10, 13}

#Operações

usuarios_data_science | usuarios_machine_learning

usuarios_data_science & usuarios_machine_learning

usuarios_data_science - usuarios_machine_learning

usuarios_data_science ^ usuarios_machine_learning #OU exclusivo

fez_ds_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
27 in fez_ds_nao_fez_ml
