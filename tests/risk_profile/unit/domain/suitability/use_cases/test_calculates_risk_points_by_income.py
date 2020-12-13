import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculates_risk_points_by_income import CalculateRiskPointsByIncome
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser

class CalculateRiskPointsByIncomeTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.calculates_risk_points_by_income = CalculateRiskPointsByIncome()

    def test_not_calculates_risk_points(self):
        """
            Should not deduct points from any lines of insurance to user with income below $200k
        """

        self.calculates_risk_points_by_income.execute(self.user, self.risk_profile)
        
        self.assertEquals(self.risk_profile, MockRiskProfile.risk_profile)

    
    def test_calculates_risk_points(self):
        """
            Should deduct 1 risk point from all lines of insurance to user with income above $200k
        """

        self.user["income"] = 250000.00

        self.calculates_risk_points_by_income.execute(self.user, self.risk_profile)
        
        self.assertEquals(self.risk_profile["auto"][0]["risk_points"],0)
        self.assertEquals(self.risk_profile["disability"]["risk_points"],0)
        self.assertEquals(self.risk_profile["home"][0]["risk_points"],0)
        self.assertEquals(self.risk_profile["life"]["risk_points"],0)
        self.assertEquals(self.risk_profile["renters"][0]["risk_points"],0)
