from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculate_base_score import CalculateBaseScore


class CalculateBaseScoreTestCase(TestCase):
    def setUp(self):
        self.calculate_base_score = CalculateBaseScore()

    def test_return_risk_questions_sum(self):
        """
        Should return the sum about all numbers inside risk question list
        """

        user = dict(
            risk_questions = [0,1,2] 
        )

        result = self.calculate_base_score.execute(user)
        self.assertEquals(result, 3)