from fuzzywuzzy import fuzz

def check_sol_as_fuzzyset(ans, sol):
   '''
      Compare ans and sol by using fuzzyset
   '''

   try:
       ratio = fuzz.token_sort_ratio(ans, sol)
   except:
     # Error condition
     return {"is_error": True, "is_correct": False, "ratio": 0.0, "feedback": "Do not know"}
 
   if ratio > 98:
       response = {"is_error": False, "is_correct": True, "ratio": ratio, "feedback": "Seems correct"}
   else:
       response = {"is_error": False, "is_correct": False, "ratio": ratio, "feedback": "Seems incorrect"}

   return response


def grade_bigoh(ans, sol, x):
    '''
       Check that ans and sol of the variable x have the same order of magnitude.
       Examples:
       grade_bigoh('n', 'n', 'n')
       grade_bigoh('log(n)', 'n', 'n')
       grade_bigoh('logn(log(n))', 'log(n)', 'n')
    '''
    
    n = Symbol(x)
    ans = parse_expr(ans, evaluate=False)

    # unwrap if inside big-oh.
    if ans.is_Order:
      ans = ans.expr

    sol = parse_expr(sol, evaluate=False)
    
    l = limit(ans/sol, n, oo)
    if l.is_infinite:
       response = {"is_error": False, "is_correct": False, "ratio": 0.0, "feedback": "Your answer dominates the correct solution."}
    elif l.evalf() == 0.0:
        print(f"result = {l.evalf()}")        
        response = {"is_error": False, "is_correct": False, "ratio": 0.0, "feedback": "Your answer is dominated by the correct solution"}
    elif l.evalf() > 0.0:
        print(f"result = {l.evalf()}")        
        response = {"is_error": False, "is_correct": True, "ratio": 1.0, "feedback": "Your answer has the same asymptotic order as the solution."}
    else:
        response = {"is_error": True, "is_correct": False, "ratio": 0.0, "feedback": "Sorry I do not have useful feedback."}

    return response
