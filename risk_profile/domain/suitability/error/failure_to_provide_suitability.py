from http import HTTPStatus
from risk_profile.shared.error import custom_error
from risk_profile.domain.suitability.error import codes


failure_to_provide_suitability = custom_error.CustomError(
    'Unexpected error when providing user suitability',
    codes.SuitabilityErrorCode.INTERNAL_SERVER_ERROR.value,
    HTTPStatus.UNPROCESSABLE_ENTITY
)
