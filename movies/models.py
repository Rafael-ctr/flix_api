from django.db import models
from genres.models import Genre
from actors.models import Actor

class Movie(models.Model):
    title = models.CharField(max_length=500)  
    genre = models.ForeignKey(
        Genre, # Conectando o campo genre a tabela genres.models.Genre.
        on_delete=models.PROTECT,  # O on_delete, não permite a exclusão do genero que esteja sendo usado.
        # Exemplo: Drama está sendo usado por Movies.models.genre , não poderá ser excluido em Genres.models.genre
        related_name='movies' # Nome da relação das tabelas
    )                  
    release_date = models.DateField(null=True, blank=True)
    # ManyToManyFild = N para N . Um actors pode está em varios filmes
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null=True, blank=True) # TextField = a Texto livre
    

    def __str__(self):
     return self.title


