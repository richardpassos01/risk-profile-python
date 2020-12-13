import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculates_risk_points_by_houses import CalculateRiskPointsByHouses
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser

class CalculateRiskPointsByHousesTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.calculates_risk_points_by_houses = CalculateRiskPointsByHouses()


    def test_not_calculates_risk_points_without_house(self):
        """
            Should not add risk point to any insurance when user have no house
        """

        del self.user["houses"]
        self.calculates_risk_points_by_houses.execute(self.user, self.risk_profile)
        self.assertEquals(self.risk_profile, MockRiskProfile.risk_profile)


    def test_calculates_risk_points_wit_one_house(self):
        """
            Should add 1 risk point to home insurance when user have one house
        """

        self.calculates_risk_points_by_houses.execute(self.user, self.risk_profile)

        for house in self.risk_profile["home"]:
            self.assertEquals(house["risk_points"], 2)
    
    
    def test_calculates_risk_points_wit_mortgaged_house(self):
        """
            Should add 1 risk point to home and disability insurance when house is mortgaged
        """

        self.user["houses"].insert(0, {
            "id": 123,
            "ownership_status": "mortgaged"
        })

        self.risk_profile["home"].insert(0, {
            "id": 123,
            "is_eligible": True,
            "risk_points": 1
        })

        self.calculates_risk_points_by_houses.execute(self.user, self.risk_profile)

        for house in self.risk_profile["home"]:
            if house["id"] == 123:
                self.assertEquals(house["risk_points"], 2)
            else: 
                self.assertEquals(house["risk_points"], 1)
        
        self.assertEquals(self.risk_profile["disability"]["risk_points"], 2)


    def test_calculates_risk_points_wit_one_mortgaged_house(self):
        """
            Should add 1 risk point to home and disability insurance when house is mortgaged
            and add more 1 when user has just one house
        """

        self.user["houses"] = [{
            "id": 1,
            "ownership_status": "mortgaged"
        }]

        self.risk_profile["home"] = [{
            "id": 1,
            "is_eligible": True,
            "risk_points": 1
        }]

        self.calculates_risk_points_by_houses.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile["home"][0]["risk_points"], 3)
        self.assertEquals(self.risk_profile["disability"]["risk_points"], 2)
