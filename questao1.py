# Escreva uma função recursiva que imprima de um número x até um y 

def recursiva(x, y):
  print (x)
  if x == y :
    return ""
  return recursiva(x+1, y)
    
print(recursiva(2,6))
