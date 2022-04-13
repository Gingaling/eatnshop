from rest_framework import generics  # <- import generics
from .models import Grocery  # <- don't forget your models
from .serializers import GrocerySerializer  # <- or serializers
from rest_framework import permissions
from grocery_app.permissions import IsOwnerOrReadOnly


class GroceryList(generics.ListCreateAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroceryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    permission_classes = [IsOwnerOrReadOnly]
