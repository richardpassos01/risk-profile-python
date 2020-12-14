from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    dependents = serializers.IntegerField()
    houses = serializers.ListField()
    income = serializers.IntegerField()
    marital_status = serializers.ChoiceField(choices=["single", "married", "domestic_partnership", "divorced"])
    risk_questions = serializers.ListField()
    vehicles = serializers.ListField()