import copy
from django.test import TestCase
from risk_profile.domain.suitability.use_cases.calculates_risk_points_by_vehicles import CalculateRiskPointsByVehicles
from tests.risk_profile.unit.domain.suitability.mock import risk_profile as MockRiskProfile
from tests.risk_profile.unit.domain.suitability.mock import user as MockUser

class CalculateRiskPointsByVehiclesTestCase(TestCase):
    def setUp(self):
        self.user = copy.deepcopy(MockUser.user)
        self.risk_profile = copy.deepcopy(MockRiskProfile.risk_profile)
        self.calculates_risk_points_by_vehicles = CalculateRiskPointsByVehicles()


    def test_calculates_risk_points_without_vehicle(self):
        """
            Should not calculate risk points without vehicle's
        """

        del self.user["vehicles"]
        self.calculates_risk_points_by_vehicles.execute(self.user, self.risk_profile)
        self.assertEquals(self.risk_profile, MockRiskProfile.risk_profile)


    def test_calculates_risk_points_with_one_vehicle(self):
        """
            Should add 1 risk point to auto insurance when user have one auto
        """

        self.calculates_risk_points_by_vehicles.execute(self.user, self.risk_profile)

        for auto in self.risk_profile["auto"]:
            self.assertEquals(auto["risk_points"], 2)
    
    
    def test_calculates_risk_points_with_new_vehicle(self):
        """
            Should add 1 risk point to auto insurance when vehicle was produced in the last 5 years,
        """

        self.user["vehicles"].insert(0, {
            "id": 123,
            "year": 2019
        })

        self.risk_profile["auto"].insert(0, {
            "id": 123,
            "is_eligible": True,
            "risk_points": 1
        })

        self.calculates_risk_points_by_vehicles.execute(self.user, self.risk_profile)

        for auto in self.risk_profile["auto"]:
            if auto["id"] == 123:
                self.assertEquals(auto["risk_points"], 2)
            else: 
                self.assertEquals(auto["risk_points"], 1)
        

    def test_calculates_risk_points_with_one_new_vehicle(self):
        """
            Should add 1 risk point to auto insurance when vehicle was produced in the last 5 years,
            and add more 1 when user has just one vehicle
        """

        self.user["vehicles"] = [{
            "id": 123,
            "year": 2019
        }]

        self.risk_profile["auto"] = [{
            "id": 123,
            "is_eligible": True,
            "risk_points": 1
        }]

        self.calculates_risk_points_by_vehicles.execute(self.user, self.risk_profile)

        self.assertEquals(self.risk_profile["auto"][0]["risk_points"], 3)
