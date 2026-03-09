from django.db import models

# Criando um choices.
# Vamos criar um constante e criar uma tupla.
# Dentro dessa tupla vamos criar outras tuplas seguindo o padão ('BD, 'usuário')
NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('Brazil', 'Brasil'),
    ('Gran-bretania', 'Inglaterra'),
    ('Israel', 'Israel'),
    ('Canada', 'Canada')
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True) #Aceita o campo em branco/vazio
    nationality = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, null=True, blank=True
        )
    

#Metodo para exibir o campo name com o nome do actor e não com Object
    def __str__(self):
        return self.name
    
