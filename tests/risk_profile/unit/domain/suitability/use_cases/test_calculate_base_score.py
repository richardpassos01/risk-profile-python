from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculate_base_score import CalculateBaseScore


class CalculateBaseScoreTestCase(TestCase):

    def setUp(self):
        self.calculate_base_score = CalculateBaseScore()

    def test_return_str(self):
        user = dict(
            risk_questions = [0,1,2] 
        )

        result = self.calculate_base_score.execute(user)
        self.assertEquals(result, 3)