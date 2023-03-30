from rest_framework import serializers
from .models import Contracts, Windows, Titles


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = '__all__'


class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = '__all__'