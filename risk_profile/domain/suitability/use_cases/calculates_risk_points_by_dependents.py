from risk_profile.domain.suitability.helper.risk_points_calculator import add_risk_point_for_insurance
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating

class CalculateRiskPointsByDependents:
    def __init__(self):
        self.risk_points_rating = RiskPointsRating

    def execute(self, user, risk_profile):   
        if user["dependents"]:
            add_risk_point_for_insurance(
                risk_profile["disability"],
                self.risk_points_rating.LOW_RISK.value
            )

            add_risk_point_for_insurance(
                risk_profile["life"],
                self.risk_points_rating.LOW_RISK.value
            )