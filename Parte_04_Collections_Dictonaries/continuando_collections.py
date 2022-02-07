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

print('\n------------\n')

#most_common, value, counter

g1 = '''Especialistas dizem: o Brasil vive hoje a pandemia dos não vacinados. São eles que enchem as UTIs de Covid em grande parte do pais. Esta semana, a Fiocruz levantou o sinal de alerta mais uma vez. Os pesquisadores, que monitoram as vagas de UTI em todo o país, destacam que, por causa da ômicron, a situação começou a mudar muito rápido em novembro, após setembro do ano passado ter sido o primeiro mês, desde o começo da pandemia, em que todos os estados tinham menos de 60% dos leitos ocupados.
A rede Dor, responsável por mais de 60 hospitais em 12 estados, registrava, no fim de dezembro do ano passado, 200 pacientes internados com Covid. Agora, são cerca de 1.400. “Em sua maioria são pessoas que estão com ciclos vacinais incompletos, principalmente as mais graves e que têm comorbidades, incluindo a idade mais avançada. É muito frequente as pessoas se envergonharem de contar que não estão vacinados. Bate o arrependimento e junto bate a vergonha”, conta Leandro Reis, vice-presidente médico da rede.
Perfil dos pacientes internados por Covid mostra importância de completar esquema vacinalEm São Paulo, no Hospital Emílio Ribas, da rede pública, 100% dos leitos destinados à Covid estão ocupados. A cada cinco internados, quatro não tomaram vacina ou estão com doses atrasadas. Um levantamento exclusivo mostrou que, nos últimos três meses, 85% dos pacientes que morreram no local não tinha vacinação completa. A publicitária Vitória Monteiro viveu esse pesadelo com a mãe, Marília, no ano passado. A aposentada não quis se vacinar e ficou três meses internada na UTI – 21 dias intubada – por causa do coronavírus. Agora, ela já está em dia com as suas doses.
“Eu digo para as pessoas que ainda não tiveram essa consciência para repensar. Esse vírus não é brincadeira, ele é traiçoeiro. Tem que tomar vacina. Aproveite essa chance que a gente está tendo, da vacina, e tome a primeira, a segunda, todas as doses necessárias para ficarem protegidos”, aconselha. A artesã Liliane França e as filhas não tiveram a mesma sorte de Vitória. Gerson, de Duque de Caxias, no estado no rio, não tinha tomado a vacina, e morreu de Covid após ser diagnosticado no dia 7 de setembro do ano passado. “Ele era muito forte, era saudável, novo. Acho que até ele mesmo não acreditava que pudesse ir à óbito, né? Ele já mostrava arrependimento por não ter tomado a vacina. Ele até tinha falado: quando eu me recuperar da Covid e você for tomar a segunda dose, eu vou junto com você para tomar a vacina. Não deu tempo”, emociona-se Liliane.
ISSO É FANTÁSTICO O podcast Isso É Fantástico está disponível no G1, Globoplay, Deezer, Spotify, Google Podcasts, Apple Podcasts e Amazon Music trazendo grandes reportagens, investigações e histórias fascinantes em podcast com o selo de jornalismo do Fantástico: profundidade, contexto e informação. Siga, curta ou assine o Isso É Fantástico no seu tocador de podcasts favorito. Todo domingo tem um episódio novo. PRAZER, RENATA'''
#light = 'esta é uma mensagem automática e não deve ser respondida. Marque esse remetente de e-mail como confiável. Mantenha seu cadastro sempre atualizado. Confira outras informações divulgadas na fatura clicando aqui. para cancelar sua Fatura Digital, clique aqui. Para enviar a sua sugestão ou solicitação para a Light, acesse nossos canais.'

def analisa_frequencia(texto):
    aparicoes = Counter(g1.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia/total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(5)
    for caractere, propocao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, propocao*100))

analisa_frequencia(g1)
