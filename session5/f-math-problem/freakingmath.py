def generate_quiz():
    # Hint: Return [x, y, op, result]
    import random
    import calculate
    
    x = random.randint (1,10)
    y = random.randint (1,10)
    op = random.choice (["+","-","*","/"])
    result = calculate.calc(x,y,op)
    q = random.choice ([result -1, result, result, result,result +1])
    return [x, y, op, q]

def check_answer(x, y, op, q, answer):
    import calculate
    result = calculate.calc(x,y,op)    
    if answer == True:
        if q == result:
            return True    
        else:
            return False
            
    if answer == False:
        if q != result:
            return True       
        else:
            return False
    
    

