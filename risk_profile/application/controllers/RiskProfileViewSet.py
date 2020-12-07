from rest_framework import viewsets
from risk_profile.domain.suitability import Suitability as Model
from risk_profile.domain.suitability import serializer


class RiskProfileViewSet(viewsets.ModelViewSet):
    queryset = Model.Suitability.objects.all()
    serializer_class = serializer.SuitabilitySerializer
