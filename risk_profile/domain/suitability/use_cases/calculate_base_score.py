class CalculateBaseScore:
    def execute(self, input_dto):
        # sum() is an inbuilt function in python that adds  
        # all the elements in list,set and tuples and returns 
        # the value
          
        risk_questions = input_dto["risk_questions"]
        base_score = sum(risk_questions) 

        return base_score
    
