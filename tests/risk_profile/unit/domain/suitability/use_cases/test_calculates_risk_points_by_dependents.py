import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculates_risk_points_by_dependents import CalculateRiskPointsByDependents
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating

class CalculateRiskPointsByDependentsTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.calculates_risk_points_by_dependents = CalculateRiskPointsByDependents()
        self.risk_points_rating = RiskPointsRating


    def test_calculates_risk_points_by_dependents(self):
        """
            Should add 1 risk point to both the disability and life scores for user with dependents
        """

        self.calculates_risk_points_by_dependents.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile["disability"]["risk_points"], 2)
        self.assertEquals(self.risk_profile["life"]["risk_points"], 2)


    def test_not_calculates_risk_points(self):
        """
            Should not add 1 risk point to both the disability and life scores for user without dependents
        """

        self.user["dependents"] =  0
        self.calculates_risk_points_by_dependents.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile["disability"]["risk_points"], 1)
        self.assertEquals(self.risk_profile["life"]["risk_points"], 1)
