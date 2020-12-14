class CalculateBaseScore:
    def __init__(self, logger):
        self.logger = logger
      
    def execute(self, user):
        "sum() is an inbuilt function in python that adds"
        "all the elements in list,set and tuples and returns" 
        "the value"
        
        risk_questions = user["risk_questions"]
        base_score = sum(risk_questions) 

        self.logger.info('The basic score by the sum of the answers to the risk questions is {}'.format(base_score))
        return base_score
    