from rest_framework import serializers
from .models import Image, Effect

from django.core.files.base import ContentFile

import base64
import six
import uuid
import imghdr

class Base64ImageField(serializers.ImageField):
    """Base64 configurations"""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name = id.urn[9:] + '.' + ext)
            
        return super(Base64ImageField, self).to_internal_value(data)

class ImageSerializer(serializers.ModelSerializer):
    """Image model serializer"""
    
    # image = serializers.ImageField(max_length=None, use_url=True)
    image = Base64ImageField(
        max_length=None,
        use_url=True
    )
    
    class Meta:
        model = Image
        fields = ['image']

class EffectSerializer(serializers.ModelSerializer):
    """Effect model serializer"""
    
    image = Base64ImageField(
        max_length=None,
        use_url=True
    )
    
    class Meta:
        model = Effect
        fields = ['id', 'preview', 'title', 'description']
