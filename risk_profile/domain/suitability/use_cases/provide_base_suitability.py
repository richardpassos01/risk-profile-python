class ProvideBaseSuitability:
    def execute(self, input_dict, base_eligible_status, base_score):
        self.base_eligible_status = base_eligible_status
        self.base_score = base_score

        base_suitability = dict(
            auto = list(self.define_insurance_type_by_input_value(input_dict["vehicles"])),
            disability = self.create_base_insurance(),
            home = list(self.define_insurance_type_by_input_value(input_dict["houses"])),
            life = self.create_base_insurance(),
            renters = self.create_base_insurance()
        )

        return base_suitability
    

    def define_insurance_type_by_input_value(self, value):
        value_is_array = isinstance(value, list)

        if(value_is_array):
            base_insurance = map(self.create_base_insurance, value)
            return base_insurance

        return create_base_insurance


    def create_base_insurance(self, value = { "id": 0 }):
        return {
            "id": value["id"],
            "is_eligible": self.base_eligible_status,
            "risk_points": self.base_score,
        }