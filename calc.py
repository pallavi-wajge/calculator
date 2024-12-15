from art import logo 

print(logo) 


#Calculator 

#Add 

def add(n1, n2): 

  return n1 + n2 

  

#sub 

def sub(n1, n2): 

  return n1 - n2 

  

#divide 

def div(n1, n2): 

  return n1/ n2 

  

#mul 

def mul(n1, n2): 

  return n1 * n2 

  

#dict 

operations = { 

  "+" : add, 

  "-" : sub, 

  "/" : div, 

  "*" : mul, 

} 

  

def calculator(): 

  num1 = float(input("Enter 1st number: ")) 

  

  for symbol in operations: 

    print(symbol) 

   

  end = False 

  while not end: 

    operation_sym = input("Pick symbol form the options: ") 

    num2 = float(input("Enter next number: ")) 

    answer = operations[operation_sym](num1, num2) 

    print(f" {num1} {operation_sym} {num2} = {answer} ") 

   

    if input('''Type "y" if you wish to conitnue, else type "n"''') == "y": 

      num1 = answer 

    else: 

      end = True 

      calculator() 


calculator() 

  

   

  

  

   
