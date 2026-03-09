from rest_framework import serializers
from genres.models import Genre

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre # Indica o model a ser o usado
        fields = '__all__' # quais os campos a serme usados no caso será todos
        # No campo fields posso informar uma lista de camapos a serem usados
        # da seguinte forma fields = ['id','name']

        