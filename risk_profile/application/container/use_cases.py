from risk_profile.application.logger.logger import Logger
from risk_profile.domain.suitability.use_cases import provide_risk_profile
from risk_profile.domain.suitability.use_cases import calculate_base_score
from risk_profile.domain.suitability.use_cases import provide_base_suitability
from risk_profile.domain.suitability.use_cases import determine_eligibility
from risk_profile.domain.suitability.use_cases import calculates_risk_points_by_age
from risk_profile.domain.suitability.use_cases import calculates_risk_points_by_income
from risk_profile.domain.suitability.use_cases import calculates_risk_points_by_houses
from risk_profile.domain.suitability.use_cases import calculates_risk_points_by_dependents
from risk_profile.domain.suitability.use_cases import calculates_risk_points_by_marital_status
from risk_profile.domain.suitability.use_cases import calculates_risk_points_by_vehicles
from risk_profile.domain.suitability.use_cases import provide_suitability

logger = Logger().get_instance()

def create_calculate_base_score():
    return calculate_base_score.CalculateBaseScore(
        logger
    )

def create_provide_base_suitability():
    return provide_base_suitability.ProvideBaseSuitability()

def create_determine_eligibility():
    return determine_eligibility.DetermineEligibility(
        logger
    )

def create_calculates_risk_points_by_age():
    return calculates_risk_points_by_age.CalculateRiskPointsByAge(
        logger
    )

def create_calculates_risk_points_by_income():
    return calculates_risk_points_by_income.CalculateRiskPointsByIncome(
        logger
    )

def create_calculates_risk_points_by_houses():
    return calculates_risk_points_by_houses.CalculateRiskPointsByHouses(
        logger
    )

def create_calculates_risk_points_by_dependents():
    return calculates_risk_points_by_dependents.CalculateRiskPointsByDependents(
        logger
    )

def create_calculates_risk_points_by_marital_status():
    return calculates_risk_points_by_marital_status.CalculateRiskPointsByMaritalStatus(
        logger
    )

def create_calculates_risk_points_by_vehicles():
    return calculates_risk_points_by_vehicles.CalculateRiskPointsByVehicles(
        logger
    )

def create_provide_suitability():
    return provide_suitability.ProvideSuitability(
        logger
    )

def create_provide_risk_profile():
    return provide_risk_profile.ProvideRiskProfile(
        create_calculate_base_score(),
        create_provide_base_suitability(),
        create_determine_eligibility(),
        create_calculates_risk_points_by_age(),
        create_calculates_risk_points_by_income(),
        create_calculates_risk_points_by_houses(),
        create_calculates_risk_points_by_dependents(),
        create_calculates_risk_points_by_marital_status(),
        create_calculates_risk_points_by_vehicles(),
        create_provide_suitability()
    )
