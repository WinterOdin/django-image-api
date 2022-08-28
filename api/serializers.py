from rest_framework import serializers
from .models import Pictures


class PictureSerializer(serializers.ModelSerializer):
    image_large = serializers.ImageField(read_only=True)
    image_medium = serializers.ImageField(read_only=True)
    image_small = serializers.ImageField(read_only=True)

    class Meta:
        model = Pictures
        fields = [
            'created_at',
            'updated_at',
            'title',
            'slug',
            'image',
            'image_large',
            'image_medium',
            'image_small',
        ]
