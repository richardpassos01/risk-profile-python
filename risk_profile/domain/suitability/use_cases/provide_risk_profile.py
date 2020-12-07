from risk_profile.domain.suitability import Suitability as Model


class ProvideRiskProfile:
    def __init__(
        self,
        determine_eligibility_use_case,
        provide_base_suitability
    ):
        self.determine_eligibility = determine_eligibility_use_case
        self.provide_base_suitability = provide_base_suitability

    def execute(self, data):
        try:
            value = self.determine_eligibility.execute('test')
            base_suitability = self.provide_base_suitability.execute(data, True, 1)
            
            return base_suitability
        except Exception as e:
            if e.code==-2013:
                print ("Order does not exist.");
            elif e.code==-2014:
                print ("API-key format invalid.");
            #End If
