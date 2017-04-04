# Escreva uma função recursiva que retorne a soma de n até zero

global i
i = 0
def recursiva(n):
    global i
    i+= n
    if n == 0:
        return i
        return ""
    else:
        return recursiva(n -1)

print (recursiva(4))
    
