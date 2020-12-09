from rest_framework import viewsets
from risk_profile.application.container import use_cases
from risk_profile.domain.suitability.serializer import SuitabilitySerializer
from rest_framework.response import Response
 
class RiskProfileViewSet(viewsets.ModelViewSet):
    queryset = ""
    serializer_class = SuitabilitySerializer

    def create(self, request):
        provide_risk_profile = use_cases.create_provide_risk_profile()
        risk_profile = provide_risk_profile.execute(request.data)
       
        serializer = SuitabilitySerializer(risk_profile, many=False)
        return Response(serializer.data)
