# qize_game for quick_test 

questions = [['Which of the following are invalid identifiers in Python?', 'Total-sum', 'Error', 'Error_count', 'None of these', 1],
['A_________ is a sequence of one or more characters used to provide a name for a given element.', 'Identifier', 'Variable', 'String', 'Characters', 1],

['Identify the invalid identifier below.',         '__2017discount', 'Profit', 'Total-discount', 'Totaldiscount', 3],     

['_______ are not allowed as part of an identifier.', 'Spaces', 'Numbers', 'Underscore', 'All of these', 1],     

['Identifiers may contain letters and digits, but cannot begin with a _____.', 'Character', 'Digit', 'Underscore', 'Special Symbols', 2],     

['Which is not a reserved keyword in Python?', 'Insert', 'Except', 'Import', 'Yield', 1],     

['Identify the invalid keyword below.', 'And', 'As', 'While', 'Until', 4],     ['________ is an identifier that has predefined meaning.', 'Variable', 'Identifier', 'Keyword', 'None of these', 3],

['Bitwise _______ operator gives 1 if one bit is zero and the other is 1.', 'Or', 'And', 'Xor', 'Not', 3],     

['Guess the output of the following code: 1 > 2 and 9 > 6', 'True', 'False', 'cMachine Dependent', 'Error', 2],     

['How many operands are there in the following arithmetic expression? -6*35+8-25', '4', '3', '5', '8', 3],     

['How many binary operators are there in the following arithmetic expression? -6+10/(23+56)', '2', '3', '5', '8', 2],     

['Which operator returns the remainder of operands?', '/', '//', '%', '**', 3],     

['A____________ is a name that is associated with a value.', 'Identifier', 'Keyword', 'Variable', 'None of these', 3],

['Guess the output of the following expression: float(22//3+3/3)', '8', '8.0', '-8.3', '8.333', 2],

 ['What value does the following expression evaluate to? 2 + 9 * ((3 * 12) / 10)', '27', '27.2', '30.8', 'None of these', 2],

['___________ and ________ are two ways to comment in Python.', 'Single and Multilevel comments', 'Single line and Double comments', 'One and Many lines comments', 'Single line and Multiline comments', 4],

 ['Single-line comments can be done by adding __________ symbol.', '*#', '#', '*', '&', 2], 

['Multiline comments can be done by adding _______ on each end of the comment.', "''' ''' (triple quote)", '#(Hash)', '$(dollar)', '%(modulus)', 1], 

['Python programs get structured through_______', 'Alignment', 'Indentation', 'Justification', 'None', 2], ]  
prizes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]  
score = 0  
for i, question in enumerate(questions):    
    print(f"Q{i+1}: {question[0]}")print(question[1])
    print(question[2]
    print(question[3])
    print(question[4])      
    try:         
       ans = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))     
   except:         
         print("Invalid input! Exiting the game.")         
         break      

if ans == question[5]:
  print("Correct Answer!\n") 
  score= prizes[i]     
else:         
    print(f"Incorrect! The correct answer was option {question[5]}") 
    print("Better luck next time!") 
    break  

print(f"You scored: {score}points") 

i +=1