def deduct_points_from_all_lines_of_insurance(
    risk_profile,
    number_of_risk_points_to_deduct
):
    for insurance in risk_profile:
        if isinstance(risk_profile[insurance], list):
            for insurance_item in risk_profile[insurance]:
                insurance_item["risk_points"] -= number_of_risk_points_to_deduct
                
        if not isinstance(risk_profile[insurance], list):
            risk_profile[insurance]["risk_points"] -= number_of_risk_points_to_deduct


def find_insurance_by_reference_and_add_risk_point(
    insurances,
    reference_id,
    number_of_risk_points_to_add
):
    for insurance in insurances:
        if insurance["id"] == reference_id:
            insurance["risk_points"] += number_of_risk_points_to_add


def add_risk_point_for_insurance(
    insurance,
    number_of_risk_points_to_add
):
    insurance["risk_points"] += number_of_risk_points_to_add


def deduct_risk_point_for_insurance(
    insurance,
    number_of_risk_points_to_deduct
):
    insurance["risk_points"] -= number_of_risk_points_to_deduct