from risk_profile.domain.suitability.use_cases import provide_risk_profile
from risk_profile.domain.suitability.use_cases import determine_eligibility

def create_determine_eligibility():
    return determine_eligibility.DetermineEligibility()

def create_provide_risk_profile():
    return provide_risk_profile.ProvideRiskProfile(
        create_determine_eligibility()
    )
