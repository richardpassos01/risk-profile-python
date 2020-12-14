from risk_profile.domain.suitability.error.failure_to_provide_suitability import failure_to_provide_suitability

class ProvideRiskProfile:
    def __init__(
        self,
        calculate_base_score,
        provide_base_suitability,
        determine_eligibility,
        calculates_risk_points_by_age,
        calculates_risk_points_by_income,
        calculates_risk_points_by_houses,
        calculates_risk_points_by_dependents,
        calculates_risk_points_by_marital_status,
        calculates_risk_points_by_vehicles,
        provide_suitability
    ):
        self.calculate_base_score = calculate_base_score
        self.provide_base_suitability = provide_base_suitability
        self.determine_eligibility = determine_eligibility
        self.calculates_risk_points_by_age = calculates_risk_points_by_age
        self.calculates_risk_points_by_income = calculates_risk_points_by_income
        self.calculates_risk_points_by_houses = calculates_risk_points_by_houses
        self.calculates_risk_points_by_dependents = calculates_risk_points_by_dependents
        self.calculates_risk_points_by_marital_status = calculates_risk_points_by_marital_status
        self.calculates_risk_points_by_vehicles = calculates_risk_points_by_vehicles
        self.provide_suitability = provide_suitability

    def execute(self, data):
        try:
            user = data
            base_score = self.calculate_base_score.execute(user)
            is_eligible = True

            risk_profile = self.provide_base_suitability.execute(user, is_eligible, base_score)
            
            self.determine_eligibility.execute(user, risk_profile)
            self.calculates_risk_points_by_age.execute(user, risk_profile);
            self.calculates_risk_points_by_income.execute(user, risk_profile);
            self.calculates_risk_points_by_houses.execute(user, risk_profile);
            self.calculates_risk_points_by_dependents.execute(user, risk_profile);
            self.calculates_risk_points_by_marital_status.execute(user, risk_profile);
            self.calculates_risk_points_by_vehicles.execute(user, risk_profile);
            
            return self.provide_suitability.execute(risk_profile)
        except Exception as error:
            raise failure_to_provide_suitability