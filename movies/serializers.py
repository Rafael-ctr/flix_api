from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from actors.serializers import ActorSerializers
from genres.serializers import GenreSerializer

class MovieModelSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1970")
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracter')
        return value
    

class MovieListDetailSerialilzer(serializers.ModelSerializer):
    #Vamos chamar os serializer para exibir o oobjeto as informações de Actors e de Genre
    actors = ActorSerializers(many=True)
    genre = GenreSerializer()

    #SerializersMethodField é um campo calculado do serealizers
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model= Movie
        #ordem de exbição dos dados 
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

#Quando crio um campo calculado é necessario crir uma função com o nome
#get_<nome_do_campo_calculado>
#O resultado dessa função será exibido em rate    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars')) ['stars__avg']

        if rate:
            return round(rate, 1) #diminuindo as casas decimais
        return None    
    

       