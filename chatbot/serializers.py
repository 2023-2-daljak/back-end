from rest_framework import serializers
from .models import chatbot


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatbot
        fields = ['name', 'phone_number', 'address']

