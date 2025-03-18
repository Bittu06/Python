"""Write a program to fill in a letter template given below with name and date. 
letter = '''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
        '''
"""

Name = str(input("Enter your name: "))
Date = str(input("Enter the date: "))

letter = '''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
        ''' 
letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)
print(letter)