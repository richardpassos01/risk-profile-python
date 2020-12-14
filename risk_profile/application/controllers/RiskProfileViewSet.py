from rest_framework import viewsets
from risk_profile.application.container import use_cases
from risk_profile.domain.suitability.serializer import SuitabilitySerializer
from risk_profile.domain.user.serializer import UserSerializer
from rest_framework.response import Response

from django.utils.decorators import decorator_from_middleware
from risk_profile.application.middlewares.user_schema_validator import UserSchemaValidatorMiddleware

user_schema_validator = decorator_from_middleware(UserSchemaValidatorMiddleware)
 
class RiskProfileViewSet(viewsets.ModelViewSet):
    queryset = ""
    serializer_class = UserSerializer

    @user_schema_validator
    def create(self, request):
        provide_risk_profile = use_cases.create_provide_risk_profile()
        risk_profile = provide_risk_profile.execute(request.data)

        serializer = SuitabilitySerializer(risk_profile, many=False)
        return Response(serializer.data)
