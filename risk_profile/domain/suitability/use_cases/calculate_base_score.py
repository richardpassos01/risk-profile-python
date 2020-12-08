class CalculateBaseScore:
    def execute(self, user):
        "sum() is an inbuilt function in python that adds"
        "all the elements in list,set and tuples and returns" 
        "the value"
          
        risk_questions = user["risk_questions"]
        base_score = sum(risk_questions) 

        return base_score
    