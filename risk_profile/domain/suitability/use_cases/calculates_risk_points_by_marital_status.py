from risk_profile.shared.enums.user_marital_status import UserMaritalStatus
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating
from risk_profile.domain.suitability.utils.calculator import add_risk_point_for_insurance
from risk_profile.domain.suitability.utils.calculator import deduct_risk_point_for_insurance


class CalculateRiskPointsByMaritalStatus:
    def __init__(self):
        self.user_marital_status = UserMaritalStatus
        self.risk_points_rating = RiskPointsRating

    def execute(self, user, risk_profile):   
        if user["marital_status"] == self.user_marital_status.DOMESTIC_PARTNERSHIP.value:
            add_risk_point_for_insurance(
                risk_profile["life"],
                self.risk_points_rating.BIG_RISK.value
            )

            deduct_risk_point_for_insurance(
                risk_profile["disability"],
                self.risk_points_rating.LOW_RISK.value
            )
    
        if user["marital_status"] == self.user_marital_status.MARRIED.value: 
            add_risk_point_for_insurance(
                risk_profile["life"],
                self.risk_points_rating.LOW_RISK.value
            )

            deduct_risk_point_for_insurance(
                risk_profile["disability"],
                self.risk_points_rating.LOW_RISK.value
            )