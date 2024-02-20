from rest_framework import viewsets
from .models import GameConsumable
from .serializers import GameConsumableSerializer

class GameConsumableViewSet(viewsets.ModelViewSet):
    queryset = GameConsumable.objects.all()
    serializer_class = GameConsumableSerializer
    
class GameConsumableDetail(RetrieveUpdateDestroyAPIView):
    queryset = GameConsumable.objects.all()  # Updated
    serializer_class = GameConsumableSerializer  # Updated