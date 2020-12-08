import datetime
from risk_profile.domain.suitability.utils.calculator import find_insurance_by_reference_and_add_risk_point
from risk_profile.shared.enums.vehicle_situation import VehicleSituation
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating

class CalculateRiskPointsByVehicles:
    def __init__(self):
        self.vehicle_situation = VehicleSituation
        self.risk_points_rating = RiskPointsRating

    def execute(self, user, risk_profile):   
        if not "vehicles" in user:
            return
        
        current_year = datetime.datetime.now().year

        for vehicle in user["vehicles"]:
            produced_how_many_years_ago = current_year - vehicle['year'];

            is_new_vehicle = produced_how_many_years_ago <= self.vehicle_situation.NEW.value

            if is_new_vehicle: 
                find_insurance_by_reference_and_add_risk_point(
                    risk_profile["auto"],
                    vehicle["id"],
                    self.risk_points_rating.LOW_RISK.value
                )