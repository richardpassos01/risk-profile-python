from risk_profile.shared.enums.insurances import InsuranceNames
from risk_profile.shared.enums.insurances import PointsToBeInsurance


class ProvideSuitability:
    def __init__(self):
        self.insurance_names = InsuranceNames
        self.points_to_be_insurance = PointsToBeInsurance

    def execute(self, risk_profile): 
        suitability = dict(
            auto = 
                list(self.map_insurances_to_create_suitabilities(risk_profile["auto"]))
                if isinstance(risk_profile["auto"], list)
                else self.create_suitability(risk_profile["auto"]),
            disability = self.create_suitability(risk_profile["disability"]),
            renters = 
                list(self.map_insurances_to_create_suitabilities(risk_profile["renters"]))
                if isinstance(risk_profile["renters"], list)
                else self.create_suitability(risk_profile["renters"]),
            home = 
                list(self.map_insurances_to_create_suitabilities(risk_profile["home"]))
                if isinstance(risk_profile["home"], list)
                else self.create_suitability(risk_profile["home"]),
            life = self.create_suitability(risk_profile["life"]),
        )

        return suitability 

    def map_insurances_to_create_suitabilities(self, insurances):
        suitabilities = []

        for insurance in insurances:
            suitability = self.create_suitability(insurance)
            
            suitabilities.insert(len(suitabilities), {
                "id": insurance["id"],
                "plan": suitability
            })
        
        return suitabilities

    def create_suitability(self, insurance):
        if not insurance["is_eligible"]:
            return self.insurance_names.INELIGIBLE.value
        

        if insurance["risk_points"] <= self.points_to_be_insurance.ECONOMIC.value:
            return self.insurance_names.ECONOMIC.value


        if insurance["risk_points"] >= self.points_to_be_insurance.RESPONSIBLE.value:
            return self.insurance_names.RESPONSIBLE.value


        return self.insurance_names.REGULAR.value
  
