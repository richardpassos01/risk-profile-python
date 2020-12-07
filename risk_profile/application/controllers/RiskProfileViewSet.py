from rest_framework import viewsets
from risk_profile.application.container import use_cases
from risk_profile.domain.suitability.serializer import SuitabilitySerializer
from rest_framework.response import Response
from risk_profile.domain.suitability import Suitability as Model

class RiskProfileViewSet(viewsets.ModelViewSet):
    queryset = Model.Suitability.objects.all()
    serializer_class = SuitabilitySerializer

    def create(self, request):
        provide_risk_profile = use_cases.create_provide_risk_profile()
        risk_profile = provide_risk_profile.execute(request.data)
       
        serializer = SuitabilitySerializer(self.queryset, many=True)
        return Response(serializer.data)
