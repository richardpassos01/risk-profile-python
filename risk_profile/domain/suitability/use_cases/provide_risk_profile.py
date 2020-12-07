from risk_profile.domain.suitability import Suitability as Model


class ProvideRiskProfile:
    def __init__(
        self,
        calculate_base_score,
        determine_eligibility,
        provide_base_suitability
    ):
        self.calculate_base_score = calculate_base_score
        self.determine_eligibility = determine_eligibility
        self.provide_base_suitability = provide_base_suitability

    def execute(self, data):
        try:
            user = data
            base_score = self.calculate_base_score.execute(user)
            is_eligible = True

            risk_profile = self.provide_base_suitability.execute(user, is_eligible, base_score)
            
            self.determine_eligibility.execute(user, risk_profile)
            
            
            return risk_profile
        except Exception as e:
            print(e)
            if e.code==-2013:
                print ("Order does not exist.");
            elif e.code==-2014:
                print ("API-key format invalid.");
            #End If
