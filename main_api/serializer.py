from rest_framework import serializers
from .models import Crib

class CribSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crib
        fields = ['id', 'title', 'description','created']
