
from django.test import TestCase
import json

class RiskProfileTestCase(TestCase):
    def test_home_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


    def test_risk_profile(self):
        body = {
            "age": 35,
            "dependents": 2,
            "houses": [ 
                {
                    "id": 1, "ownership_status": "owned"
                }
            ],
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicles": [
                {
                    "id": 1, "year": 2019
                },
                {
                    "id": 2, "year": 2010
                },
                        {
                    "id": 3, "year": 2012
                }
            ]
        }

        expected = {
            "auto": [
                {
                    "id": 1,
                    "plan": "regular"
                },
                {
                    "id": 2,
                    "plan": "economic"
                },
                {
                    "id": 3,
                    "plan": "economic"
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

        response = self.client.post(
            '/risk-profile/', 
            json.dumps(body),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)