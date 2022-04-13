from djoser.serializers import GroceryCreateSerializer, GrocerySerializer
from rest_framework import serializers
from . import models


class GroceryCreateSerializer(GroceryCreateSerializer):
    class Meta(GroceryCreateSerializer.Meta):
        model = models.Grocery
        fields = ('name', 'owner', 'nowHave', 'unitMeasure',
                  'eaten', 'purchased', 'img')
