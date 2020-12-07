from risk_profile.domain.suitability import Suitability as Model


class ProvideRiskProfile:
    def __init__(
        self,
        calculate_base_score,
        determine_eligibility_use_case,
        provide_base_suitability
    ):
        self.calculate_base_score = calculate_base_score
        self.determine_eligibility = determine_eligibility_use_case
        self.provide_base_suitability = provide_base_suitability

    def execute(self, data):
        try:
            base_score = self.calculate_base_score.execute(data)
            is_eligible = True

            base_suitability = self.provide_base_suitability.execute(data, is_eligible, base_score)
            
            self.determine_eligibility.execute('test')
            
            
            return base_suitability
        except Exception as e:
            print(e)
            if e.code==-2013:
                print ("Order does not exist.");
            elif e.code==-2014:
                print ("API-key format invalid.");
            #End If
