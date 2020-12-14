import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.provide_suitability import ProvideSuitability
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile
from tests.risk_profile.unit.domain.suitability.mock import logger as MockLogger

class ProvideSuitabilityTestCase(TestCase):
    
    def setUp(self):
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.provide_suitability = ProvideSuitability(
            MockLogger.logger
        )
    

    def test_create_suitability(self):
        """Should create a suitability for user with many vehicle's and house's"""
        
        suitability = self.provide_suitability.execute(self.risk_profile)
        
        expected = {
            'auto': [{'id': 1, 'plan': 'regular'}],
            'disability': 'regular',
            'renters': [{'id': 1, 'plan': 'regular'}],
            'home': [{'id': 1, 'plan': 'regular'}],
            'life': 'regular'
        }

        self.assertEquals(suitability, expected)

    def test_create_suitability_default(self):
        """Should create a suitability for user with one or less vehicle's and house's"""

        self.risk_profile["home"] = dict(
            id = 0,
            is_eligible = True,
            risk_points = 1
        ) 

        self.risk_profile["auto"] = dict(
            id = 0,
            is_eligible = True,
            risk_points = 1
        )

        self.risk_profile["renters"] = dict(
            id = 0,
            is_eligible = True,
            risk_points = 1
        ) 
        
        suitability = self.provide_suitability.execute(self.risk_profile)
        
        expected = {
            'auto': 'regular',
            'disability': 'regular',
            'renters': 'regular',
            'home': 'regular',
            'life': 'regular'
        }

        self.assertEquals(suitability, expected)

    
    def test_create_ineligible_suitability(self):
        """Should create a suitability for ineligible insurances"""

        ineligible_risk_profile = {}

        ineligible_risk_profile["auto"] = dict(
            is_eligible = False
        )

        ineligible_risk_profile["disability"] = dict(
            is_eligible = False
        )

        ineligible_risk_profile["renters"] = dict(
            is_eligible = False
        )

        ineligible_risk_profile["home"] = dict(
            is_eligible = False
        ) 

        ineligible_risk_profile["life"] = dict(
            is_eligible = False
        )
        
        suitability = self.provide_suitability.execute(ineligible_risk_profile)
        
        expected = {
            'auto': 'ineligible',
            'disability': 'ineligible',
            'renters': 'ineligible',
            'home': 'ineligible',
            'life': 'ineligible'
        }

        self.assertEquals(suitability, expected)
