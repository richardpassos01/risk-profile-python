from risk_profile.domain.suitability.helper.risk_points_calculator import add_risk_point_for_insurance
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating

class CalculateRiskPointsByDependents:
    def __init__(self, logger):
        self.logger = logger
        self.risk_points_rating = RiskPointsRating

    def execute(self, user, risk_profile):   
        """
            Check if the user has dependents and add 1 risk point to both,
            disability and life scores.
        """
        if user["dependents"]:
            add_risk_point_for_insurance(
                risk_profile["disability"],
                self.risk_points_rating.LOW_RISK.value
            )

            add_risk_point_for_insurance(
                risk_profile["life"],
                self.risk_points_rating.LOW_RISK.value
            )

            self.logger.info('{} risk points were add from Disability and Life insurance because the user has dependents.'
                .format(self.risk_points_rating.LOW_RISK.value,)
            )

