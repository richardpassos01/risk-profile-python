import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.provide_base_suitability import ProvideBaseSuitability
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile


class ProvideBaseSuitabilityTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.provide_base_suitability = ProvideBaseSuitability()
    

    def test_create_base_suitability(self):
        base_eligible_status = True
        base_score = 1
        base_suitability = self.provide_base_suitability.execute(self.user, base_eligible_status, base_score)
        
        self.assertEquals(base_suitability, self.risk_profile)