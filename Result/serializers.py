from rest_framework import serializers
from Renyuan.models import Ceping


class CepingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceping
        fields = '__all__'
