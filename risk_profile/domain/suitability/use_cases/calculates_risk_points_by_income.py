from risk_profile.shared.enums.income_situation_by_money import IncomeSituationByMoney
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating
from risk_profile.domain.suitability.helper.risk_points_calculator import deduct_points_from_all_lines_of_insurance 


class CalculateRiskPointsByIncome:
    def __init__(self, logger):
        self.logger = logger
        self.income_situation_by_money = IncomeSituationByMoney
        self.risk_points_rating = RiskPointsRating


    def execute(self, user, risk_profile):
        if "income" in user and user["income"] > self.income_situation_by_money.SAFE.value:
            number_of_risk_points_to_deduct = self.risk_points_rating.LOW_RISK.value

            deduct_points_from_all_lines_of_insurance(risk_profile, number_of_risk_points_to_deduct)

            self.logger.info('{} risk points were deducted from all insurance lines because the user income is above {} dollars'
                .format(number_of_risk_points_to_deduct, self.income_situation_by_money.SAFE.value)
            )
