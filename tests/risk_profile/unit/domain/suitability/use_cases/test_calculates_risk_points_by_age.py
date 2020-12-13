import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculates_risk_points_by_age import CalculateRiskPointsByAge
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating

class CalculateRiskPointsByAgeTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.calculates_risk_points_by_age = CalculateRiskPointsByAge()
        self.risk_points_rating = RiskPointsRating
 
    def test_calculates_risk_points_by_senior_age(self):
        """Should not change risk_profile because user does not meet score calculation criteria"""

        self.user["age"] = 75

        self.calculates_risk_points_by_age.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile, MockRiskProfile.risk_profile)


    def test_calculates_risk_points_by_young_age(self):
        """
            Should deduct {} ris points from all lines of insurance when user is under the age of thirty
        """.format(self.risk_points_rating.MEDIUM_RISK.value)

        self.user["age"] = 25

        self.calculates_risk_points_by_age.execute(self.user, self.risk_profile)
        
        self.assertEquals(self.risk_profile["disability"]["risk_points"], -1)


    def test_calculates_risk_points_by_adult_age(self):
        """
            Should deduct {} from all lines of insurance when user is between 30 and 40 years old
        """.format(self.risk_points_rating.LOW_RISK.value)

        self.user["age"] = 35

        self.calculates_risk_points_by_age.execute(self.user, self.risk_profile)
        
        self.assertEquals(self.risk_profile["disability"]["risk_points"], 0)