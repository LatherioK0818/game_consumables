from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from consumables.models import GameConsumable
from .serializers import GameConsumableSerializer

class GameConsumableList(ListCreateAPIView):
    queryset = GameConsumable.objects.all()
    serializer_class = GameConsumableSerializer
    
class GameConsumableDetail(RetrieveUpdateDestroyAPIView):
    queryset = GameConsumable.objects.all()  # Updated
    serializer_class = GameConsumableSerializer  # Updated