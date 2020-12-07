from rest_framework import serializers
from risk_profile.domain.suitability import Suitability as Model


class SuitabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Model.Suitability
        fields = '__all__'
