numero1 = float(input('Informe o número 1 :'))
operecao = str(input('Operacao :'))
numero2 = int(input('Informe o número 2 :'))
resultado = 0
    
if operecao == '+':
    resultado = numero1 + numero2
elif operecao == '-':
    resultado = numero1 - numero2
elif operecao == '*':
    resultado = numero1 * numero2
elif operecao == '/':
    resultado = numero1 / numero2

print (resultado)