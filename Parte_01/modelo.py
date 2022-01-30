class Programa:
    def __init__(self,nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome
      
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f' {self.nome} - {self.ano} - {self.likes}'


class Filme (Programa):
    def __init__(self,nome, ano, duracao):        
        super().__init__(nome,ano)
        self.duracao = duracao
    
    def __str__(self):
        return f' {self.nome} - {self.ano} - {self.duracao} -  {self.likes}'
        

    
      
class Serie (Programa):
    def __init__(self,nome, ano, temporada):
        super().__init__(nome,ano)
        self.temporada = temporada

    def __str__(self):
        return f' {self.nome} - {self.ano} - {self.temporada} -  {self.likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self,item):
       return  self._programas[item]
        
    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)
        

        
filme = Filme('Vingadores', 2018, 160)
serie = Serie('Boba Fett', 2021, 1)


filme.dar_like()
filme.dar_like()
serie.dar_like()


filmes_series = [filme, serie]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

print ('demolidor' in playlist_fim_de_semana)


for programa in playlist_fim_de_semana:
    #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada
    print(programa)
    
