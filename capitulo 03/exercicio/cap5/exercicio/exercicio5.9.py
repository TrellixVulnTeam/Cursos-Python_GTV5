

dividendo = int(input('Digite 1º numero: '))
divisor = int(input('Digite 2º numero: '))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
    
resto = x
print('%d  / %d = %d (quociente) %d (resto)' %(dividendo, divisor, quociente, resto))
