from risk_profile.shared.enums.user_definition_by_age import UserDefinitionByQuantityYears
from risk_profile.shared.enums.risk_points_rating import RiskPointsRating
from risk_profile.domain.suitability.helper.risk_points_calculator import deduct_points_from_all_lines_of_insurance 
class CalculateRiskPointsByAge:
    def __init__(self):
        self.user_definition_by_age = UserDefinitionByQuantityYears
        self.risk_points_rating = RiskPointsRating

    def execute(self, user, risk_profile):   
        is_under_the_age_of_thirty = user["age"] < self.user_definition_by_age.YOUNG.value
        is_over_the_young_age = user["age"] >= self.user_definition_by_age.YOUNG.value
        is_under_the_adult_age = user["age"] <= self.user_definition_by_age.ADULT.value
        is_between_forty_and_fifty_years_old = is_over_the_young_age and is_under_the_adult_age
        number_of_risk_points_to_deduct = 0

        if not is_under_the_age_of_thirty and not is_between_forty_and_fifty_years_old:
            print('User does not meet score calculation criteria')
            return

        if not is_under_the_age_of_thirty:
            number_of_risk_points_to_deduct = self.risk_points_rating.MEDIUM_RISK.value

        if is_over_the_young_age:
            number_of_risk_points_to_deduct = self.risk_points_rating.LOW_RISK.value

        deduct_points_from_all_lines_of_insurance(risk_profile, number_of_risk_points_to_deduct)
