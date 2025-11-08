
def calculadora():
    #variaveis locais

    while True:
        n1 = float(input('n >>'))
        op = input('+ | - | * | / ')

        if op == '+':
            n2 = float(input('n >>'))
            print('=', n1+n2)

        elif op == '-':
            n2 = float(input('n >>'))
            print('=', n1-n2)

        elif op == '*':
             n2 = float(input('n >>'))
             print('=', n1*n2)

        elif op == '/':
             n2 = float(input('n >>'))
             print('=', n1/n2)

        else:
            print('digite algo invalido')


calculadora()

        
        
        