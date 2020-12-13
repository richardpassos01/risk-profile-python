import copy
from django.test import TestCase
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser
from risk_profile.application.container.use_cases import create_provide_risk_profile

class ProvideRiskProfileTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.provide_risk_profile = create_provide_risk_profile()
    

    def test_create_risk_profile(self):
        """Should generate a suitability for user"""
        
        risk_profile = self.provide_risk_profile.execute(self.user)

        expected = {
            "auto": [
                {
                    "id": 1,
                    "plan": "regular"
                }
            ],
            "disability": "ineligible",
            "renters": [
                {
                    "id": 1,
                    "plan": "ineligible"
                }
            ],
            "home": [
                {
                    "id": 1,
                    "plan": "regular"
                }
            ],
            "life": "regular"
        }

        self.assertEquals(risk_profile, expected)