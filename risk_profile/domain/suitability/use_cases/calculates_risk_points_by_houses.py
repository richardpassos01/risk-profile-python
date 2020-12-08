from risk_profile.shared.enums.user_home_ownership_status import UserHomeOwnerShipStatus
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating
from risk_profile.domain.suitability.utils.calculator import add_risk_point_for_insurance
from risk_profile.domain.suitability.utils.calculator import find_insurance_by_reference_and_add_risk_point


class CalculateRiskPointsByHouses:
    def __init__(self):
        self.user_home_ownership_status = UserHomeOwnerShipStatus
        self.risk_points_rating = RiskPointsRating

    def execute(self, user, risk_profile):   
        if not "houses" in user:
            return
        
        for house in user["houses"]:
            house_is_mortgaged = house["ownership_status"] == self.user_home_ownership_status.MORTGAGED.value

            if house_is_mortgaged:
                find_insurance_by_reference_and_add_risk_point(
                    risk_profile["home"],
                    house["id"],
                    self.risk_points_rating.LOW_RISK.value
                )

                add_risk_point_for_insurance(
                    risk_profile["disability"],
                    self.risk_points_rating.LOW_RISK.value
                )