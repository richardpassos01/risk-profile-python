class ProvideBaseSuitability:
    def execute(self, user, base_eligible_status, base_score):
        self.base_eligible_status = base_eligible_status
        self.base_score = base_score


        base_suitability = dict(
            auto = 
                list(self.define_insurance_type_by_input_value(user["vehicles"]))
                if "vehicles" in user
                else self.create_base_insurance(),
            disability = self.create_base_insurance(),
            home = 
                list(self.define_insurance_type_by_input_value(user["houses"]))
                if "houses" in user
                else self.create_base_insurance(),
            life = self.create_base_insurance(),
            renters = 
                list(self.define_insurance_type_by_input_value(user["houses"]))
                if "houses" in user
                else self.create_base_insurance(),
        )

        return base_suitability
    

    def define_insurance_type_by_input_value(self, value):
        base_insurance = map(self.create_base_insurance, value)
        return base_insurance

    def create_base_insurance(self, value = { "id": 0 }):
        return {
            "id": value["id"],
            "is_eligible": self.base_eligible_status,
            "risk_points": self.base_score,
        }