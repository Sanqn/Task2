from rest_framework import serializers
from .models import WbData, WbDataFile


class WbDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WbData
        fields = '__all__'


class WbDataFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WbDataFile
        fields = ['article', 'file']
