from risk_profile.domain.suitability.use_cases import provide_risk_profile
from risk_profile.domain.suitability.use_cases import determine_eligibility
from risk_profile.domain.suitability.use_cases import provide_base_suitability


def create_determine_eligibility():
    return determine_eligibility.DetermineEligibility()


def create_provide_base_suitability():
    return provide_base_suitability.ProvideBaseSuitability()


def create_provide_risk_profile():
    return provide_risk_profile.ProvideRiskProfile(
        create_determine_eligibility(),
        create_provide_base_suitability()
    )
