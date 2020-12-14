
import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.determine_eligibility import DetermineEligibility
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile
from tests.risk_profile.unit.domain.suitability.mock import logger as MockLogger


class DetermineEligibilityTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.determine_eligibility = DetermineEligibility(
            MockLogger.logger
        )

    def test_determine_by_age(self):
        """
        Should set disability and life insurance to be eligible when user is over 60 years old
        """
        
        self.user["age"] = 65

        self.determine_eligibility.execute(self.user, self.risk_profile)

        self.assertFalse(self.risk_profile["disability"]["is_eligible"])
        self.assertFalse(self.risk_profile["life"]["is_eligible"])


    def test_determine_by_income(self):
        """
        Should set disability insurance to be eligible when the user has no or zero income
        """
        del self.user["income"]
        
        self.determine_eligibility.execute(self.user, self.risk_profile)

        self.assertFalse(self.risk_profile["disability"]["is_eligible"])


    def test_determine_by_vehicle(self):
        """
        Should set auto insurance to be eligible when the user has no vehicle
        """
        
        del self.user["vehicles"]
        self.risk_profile["auto"] = dict(
            id = 1,
            is_eligible = True,
            risk_points = 1
        )

        self.determine_eligibility.execute(self.user, self.risk_profile)

        self.assertFalse(self.risk_profile["auto"]["is_eligible"])
    
      
    def test_determine_without_houses(self):
        """
        Should set home insurance to be eligible when the user has no house
        """
        
        del self.user["houses"]
        self.risk_profile["home"] = dict(
            id = 1,
            is_eligible = True,
            risk_points = 1
        )

        self.determine_eligibility.execute(self.user, self.risk_profile)

        self.assertFalse(self.risk_profile["home"]["is_eligible"])


    def test_determine_by_houses(self):
        """
        Should set home insurance to be eligible when the house is rented,
        and set renters to be eligible when the user is owns home. 
        """
        
        self.user["houses"] = [
            dict(
                id = 123,
                ownership_status = "owned"
            ),
            dict(
                id = 456,
                ownership_status = "rented"
            )
        ]

        self.risk_profile["home"] = [
            dict(
                id = 123,
                is_eligible = True,
                risk_points = 1
            ),
            dict(
                id = 456,
                is_eligible = True,
                risk_points = 1
            )
        ]

        self.risk_profile["renters"] = [
            dict(
                id = 123,
                is_eligible = True,
                risk_points = 1
            ),
            dict(
                id = 456,
                is_eligible = True,
                risk_points = 1
            )
        ]

        self.determine_eligibility.execute(self.user, self.risk_profile)

        for home in self.risk_profile["home"]:
            if home["id"] == 123:
                self.assertTrue(home["is_eligible"])
            
            if home["id"] == 456:
                self.assertFalse(home["is_eligible"])


        for renters in self.risk_profile["renters"]:
            if renters["id"] == 123:
                self.assertFalse(renters["is_eligible"])
            
            if renters["id"] == 456:
                self.assertTrue(renters["is_eligible"])
