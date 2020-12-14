
from django.test import TestCase
import json

class UserSchemaValidatorTestCase(TestCase):
    def test_no_age(self):
        body = {
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

        response = self.client.post(
            '/risk-profile/', 
            json.dumps(body),
            content_type="application/json"
        )

        expected = {
            'message': "'age' is a required property",
            'code': 'VLD0001'
        }
        
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), expected)
    
    def test_negative_age(self):
        body = {
            "age": -1,
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

        response = self.client.post(
            '/risk-profile/', 
            json.dumps(body),
            content_type="application/json"
        )

        expected = {
            'message': '-1 is less than the minimum of 0',
            'code': 'VLD0001'
        }
        
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), expected)

    def test_unacceptable_age(self):
        body = {
            "age": 115,
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

        response = self.client.post(
            '/risk-profile/', 
            json.dumps(body),
            content_type="application/json"
        )

        expected = {
            'message': '115 is greater than or equal to the maximum of 110',
            'code': 'VLD0001'
        }
        
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), expected)

    def test_no_dependents(self):
        body = {
            "age": 35,
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

        response = self.client.post(
            '/risk-profile/', 
            json.dumps(body),
            content_type="application/json"
        )

        expected = {
            'message': "'dependents' is a required property",
            'code': 'VLD0001'
        }
        
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), expected)

    
    def test_negative_dependents(self):
        body = {
            "age": 35,
            "dependents": -10,
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

        response = self.client.post(
            '/risk-profile/', 
            json.dumps(body),
            content_type="application/json"
        )

        expected = {
            'message': '-10 is less than the minimum of 0',
            'code': 'VLD0001'
        }
        
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), expected)
    