from risk_profile.shared.enums.user_home_ownership_status import UserHomeOwnerShipStatus
from risk_profile.shared.enums.user_definition_by_age import UserDefinitionByQuantityYears

class DetermineEligibility:
    def __init__(self, logger):
        self.logger = logger
        self.user_home_ownership_status = UserHomeOwnerShipStatus
        self.user_definition_by_age = UserDefinitionByQuantityYears


    def execute(self, user, risk_profile):
        self.determine_by_age(user, risk_profile)
        self.determine_by_income(user, risk_profile)
        self.determine_by_vehicle(user, risk_profile)
        self.determine_by_houses(user, risk_profile)


    def determine_by_age(self, user, risk_profile):
        if user["age"] > self.user_definition_by_age.SENIOR.value:
            risk_profile["disability"]["is_eligible"] = False
            risk_profile["life"]["is_eligible"] = False

            self.logger.info('Disability and Life insurance is not eligible because the user is over 60 years old')


    def determine_by_income(self, user, risk_profile):
        if not "income" in user or user["income"] == 0:
            risk_profile["disability"]["is_eligible"] = False
        
            self.logger.info('Disability insurance is not eligible because the user has no income')
            

    def determine_by_vehicle(self, user, risk_profile):
        if not "vehicles" in user:
            risk_profile["auto"]["is_eligible"] = False

            self.logger.info('Auto insurance is not eligible because the user has no vehicle')


    def determine_by_houses(self, user, risk_profile):
        if not "houses" in user:
            risk_profile["home"]["is_eligible"] = False
            
            self.logger.info('Home insurance is not eligible because the user has no home')
            return


        for house in user["houses"]:
            "For each house, it will be checked whether it is owned or rented."
            "If the user owns a home, the renter's insurance corresponding to that home will be ineligible."
            "If the user's home is rented, home insurance is not eligible"

            if house["ownership_status"] == self.user_home_ownership_status.OWNED.value:
                renters = [renter for renter in risk_profile["renters"] if renter.get('id') == house["id"]]
                renters[0]["is_eligible"] = False

                self.logger.info('Renters insurance is not eligible because the user is owned of house')


            if house["ownership_status"] == self.user_home_ownership_status.RENTEND.value:
                homes = [home for home in risk_profile["home"] if home.get('id') == house["id"]]
                homes[0]["is_eligible"] = False

                self.logger.info('Home insurance is not eligible because the user house is rented')
