from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculate_base_score import CalculateBaseScore
from tests.risk_profile.unit.domain.suitability.mock import logger as MockLogger


class CalculateBaseScoreTestCase(TestCase):
    def setUp(self):
        self.calculate_base_score = CalculateBaseScore(
            MockLogger.logger
        )

    def test_return_risk_questions_sum(self):
        """
        Should return the sum about all numbers inside risk question list
        """

        user = dict(
            risk_questions = [0,1,2] 
        )

        result = self.calculate_base_score.execute(user)
        self.assertEquals(result, 3)