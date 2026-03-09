from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from genres.models import Genre
from genres.serializers import GenreSerializer



class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,) # Todos os autenticados
    #Buscar todos os generos da tabela Genre do BD
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    #Buscar todos os generos da tabela Genre do BD
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


            
        
