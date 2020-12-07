from rest_framework import viewsets
from risk_profile.domain.suitability.use_cases import provide_risk_profile
from risk_profile.domain.suitability.serializer import SuitabilitySerializer
from rest_framework.response import Response
from risk_profile.domain.suitability import Suitability as Model

class RiskProfileViewSet(viewsets.ModelViewSet):
    queryset = Model.Suitability.objects.all()
    serializer_class = SuitabilitySerializer

    def create(self, request):
        use_case = provide_risk_profile.ProvideRiskProfile()
        risk_profile = use_case.execute(request.data)
       
        serializer = SuitabilitySerializer(queryset, many=True)
        return Response(serializer.data)
