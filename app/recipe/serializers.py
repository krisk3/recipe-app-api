"""
Serializers for Recipe API
"""

from rest_framework import serializers

from core.models import Recipe

class RecipeSerializers(serializers.ModelSerializer):
    """Serializer for recipes"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']

