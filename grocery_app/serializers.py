from rest_framework import serializers
from .models import Grocery


class GrocerySerializer(serializers.HyperlinkedModelSerializer):
    # reviews = serializers.HyperlinkedRelatedField(
    #     view_name='review_detail',
    #     many=True,
    #     read_only=True
    # )

    grocery_url = serializers.ModelSerializer.serializer_url_field(
        view_name='grocery_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Grocery
        fields = ('name', 'owner', 'nowHave', 'unitMeasure', 'eaten', 'purchased', 'img')
