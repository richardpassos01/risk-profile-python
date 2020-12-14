import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculates_risk_points_by_marital_status import CalculateRiskPointsByMaritalStatus
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser
from tests.risk_profile.unit.domain.suitability.mock import logger as MockLogger


class CalculateRiskPointsByMaritalStatusTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.calculates_risk_points_by_marital_status = CalculateRiskPointsByMaritalStatus(
            MockLogger.logger
        )


    def test_not_calculates_risk_points_by_single_users(self):
        """
            Should not deduct or add points from any lines of insurance to single users.
        """

        self.user["marital_status"] = "single"
        self.calculates_risk_points_by_marital_status.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile, MockRiskProfile.risk_profile)


    def test_not_calculates_risk_points_by_divorced_users(self):
        """
            Should not deduct or add points from any lines of insurance to divorced users.
        """

        self.user["marital_status"] = "divorced"
        self.calculates_risk_points_by_marital_status.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile, MockRiskProfile.risk_profile)


    def test_calculates_risk_points_by_married_users(self):
        """
            Should add 1 risk point to the life score and remove 1 risk point from disability for married users.
        """

        self.user["marital_status"] = "married"
        self.calculates_risk_points_by_marital_status.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile["life"]["risk_points"], 2)
        self.assertEquals(self.risk_profile["disability"]["risk_points"], 0)


    def test_calculates_risk_points_by_domestic_partnership_users(self):
        """
            Should add 4 risk point to the life score and remove 1 risk point from disability for domestic partnership users.
        """

        self.user["marital_status"] = "domestic_partnership"
        self.calculates_risk_points_by_marital_status.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile["life"]["risk_points"], 5)
        self.assertEquals(self.risk_profile["disability"]["risk_points"], 0)
