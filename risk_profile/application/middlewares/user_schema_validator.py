from http import HTTPStatus
from jsonschema import validate
from django.http import JsonResponse
from risk_profile.shared.error import custom_error
from risk_profile.application.error.codes import ApplicationErrorCode


class UserSchemaValidatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_template_response(self,_,response):
        return response

    def process_request(self, request):
        user = request.request.data
        return self.validate_user_schema(user)

    def validate_user_schema(self, user):
        schema = {
            "type" : "object",
            "properties" : {
                "age" : {
                    "type" : "integer",
                    "minimum": 0,
                    "exclusiveMaximum": 110
                },
                "dependents" : {
                    "type" : "integer",
                    "minimum": 0
                },
                "houses": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "minimum": 0
                            },
                            "ownership_status": {
                                "type": "string", 
                                    "enum": ["owned", "mortgaged", "rented"] 
                            }
                        }
                    }
                },
                "income": {
                    "type" : "integer",
                    "minimum": 0
                },
                "marital_status": {
                    "type": "string",
                    "enum": ["single", "married", "divorced", "domestic_partnership"]
                },
                "risk_questions": {
                    "type": "array",
                    "minItems": 3,
                    "maxItems": 3,
                    "items": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 1
                    }

                },
                "vehicles": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "minimum": 0
                            },
                            "year": {
                                "type": "integer", 
                                "minimum": 0
                            }
                        }
                    }
                }
            },
            "required": ["age", "dependents", "income", "marital_status", "risk_questions"]
        }

        try:
            return validate(user, schema)
        except Exception as error:
            raise custom_error.CustomError(
                error.message,
                ApplicationErrorCode.SCHEMA_VALIDATOR_ERROR.value,
                HTTPStatus.UNPROCESSABLE_ENTITY
            )