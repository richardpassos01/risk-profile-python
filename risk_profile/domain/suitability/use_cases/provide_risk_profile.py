from risk_profile.domain.suitability import Suitability as Model


class ProvideRiskProfile:
    def __init__(
        self,
        determine_eligibility_use_case
    ):
        self.determine_eligibility = determine_eligibility_use_case

    def execute(self, data):
        try:
            value = self.determine_eligibility.execute('test')
            return value
        except True:
            return "Error"
