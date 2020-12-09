from rest_framework import serializers

class SuitabilitySerializer(serializers.Serializer):
    auto = serializers.JSONField()
    disability = serializers.CharField(max_length=None)
    renters = serializers.JSONField()
    home = serializers.JSONField()
    life = serializers.CharField(max_length=None)
