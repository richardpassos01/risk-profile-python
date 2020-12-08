from enum import Enum

class InsuranceNames(Enum):
    INELIGIBLE = "ineligible"
    ECONOMIC = "economic"
    RESPONSIBLE = "responsible"
    REGULAR = "regular"

class PointsToBeInsurance(Enum):
    ECONOMIC = 0
    RESPONSIBLE = 3

