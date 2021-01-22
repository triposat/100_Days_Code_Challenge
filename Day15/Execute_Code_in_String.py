def Execute_Code(Test_string):
    return exec(Test_string)


Test_string = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
Execute_Code(Test_string)
