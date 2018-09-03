from rest_framework_mongoengine import serializers
from .models import ScoringData


class ScoringDataSerializer(serializers.DocumentSerializer):
    class Meta:
        model = ScoringData
        fields = '__all__'