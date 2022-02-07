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

usuarios = {1,5,76,34,52,13,17}
len(usuarios)

usuarios.add(50)
len(usuarios)

usuarios = frozenset(usuarios) #Conjunto congelado


print('\n#######################\n')

#Dictionary

#Formas de criar dicionarios
aparicoes = dict(Juh = 34, Hope = 10, Momo = 7)
aparicao = {
    "Juh" : 34,
    "Hope" : 10,
    "Momo" : 7
}

aparicoes['Manu'] = 29
print(aparicoes)

del aparicoes['Manu']
print(aparicoes)


#Busca nas chaves
"Juh" in aparicoes

"Manu" in aparicoes


for elemento in aparicoes:
    print(elemento)
    
for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.items():
    print(elemento)
    
for chave, valor in aparicoes.items():
    print(chave, ' = ', valor)
    
#Concatenando palavra
['palavra {}'.format(chave) for chave in aparicoes.keys()]

print('\n------------\n')

#Contando repetições

meu_texto = "Bem vindo meu nome é Juliana Simoes , eu gosto de cachorros e gatos. Eu tenho 2 cachorros , mas nenhum gato"

meu_texto.lower()
print(meu_texto)

aparicoes = {}
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
    
aparicoes

print('\n------------\n')

#Defaultdict - dicionario padrao
from collections import defaultdict

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

aparicoes

print('\n------------\n')

aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1

aparicoes

print('\n------------\n')

from collections import Counter
aparicoes = Counter()
for palavra in meu_texto.split():
    aparicoes[palavra] += 1

aparicoes

print('\n------------\n')

aparicoes = Counter(meu_texto.split())
aparicoes


amazon = 'Agradecemos por assinar o Amazon Prime. Agora você pode assistir aos melhores filmes e séries no Prime Video, incluindo originais Amazon. E o melhor: sem qualquer custo adicional.'
light = 'esta é uma mensagem automática e não deve ser respondida. Marque esse remetente de e-mail como confiável. Mantenha seu cadastro sempre atualizado. Confira outras informações divulgadas na fatura clicando aqui. para cancelar sua Fatura Digital, clique aqui. Para enviar a sua sugestão ou solicitação para a Light, acesse nossos canais.'

aparicoes = Counter(amazon.lower())
total_de_caracteres = sum

